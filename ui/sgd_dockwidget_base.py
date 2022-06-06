# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/sgd_dockwidget_base.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sgdDockWidgetBase(object):
    def setupUi(self, sgdDockWidgetBase):
        sgdDockWidgetBase.setObjectName("sgdDockWidgetBase")
        sgdDockWidgetBase.resize(513, 807)
        sgdDockWidgetBase.setMinimumSize(QtCore.QSize(500, 180))
        font = QtGui.QFont()
        font.setPointSize(13)
        sgdDockWidgetBase.setFont(font)
        sgdDockWidgetBase.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.guiShowMapBtn = QtWidgets.QPushButton(self.dockWidgetContents)
        self.guiShowMapBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/plugins/swissgeodownloader/resources/switzerland.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.guiShowMapBtn.setIcon(icon)
        self.guiShowMapBtn.setFlat(False)
        self.guiShowMapBtn.setObjectName("guiShowMapBtn")
        self.horizontalLayout_4.addWidget(self.guiShowMapBtn)
        self.guiRefreshDatasetsBtn = QtWidgets.QPushButton(self.dockWidgetContents)
        self.guiRefreshDatasetsBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/plugins/swissgeodownloader/resources/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.guiRefreshDatasetsBtn.setIcon(icon1)
        self.guiRefreshDatasetsBtn.setObjectName("guiRefreshDatasetsBtn")
        self.horizontalLayout_4.addWidget(self.guiRefreshDatasetsBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.guiInfoBtn = QtWidgets.QPushButton(self.dockWidgetContents)
        self.guiInfoBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/plugins/swissgeodownloader/resources/die-info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.guiInfoBtn.setIcon(icon2)
        self.guiInfoBtn.setFlat(False)
        self.guiInfoBtn.setObjectName("guiInfoBtn")
        self.horizontalLayout_4.addWidget(self.guiInfoBtn)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.guiFileListStatus = QtWidgets.QLabel(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.guiFileListStatus.sizePolicy().hasHeightForWidth())
        self.guiFileListStatus.setSizePolicy(sizePolicy)
        self.guiFileListStatus.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.guiFileListStatus.setText("")
        self.guiFileListStatus.setWordWrap(True)
        self.guiFileListStatus.setObjectName("guiFileListStatus")
        self.horizontalLayout.addWidget(self.guiFileListStatus)
        spacerItem1 = QtWidgets.QSpacerItem(1, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.guiDownloadBtn = QtWidgets.QPushButton(self.dockWidgetContents)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/plugins/swissgeodownloader/resources/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.guiDownloadBtn.setIcon(icon3)
        self.guiDownloadBtn.setObjectName("guiDownloadBtn")
        self.horizontalLayout.addWidget(self.guiDownloadBtn)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(200, 0))
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 493, 697))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.guiGroupDataset = gui.QgsCollapsibleGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.guiGroupDataset.sizePolicy().hasHeightForWidth())
        self.guiGroupDataset.setSizePolicy(sizePolicy)
        self.guiGroupDataset.setMinimumSize(QtCore.QSize(0, 0))
        self.guiGroupDataset.setObjectName("guiGroupDataset")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.guiGroupDataset)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.guiDatasets = QtWidgets.QVBoxLayout()
        self.guiDatasets.setObjectName("guiDatasets")
        self.verticalLayout_2.addLayout(self.guiDatasets)
        self.verticalLayout.addWidget(self.guiGroupDataset)
        self.guiGroupExtent = gui.QgsCollapsibleGroupBox(self.scrollAreaWidgetContents)
        self.guiGroupExtent.setObjectName("guiGroupExtent")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.guiGroupExtent)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.guiFullExtentChbox = QtWidgets.QCheckBox(self.guiGroupExtent)
        self.guiFullExtentChbox.setMaximumSize(QtCore.QSize(16777215, 14))
        self.guiFullExtentChbox.setObjectName("guiFullExtentChbox")
        self.horizontalLayout_2.addWidget(self.guiFullExtentChbox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.guiExtentWidget = gui.QgsExtentGroupBox(self.guiGroupExtent)
        self.guiExtentWidget.setTitleBase("")
        self.guiExtentWidget.setObjectName("guiExtentWidget")
        self.verticalLayout_6.addWidget(self.guiExtentWidget)
        self.verticalLayout.addWidget(self.guiGroupExtent)
        self.guiGroupFiles = gui.QgsCollapsibleGroupBox(self.scrollAreaWidgetContents)
        self.guiGroupFiles.setObjectName("guiGroupFiles")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.guiGroupFiles)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.guiRequestListBtn = QtWidgets.QPushButton(self.guiGroupFiles)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/plugins/swissgeodownloader/resources/sort-down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.guiRequestListBtn.setIcon(icon4)
        self.guiRequestListBtn.setObjectName("guiRequestListBtn")
        self.horizontalLayout_3.addWidget(self.guiRequestListBtn)
        self.guiRequestCancelBtn = QtWidgets.QPushButton(self.guiGroupFiles)
        icon = QtGui.QIcon.fromTheme("cancel")
        self.guiRequestCancelBtn.setIcon(icon)
        self.guiRequestCancelBtn.setObjectName("guiRequestCancelBtn")
        self.horizontalLayout_3.addWidget(self.guiRequestCancelBtn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.guiFileType = QtWidgets.QComboBox(self.guiGroupFiles)
        self.guiFileType.setObjectName("guiFileType")
        self.gridLayout_3.addWidget(self.guiFileType, 0, 1, 1, 1)
        self.guiResolution = QtWidgets.QComboBox(self.guiGroupFiles)
        self.guiResolution.setObjectName("guiResolution")
        self.gridLayout_3.addWidget(self.guiResolution, 2, 1, 1, 1)
        self.guiFormatL = QtWidgets.QLabel(self.guiGroupFiles)
        self.guiFormatL.setObjectName("guiFormatL")
        self.gridLayout_3.addWidget(self.guiFormatL, 1, 0, 1, 1)
        self.guiResolutionL = QtWidgets.QLabel(self.guiGroupFiles)
        self.guiResolutionL.setObjectName("guiResolutionL")
        self.gridLayout_3.addWidget(self.guiResolutionL, 2, 0, 1, 1)
        self.guiFormat = QtWidgets.QComboBox(self.guiGroupFiles)
        self.guiFormat.setObjectName("guiFormat")
        self.gridLayout_3.addWidget(self.guiFormat, 1, 1, 1, 1)
        self.guiTimestampL = QtWidgets.QLabel(self.guiGroupFiles)
        self.guiTimestampL.setObjectName("guiTimestampL")
        self.gridLayout_3.addWidget(self.guiTimestampL, 3, 0, 1, 1)
        self.guiTimestamp = QtWidgets.QComboBox(self.guiGroupFiles)
        self.guiTimestamp.setObjectName("guiTimestamp")
        self.gridLayout_3.addWidget(self.guiTimestamp, 3, 1, 1, 1)
        self.guiCoordsysL = QtWidgets.QLabel(self.guiGroupFiles)
        self.guiCoordsysL.setObjectName("guiCoordsysL")
        self.gridLayout_3.addWidget(self.guiCoordsysL, 4, 0, 1, 1)
        self.guiCoordsys = QtWidgets.QComboBox(self.guiGroupFiles)
        self.guiCoordsys.setObjectName("guiCoordsys")
        self.gridLayout_3.addWidget(self.guiCoordsys, 4, 1, 1, 1)
        self.guiFileTypeL = QtWidgets.QLabel(self.guiGroupFiles)
        self.guiFileTypeL.setObjectName("guiFileTypeL")
        self.gridLayout_3.addWidget(self.guiFileTypeL, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.guiFileListLayout = QtWidgets.QVBoxLayout()
        self.guiFileListLayout.setObjectName("guiFileListLayout")
        self.verticalLayout_3.addLayout(self.guiFileListLayout)
        self.verticalLayout.addWidget(self.guiGroupFiles)
        spacerItem4 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 2, 0, 1, 1)
        sgdDockWidgetBase.setWidget(self.dockWidgetContents)

        self.retranslateUi(sgdDockWidgetBase)
        QtCore.QMetaObject.connectSlotsByName(sgdDockWidgetBase)
        sgdDockWidgetBase.setTabOrder(self.guiShowMapBtn, self.guiRefreshDatasetsBtn)
        sgdDockWidgetBase.setTabOrder(self.guiRefreshDatasetsBtn, self.guiInfoBtn)
        sgdDockWidgetBase.setTabOrder(self.guiInfoBtn, self.scrollArea)
        sgdDockWidgetBase.setTabOrder(self.scrollArea, self.guiGroupDataset)
        sgdDockWidgetBase.setTabOrder(self.guiGroupDataset, self.guiGroupExtent)
        sgdDockWidgetBase.setTabOrder(self.guiGroupExtent, self.guiFullExtentChbox)
        sgdDockWidgetBase.setTabOrder(self.guiFullExtentChbox, self.guiExtentWidget)
        sgdDockWidgetBase.setTabOrder(self.guiExtentWidget, self.guiGroupFiles)
        sgdDockWidgetBase.setTabOrder(self.guiGroupFiles, self.guiRequestListBtn)
        sgdDockWidgetBase.setTabOrder(self.guiRequestListBtn, self.guiRequestCancelBtn)
        sgdDockWidgetBase.setTabOrder(self.guiRequestCancelBtn, self.guiFileType)
        sgdDockWidgetBase.setTabOrder(self.guiFileType, self.guiFormat)
        sgdDockWidgetBase.setTabOrder(self.guiFormat, self.guiResolution)
        sgdDockWidgetBase.setTabOrder(self.guiResolution, self.guiTimestamp)
        sgdDockWidgetBase.setTabOrder(self.guiTimestamp, self.guiCoordsys)
        sgdDockWidgetBase.setTabOrder(self.guiCoordsys, self.guiDownloadBtn)

    def retranslateUi(self, sgdDockWidgetBase):
        _translate = QtCore.QCoreApplication.translate
        sgdDockWidgetBase.setWindowTitle(_translate("sgdDockWidgetBase", "Swiss Geo Downloader"))
        self.guiShowMapBtn.setToolTip(_translate("sgdDockWidgetBase", "Show overview map"))
        self.guiRefreshDatasetsBtn.setToolTip(_translate("sgdDockWidgetBase", "Refresh dataset list"))
        self.guiInfoBtn.setToolTip(_translate("sgdDockWidgetBase", "Plugin info"))
        self.guiDownloadBtn.setToolTip(_translate("sgdDockWidgetBase", "Download list of files"))
        self.guiDownloadBtn.setText(_translate("sgdDockWidgetBase", "Download"))
        self.guiGroupDataset.setTitle(_translate("sgdDockWidgetBase", "1. Dataset"))
        self.guiGroupExtent.setTitle(_translate("sgdDockWidgetBase", "2. Extent"))
        self.guiFullExtentChbox.setText(_translate("sgdDockWidgetBase", "Full dataset extent"))
        self.guiGroupFiles.setTitle(_translate("sgdDockWidgetBase", "3. Files"))
        self.guiRequestListBtn.setToolTip(_translate("sgdDockWidgetBase", "Requests are limited to max. 100 files"))
        self.guiRequestListBtn.setText(_translate("sgdDockWidgetBase", "Request file list"))
        self.guiRequestCancelBtn.setText(_translate("sgdDockWidgetBase", "Cancel request"))
        self.guiFileType.setToolTip(_translate("sgdDockWidgetBase", "Filter file list by type"))
        self.guiResolution.setToolTip(_translate("sgdDockWidgetBase", "Select resolution (only raster based datasets)"))
        self.guiFormatL.setText(_translate("sgdDockWidgetBase", "Format"))
        self.guiResolutionL.setText(_translate("sgdDockWidgetBase", "Resolution [m]"))
        self.guiFormat.setToolTip(_translate("sgdDockWidgetBase", "Select format"))
        self.guiTimestampL.setText(_translate("sgdDockWidgetBase", "Timestamp"))
        self.guiTimestamp.setToolTip(_translate("sgdDockWidgetBase", "Select timestamp"))
        self.guiCoordsysL.setText(_translate("sgdDockWidgetBase", "Coord.sys"))
        self.guiCoordsys.setToolTip(_translate("sgdDockWidgetBase", "Select coordinate reference system"))
        self.guiFileTypeL.setText(_translate("sgdDockWidgetBase", "File type"))
from qgis import gui
from ..resources import resources
