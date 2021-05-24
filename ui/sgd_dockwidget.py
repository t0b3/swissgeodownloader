# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SwissGeoDownloaderDockWidget
                                 A QGIS plugin
 This plugin lets you comfortably download open geo data from sigstop.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-03-14
        git sha              : $Format:%H$
        copyright            : (C) 2021 by Patricia Moll
        email                : pimoll.dev@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
from qgis.PyQt.QtCore import pyqtSignal
from qgis.PyQt.QtGui import QColor
from qgis.PyQt.QtWidgets import (QDockWidget, QListWidget, QFileDialog,
                                 QMessageBox)
from qgis.gui import QgsExtentGroupBox
from qgis.core import (QgsCoordinateReferenceSystem, QgsCoordinateTransform,
                       QgsProject, QgsPoint, QgsRectangle, QgsApplication,
                       QgsMessageLog, Qgis)
from .sgd_dockwidget_base import Ui_sgdDockWidgetBase
from .waitingSpinnerWidget import QtWaitingSpinner
from .ui_utilities import (filesizeFormatter, getDateFromIsoString, addToQgis,
                           addOverviewMap, MESSAGE_CATEGORY)
from .fileListTable import FileListTable
from ..api.datageoadmin import ApiDataGeoAdmin, API_EPSG
from ..api.apiCallerTask import ApiCallerTask

VERSION = Qgis.QGIS_VERSION_INT

class SwissGeoDownloaderDockWidget(QDockWidget, Ui_sgdDockWidgetBase):

    closingPlugin = pyqtSignal()

    def __init__(self, interface, parent=None):
        """Constructor."""
        super(SwissGeoDownloaderDockWidget, self).__init__(parent)
        self.setupUi(self)
        self.iface = interface

        # Initialize variables
        self.datasetList = {}
        self.currentDataset = {}
        self.selectMode = None
        self.fileList = []
        self.fileListFiltered = {}
        self.filesListDownload = []
        self.currentFilter = self.tr('all')
        self.outputPath = None
        self.msgBar = self.iface.messageBar()
        self.msgLog = QgsMessageLog()
        
        # Coordinate system
        self.mapRefSys = self.iface.mapCanvas().mapSettings().destinationCrs()
        self.apiRefSys = QgsCoordinateReferenceSystem(API_EPSG)
        self.transformProj2Api = QgsCoordinateTransform(
            self.mapRefSys, self.apiRefSys, QgsProject.instance())
        self.transformApi2Proj = QgsCoordinateTransform(
            self.apiRefSys, self.mapRefSys, QgsProject.instance())
        
        # Init QgsExtentBoxGroup Widget
        self.guiExtentWidget: QgsExtentGroupBox
        self.guiExtentWidget.setOriginalExtent(self.iface.mapCanvas().extent(),
                                         self.mapRefSys)
        # Set current (=map view) extent
        self.guiExtentWidget.setCurrentExtent(self.iface.mapCanvas().extent(),
                                        self.mapRefSys)
        self.guiExtentWidget.setOutputExtentFromCurrent()

        # Deactivate unused ui-elements
        self.onUnselectDataset()
        self.guiDatasetStatus.hide()
        self.guiQuestionBtn.hide()
        self.questionTxt = []

        # File list table
        self.fileListTbl = FileListTable(self, self.guiFileListLayout)
        self.fileListTbl.sig_selectionChanged.connect(self.onFileSelectionChange)
        
        # Create spinners to indicate data loading
        # Spinner for dataset request
        self.spinnerDs = QtWaitingSpinner(self)
        self.spinnerDs.setRoundness(70.0)
        self.spinnerDs.setMinimumTrailOpacity(15.0)
        self.spinnerDs.setTrailFadePercentage(70.0)
        self.spinnerDs.setNumberOfLines(16)
        self.spinnerDs.setLineLength(16)
        self.spinnerDs.setLineWidth(5)
        self.spinnerDs.setInnerRadius(12)
        self.spinnerDs.setRevolutionsPerSecond(1)
        self.spinnerDs.setColor(QColor(100, 100, 100))
        self.verticalLayout_3.addWidget(self.spinnerDs)
        self.spinnerDs.start()
        
        # Spinner for file list request
        self.spinnerFl = QtWaitingSpinner(self)
        self.spinnerFl.setRoundness(70.0)
        self.spinnerFl.setMinimumTrailOpacity(15.0)
        self.spinnerFl.setTrailFadePercentage(70.0)
        self.spinnerFl.setNumberOfLines(16)
        self.spinnerFl.setLineLength(16)
        self.spinnerFl.setLineWidth(5)
        self.spinnerFl.setInnerRadius(12)
        self.spinnerFl.setRevolutionsPerSecond(1)
        self.spinnerFl.setColor(QColor(100, 100, 100))
        self.verticalLayout_4.addWidget(self.spinnerFl)
        
        # Connect signals
        self.guiShowMapBtn.clicked.connect(self.onShowMapClicked)
        self.guiInfoBtn.clicked.connect(self.onInfoClicked)
        
        self.guiDatasetList.currentItemChanged.connect(self.onDatasetSelected)
        self.guiFormat.currentTextChanged.connect(self.onOptionChanged)
        self.guiResolution.currentIndexChanged.connect(self.onOptionChanged)
        self.guiCoordsys.currentIndexChanged.connect(self.onOptionChanged)
        self.guiTimestamp.currentIndexChanged.connect(self.onOptionChanged)
        
        self.guiExtentWidget.extentChanged.connect(self.onExtentChanged)
        self.guiFullExtentChbox.clicked.connect(self.onUseFullExtentClicked)
        
        self.guiRequestListBtn.clicked.connect(self.onLoadFileListClicked)
        self.guiDownloadBtn.clicked.connect(self.onDownloadFilesClicked)
        self.guiFileType.currentIndexChanged.connect(self.onFilterOptionChanged)
        self.guiQuestionBtn.clicked.connect(self.onQuestionClicked)
        
        QgsProject.instance().crsChanged.connect(self.onMapRefSysChanged)
        self.iface.mapCanvas().extentsChanged.connect(self.onMapExtentChanged)
        
        # Finally, initialize apis and request available datasets
        # Create separate task for request to not block ui
        self.apiDGA = ApiDataGeoAdmin(self)
        caller = ApiCallerTask(self.apiDGA, self.msgBar, 'getDatasetList', {})
        # Listen for finished api call
        caller.taskCompleted.connect(
            lambda: self.onReceiveDatasets(caller.output))
        caller.taskTerminated.connect(
            lambda: self.onReceiveDatasets([]))
        QgsApplication.taskManager().addTask(caller)

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()
    
    def onMapRefSysChanged(self):
        """Listen for map canvas reference system changes and apply to new
        crs to extent widget."""
        self.mapRefSys = self.iface.mapCanvas().mapSettings().destinationCrs()
        # Update transformations
        self.transformProj2Api = QgsCoordinateTransform(
            self.mapRefSys, self.apiRefSys, QgsProject.instance())
        self.transformApi2Proj = QgsCoordinateTransform(
            self.apiRefSys, self.mapRefSys, QgsProject.instance())
        # Update displayed extent
        mapExtent: QgsRectangle = self.iface.mapCanvas().extent()
        self.updateExtentValues(mapExtent, self.mapRefSys)
    
    def onExtentChanged(self):
        self.resetFileList()
    
    def onMapExtentChanged(self):
        """Show extent of current map view in extent widget."""
        if self.guiExtentWidget.extentState() == 1:
            # Only update widget if its current state is to display the map
            #  view extent
            if self.guiGroupExtent.isEnabled() and self.guiExtentWidget.isEnabled():
                # Check if extent widget is currently active
                mapExtent: QgsRectangle = self.iface.mapCanvas().extent()
                self.updateExtentValues(mapExtent, self.mapRefSys)
    
    def onUseFullExtentClicked(self):
        if self.guiFullExtentChbox.isChecked():
            self.updateSelectMode()
            self.guiExtentWidget.setDisabled(True)
        else:
            self.guiExtentWidget.setDisabled(False)
            self.resetFileList()
            self.onMapExtentChanged()
    
    def onFilterOptionChanged(self, idx):
        if idx != -1:
            selectedFileType = self.guiFileType.itemText(idx)
            self.filterFileList(selectedFileType)
    
    def onShowMapClicked(self):
        message, level = addOverviewMap(self.iface.mapCanvas(),
                                        self.mapRefSys.authid())
        self.msgBar.pushMessage(f"{MESSAGE_CATEGORY}: {message}", level)
    
    def onInfoClicked(self):
        self.showDialog(self.tr('Swiss Geo Downloader - Info'),
            self.tr('PLUGIN_INFO').format('https://pimoll.github.io/swissgeodownloader/'), 'Ok')
    
    def updateExtentValues(self, extent, refSys):
        self.guiExtentWidget.setCurrentExtent(extent, refSys)
        self.guiExtentWidget.setOutputExtentFromCurrent()
    
    def onReceiveDatasets(self, datasetList):
        """Recieve list of available datasets"""
        self.datasetList = datasetList
        self.guiDatasetList.clear()
        if self.datasetList:
            for dsId in self.datasetList.keys():
                self.guiDatasetList.addItem(dsId)
        self.spinnerDs.stop()
    
    def onDatasetSelected(self, item: QListWidget):
        """Set dataset and load details on first selection"""
        self.currentDataset = self.datasetList[item.text()]
        
        if not 'selectByBBox' in self.currentDataset.keys():
            caller = ApiCallerTask(self.apiDGA, self.msgBar, 'getDatasetDetails',
                                   {'dataset': self.currentDataset})
            # Listen for finished api call
            caller.taskCompleted.connect(
                lambda: self.onLoadDatasetDetails(caller.output))
            caller.taskTerminated.connect(
                lambda: self.onLoadDatasetDetails(None))
            QgsApplication.taskManager().addTask(caller)
        else:
            self.applyDatasetState()
    
    def onLoadDatasetDetails(self, details):
        if details:
            for key, value in details.items():
                self.currentDataset[key] = value
        self.applyDatasetState()
    
    def onQuestionClicked(self):
        self.showDialog(self.questionTxt[0], self.questionTxt[1], 'Ok')
    
    def applyDatasetState(self):
        """Set up ui according to the options of the selected dataset"""
        # Show dataset in search field
        # self.guiSearchField.setText(self.currentDataset['id'])
        
        # Activate options and extent groups
        self.clearOptions()
        self.blockUiSignals()
        
        # Show dataset status if no files are available
        if self.currentDataset['isEmpty']:
            self.guiGroupOptions.setDisabled(True)
            self.guiGroupExtent.setDisabled(True)
            self.guiExtentWidget.setCollapsed(True)
            self.guiGroupFiles.setDisabled(True)
            self.resetFileList()
            self.guiDatasetStatus.show()
            self.guiDatasetStatus.setStyleSheet('QLabel { color : red; }')
            self.guiDatasetStatus.setText(self.tr('No files available in this dataset'))
            return
        else:
            self.guiDatasetStatus.setText('')
            self.guiDatasetStatus.hide()
        
        # Setup 2. Options
        self.guiGroupOptions.setDisabled(False)
        for optionKey, option in self.currentDataset['options'].items():
            if optionKey == 'format':
                self.guiFormat.addItems(option)
                # Only enable option if there is more than one choice
                if not len(option) == 1:
                    self.guiFormatL.setDisabled(False)
                    self.guiFormat.setDisabled(False)
            if optionKey == 'resolution':
                # Stringify resolution numbers
                optionStr = [str(r) for r in option]
                self.guiResolution.addItems(optionStr)
                if not len(option) == 1:
                    self.guiResolutionL.setDisabled(False)
                    self.guiResolution.setDisabled(False)
            if optionKey == 'coordsys':
                # Create a coordinate system object and get its friendly identifier
                coordSysList = [QgsCoordinateReferenceSystem(f'EPSG:{epsg}') for epsg in option]
                if VERSION < 31003:
                    coordSysNames = [cs.description() for cs in coordSysList]
                else:
                    coordSysNames = [cs.userFriendlyIdentifier() for cs in coordSysList]
                self.guiCoordsys.addItems(coordSysNames)
                if not len(option) == 1:
                    self.guiCoordsysL.setDisabled(False)
                    self.guiCoordsys.setDisabled(False)
            if optionKey == 'timestamp':
                # Format ISO time string into nice dates
                optionStr = [getDateFromIsoString(ts) for ts in option]
                self.guiTimestamp.addItems(optionStr)
                if not len(option) == 1:
                    self.guiTimestampL.setDisabled(False)
                    self.guiTimestamp.setDisabled(False)

        # Activate / deactivate 3. Extent
        if not self.currentDataset['selectByBBox']:
            self.guiExtentWidget.setCollapsed(True)
            self.updateSelectMode()
            self.guiGroupExtent.setDisabled(True)
        else:
            self.updateSelectMode()
            self.guiExtentWidget.setCollapsed(False)
            self.guiGroupExtent.setDisabled(False)
        
        # Activate 4. Files
        self.guiGroupFiles.setDisabled(False)
        self.resetFileList()
        self.currentFilter = self.tr('all')
        
        self.unblockUiSignals()
        
    def clearOptions(self):
        """Deactivate and disable option drop down menus"""
        self.blockUiSignals()
        self.guiFormat.clear()
        self.guiFormat.setDisabled(True)
        self.guiFormatL.setDisabled(True)
        self.guiResolution.clear()
        self.guiResolution.setDisabled(True)
        self.guiResolutionL.setDisabled(True)
        self.guiCoordsys.clear()
        self.guiCoordsys.setDisabled(True)
        self.guiCoordsysL.setDisabled(True)
        self.guiTimestamp.clear()
        self.guiTimestamp.setDisabled(True)
        self.guiTimestampL.setDisabled(True)
        self.unblockUiSignals()
    
    def blockUiSignals(self):
        self.guiFormat.blockSignals(True)
        self.guiResolution.blockSignals(True)
        self.guiCoordsys.blockSignals(True)
        self.guiTimestamp.blockSignals(True)
        self.guiFullExtentChbox.blockSignals(True)
    
    def unblockUiSignals(self):
        self.guiFormat.blockSignals(False)
        self.guiResolution.blockSignals(False)
        self.guiCoordsys.blockSignals(False)
        self.guiTimestamp.blockSignals(False)
        self.guiFullExtentChbox.blockSignals(False)
        
    def onUnselectDataset(self):
        self.currentDataset = {}
        self.clearOptions()
        # self.clearExtent()

        self.guiGroupOptions.setDisabled(True)
        self.guiGroupExtent.setDisabled(True)
        self.guiExtentWidget.setCollapsed(True)
        self.guiGroupFiles.setDisabled(True)
        self.guiDownloadBtn.setDisabled(True)
    
    def resetFileList(self):
        self.fileListTbl.clear()
        self.guiDownloadBtn.setDisabled(True)
        self.guiFileListStatus.setText('')
        self.guiFileListStatus.setStyleSheet('QLabel { color : black;}')
    
    def onOptionChanged(self, newVal):
        self.resetFileList()
    
    def updateSelectMode(self):
        if self.guiFullExtentChbox.isChecked():
            bbox = QgsRectangle(*tuple(self.currentDataset['bbox']))
            self.updateExtentValues(bbox, self.apiRefSys)
    
    def getBbox(self) -> list:
        """Read out coordinates of bounding box, transform coordinates if
        necessary"""
        if self.guiFullExtentChbox.isChecked():
            return []
        
        rectangle: QgsRectangle = self.guiExtentWidget.currentExtent()
        llCoord = (rectangle.xMinimum(), rectangle.yMinimum())
        urCoord = (rectangle.xMaximum(), rectangle.yMaximum())

        # Cancel if there are no actual coords in input fields
        if not all(llCoord) or not all(urCoord):
            return []

        llPoint = QgsPoint(*tuple(llCoord))
        urPoint = QgsPoint(*tuple(urCoord))
        llPoint.transform(self.transformProj2Api)
        urPoint.transform(self.transformProj2Api)
        return [llPoint.x(),
                llPoint.y(),
                urPoint.x(),
                urPoint.y()]

    def onLoadFileListClicked(self):
        """Collect options and call api to retrieve list of items"""
        # Remove current file list
        self.fileListTbl.clear()
        
        # Read out extent
        bbox = self.getBbox()
        if float('inf') in bbox:
            bbox = []
            
        # Read out options
        options = {}
        timestamp = ''
        for optionKey, option in self.currentDataset['options'].items():
            # Only add to query parameters if there is more than one choice
            if optionKey == 'format' and len(option) > 1:
                options[optionKey] = option[self.guiFormat.currentIndex()]
            if optionKey == 'resolution' and len(option) > 1:
                options[optionKey] = option[self.guiResolution.currentIndex()]
            if optionKey == 'coordsys' and len(option) > 1:
                options[optionKey] = option[self.guiCoordsys.currentIndex()]
            if optionKey == 'timestamp' and len(option) > 1:
                timestamp = option[self.guiTimestamp.currentIndex()]
        
        # Call api
        # Create a separate task for request to not block ui
        caller = ApiCallerTask(self.apiDGA, self.msgBar, 'getFileList', {
            'dataset': self.currentDataset,
            'bbox': bbox,
            'timestamp': timestamp,
            'options': options
        })
        # Listen for finished api call
        caller.taskCompleted.connect(
            lambda: self.onReceiveFileList(caller.output))
        caller.taskTerminated.connect(
            lambda: self.onReceiveFileList(None))
        # Start spinner to indicate data loading
        self.spinnerFl.start()
        # Add task to task manager
        QgsApplication.taskManager().addTask(caller)
    
    def onReceiveFileList(self, fileList):
        if fileList is None:
            fileList = []
        self.fileList = fileList
        # Update file type filter and file list
        self.updateFilterList()
        self.filterFileList(self.currentFilter)

        # Enable download button
        if self.fileList:
            self.guiDownloadBtn.setDisabled(False)

        self.spinnerFl.stop()
    
    def updateFilterList(self):
        self.guiFileType.blockSignals(True)
        self.guiFileType.clear()
        # Get unique values from extension list and add to drop down
        fileTypeList = list(set([file['ext'] for file in self.fileList]))
        if len(fileTypeList) == 1:
            fileTypeList = [self.tr('all')]
        else:
            fileTypeList.insert(0, self.tr('all'))

        self.guiFileType.addItems(fileTypeList)
        # Set list to 'all'
        if self.currentFilter not in fileTypeList:
            self.currentFilter = self.tr('all')
        
        self.guiFileType.setCurrentIndex(fileTypeList.index(self.currentFilter))
        self.guiFileType.blockSignals(False)
    
    def populateFileList(self, fileList):
        self.fileListTbl.fill(fileList)
        self.updateSummary()

    def filterFileList(self, filetype):
        if filetype == self.tr('all'):
            self.fileListFiltered = { file['id']: dict(file, **{'selected': True})
                                      for file in self.fileList }
        else:
            self.fileListFiltered = { file['id']: dict(file, **{'selected': True})
                                      for file in self.fileList
                                      if file['ext'] == filetype }
        self.currentFilter = filetype
        
        # This list is necessary because dictionaries do not have a stable
        #  order, but we want the original order from the API response
        orderedFilesForTbl = [file for file in self.fileList
                              if file['id'] in self.fileListFiltered.keys()]
        self.populateFileList(orderedFilesForTbl)
    
    def onFileSelectionChange(self, fileId, isChecked):
        if fileId in self.fileListFiltered.keys():
            self.fileListFiltered[fileId]['selected'] = isChecked
            self.updateSummary()
    
    def updateSummary(self):
        self.guiQuestionBtn.hide()
        
        selectedFiles = [file for file in self.fileListFiltered.values()
                            if file['selected']]
        
        if len(selectedFiles) > 0:
            fileSize = 0
            for file in selectedFiles:
                if file['type'] in self.currentDataset['size'].keys():
                    fileSize += self.currentDataset['size'][file['type']]

            # fileSize = sum([file['size'] for file in self.fileListFiltered])
            
            if fileSize > 0:
                status = self.tr("{} File(s) with an estimated total size of "
                    "{} are ready to download.").format(len(selectedFiles),
                                                        filesizeFormatter(fileSize))
            else:
                status = self.tr("{} File(s) are ready to download.").format(len(selectedFiles))
            
            if len(selectedFiles) >= 100:
                self.guiQuestionBtn.show()
                self.questionTxt = \
                    [self.tr('Limited files per request'),
                     self.tr('At the moment requests are limited to 100 files '
                             'per data type. Limitation will be removed in a '
                             'future release.')]
        else:
            status = self.tr('No files found.')
            self.guiQuestionBtn.show()
            self.questionTxt = \
                [self.tr('Why are there no files?'),
                 self.tr("Not all datasets cover the whole area of Switzerland."
                         " Try changing options or select 'Full dataset extent'"
                         " to get more files.")]

        self.guiFileListStatus.setText(status)
    
    def onDownloadFilesClicked(self):
        # Let user choose output directory
        if self.outputPath:
            openDir = self.outputPath
        else:
            openDir = os.path.expanduser('~')
        folder = QFileDialog.getExistingDirectory(self,
                    self.tr('Choose output folder'), openDir, QFileDialog.ShowDirsOnly)
        if not folder:
            return
            
        # Save path for later
        self.outputPath = folder
        # Check if there are files that are going to be overwritten
        waitForConfirm = False
        # Sort out all selected files from list
        self.filesListDownload = [file for file in self.fileListFiltered.values()
                                    if file['selected']]
        
        for file in self.filesListDownload:
            savePath = os.path.join(folder, file['id'])
            if os.path.exists(savePath):
                waitForConfirm = True
                break
        
        if waitForConfirm:
            confirmed = self.showDialog(self.tr('Overwrite files?'),
                self.tr('At least one file will be overwritten. Continue?'))
            if not confirmed:
                return
        
        # Save full path
        for file in self.filesListDownload:
            file['path'] = os.path.join(folder, file['id'])

        # Call api
        # Create separate task for request to not block ui
        caller = ApiCallerTask(self.apiDGA, self.msgBar, 'downloadFiles', {
            'fileList': self.filesListDownload,
            'folder': folder,
        })
        # Listen for finished api call
        caller.taskCompleted.connect(
            lambda: self.onFinishDownload(caller.output))
        caller.taskTerminated.connect(
            lambda: self.onFinishDownload(False))
        # Start spinner to indicate data loading
        self.spinnerFl.start()
        # Add task to task manager
        QgsApplication.taskManager().addTask(caller)
    
    def onFinishDownload(self, success):
        if success:
            # Confirm successful download
            self.guiFileListStatus.setText(self.tr('Files successfully downloaded!'))
            self.guiFileListStatus.setStyleSheet('QLabel { color : green; font-weight: bold;}')
            self.fileListTbl.clear()

        self.spinnerFl.stop()
        
        # Add file as layers to qgis
        addToQgis(self.filesListDownload)
    
    @staticmethod
    def showDialog(title, msg, mode='OkCancel'):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setWindowTitle(title)
        msgBox.setText(msg)
        if mode == 'OkCancel':
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        elif mode == 'YesNo':
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        elif mode == 'error':
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
        elif mode == 'Ok':
            msgBox.setStandardButtons(QMessageBox.Ok)
        else:
            msgBox.setStandardButtons(QMessageBox.Ok)
            
        returnValue = msgBox.exec()
        return returnValue == QMessageBox.Ok or returnValue == QMessageBox.Yes
