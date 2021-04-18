# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'swissgeodatadownloader_dockwidget_base.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SwissGeodataDownloaderDockWidgetBase(object):
    def setupUi(self, SwissGeodataDownloaderDockWidgetBase):
        SwissGeodataDownloaderDockWidgetBase.setObjectName("SwissGeodataDownloaderDockWidgetBase")
        SwissGeodataDownloaderDockWidgetBase.resize(390, 646)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.guiGroupSearch = QtWidgets.QGroupBox(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.guiGroupSearch.setFont(font)
        self.guiGroupSearch.setObjectName("guiGroupSearch")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.guiGroupSearch)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.guiSearchField = QtWidgets.QLineEdit(self.guiGroupSearch)
        self.guiSearchField.setObjectName("guiSearchField")
        self.verticalLayout_3.addWidget(self.guiSearchField)
        self.guiDatasetList = QtWidgets.QListWidget(self.guiGroupSearch)
        self.guiDatasetList.setAlternatingRowColors(False)
        self.guiDatasetList.setObjectName("guiDatasetList")
        self.verticalLayout_3.addWidget(self.guiDatasetList)
        self.verticalLayout.addWidget(self.guiGroupSearch)
        self.guiGroupOptions = QtWidgets.QGroupBox(self.dockWidgetContents)
        self.guiGroupOptions.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.guiGroupOptions.setFont(font)
        self.guiGroupOptions.setFlat(False)
        self.guiGroupOptions.setCheckable(False)
        self.guiGroupOptions.setObjectName("guiGroupOptions")
        self.formLayout = QtWidgets.QFormLayout(self.guiGroupOptions)
        self.formLayout.setObjectName("formLayout")
        self.guiFormatL = QtWidgets.QLabel(self.guiGroupOptions)
        self.guiFormatL.setObjectName("guiFormatL")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.guiFormatL)
        self.guiFormat = QtWidgets.QComboBox(self.guiGroupOptions)
        self.guiFormat.setObjectName("guiFormat")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.guiFormat)
        self.guiResolutionL = QtWidgets.QLabel(self.guiGroupOptions)
        self.guiResolutionL.setObjectName("guiResolutionL")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.guiResolutionL)
        self.guiResolution = QtWidgets.QComboBox(self.guiGroupOptions)
        self.guiResolution.setObjectName("guiResolution")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.guiResolution)
        self.guiCoordsysL = QtWidgets.QLabel(self.guiGroupOptions)
        self.guiCoordsysL.setObjectName("guiCoordsysL")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.guiCoordsysL)
        self.guiCoordsys = QtWidgets.QComboBox(self.guiGroupOptions)
        self.guiCoordsys.setObjectName("guiCoordsys")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.guiCoordsys)
        self.guiTimestampL = QtWidgets.QLabel(self.guiGroupOptions)
        self.guiTimestampL.setObjectName("guiTimestampL")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.guiTimestampL)
        self.guiTimestamp = QtWidgets.QComboBox(self.guiGroupOptions)
        self.guiTimestamp.setObjectName("guiTimestamp")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.guiTimestamp)
        self.verticalLayout.addWidget(self.guiGroupOptions)
        self.guiGroupExtent = QtWidgets.QGroupBox(self.dockWidgetContents)
        self.guiGroupExtent.setObjectName("guiGroupExtent")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.guiGroupExtent)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.guiGroupExtent)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.guiSelectMode = QtWidgets.QComboBox(self.guiGroupExtent)
        self.guiSelectMode.setObjectName("guiSelectMode")
        self.horizontalLayout_2.addWidget(self.guiSelectMode)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.guiExtentWest = QtWidgets.QLineEdit(self.guiGroupExtent)
        self.guiExtentWest.setObjectName("guiExtentWest")
        self.gridLayout_3.addWidget(self.guiExtentWest, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.guiGroupExtent)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.guiExtentSouth = QtWidgets.QLineEdit(self.guiGroupExtent)
        self.guiExtentSouth.setObjectName("guiExtentSouth")
        self.gridLayout_3.addWidget(self.guiExtentSouth, 0, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.guiGroupExtent)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.guiGroupExtent)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)
        self.guiExtentEast = QtWidgets.QLineEdit(self.guiGroupExtent)
        self.guiExtentEast.setObjectName("guiExtentEast")
        self.gridLayout_3.addWidget(self.guiExtentEast, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.guiGroupExtent)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 1, 2, 1, 1)
        self.guiExtentNorth = QtWidgets.QLineEdit(self.guiGroupExtent)
        self.guiExtentNorth.setObjectName("guiExtentNorth")
        self.gridLayout_3.addWidget(self.guiExtentNorth, 1, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.verticalLayout.addWidget(self.guiGroupExtent)
        self.guiGroupFiles = QtWidgets.QGroupBox(self.dockWidgetContents)
        self.guiGroupFiles.setObjectName("guiGroupFiles")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.guiGroupFiles)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.guiFileListStatus = QtWidgets.QLabel(self.guiGroupFiles)
        self.guiFileListStatus.setText("")
        self.guiFileListStatus.setObjectName("guiFileListStatus")
        self.horizontalLayout_3.addWidget(self.guiFileListStatus)
        self.verticalLayout.addWidget(self.guiGroupFiles)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.guiDownloadBtn = QtWidgets.QPushButton(self.dockWidgetContents)
        self.guiDownloadBtn.setObjectName("guiDownloadBtn")
        self.horizontalLayout.addWidget(self.guiDownloadBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
        SwissGeodataDownloaderDockWidgetBase.setWidget(self.dockWidgetContents)

        self.retranslateUi(SwissGeodataDownloaderDockWidgetBase)
        QtCore.QMetaObject.connectSlotsByName(SwissGeodataDownloaderDockWidgetBase)

    def retranslateUi(self, SwissGeodataDownloaderDockWidgetBase):
        _translate = QtCore.QCoreApplication.translate
        SwissGeodataDownloaderDockWidgetBase.setWindowTitle(_translate("SwissGeodataDownloaderDockWidgetBase", "swiss geodata downloader"))
        self.guiGroupSearch.setTitle(_translate("SwissGeodataDownloaderDockWidgetBase", "1. Dataset"))
        self.guiSearchField.setPlaceholderText(_translate("SwissGeodataDownloaderDockWidgetBase", "Search for dataset..."))
        self.guiGroupOptions.setTitle(_translate("SwissGeodataDownloaderDockWidgetBase", "2. Options"))
        self.guiFormatL.setText(_translate("SwissGeodataDownloaderDockWidgetBase", "Format"))
        self.guiResolutionL.setText(_translate("SwissGeodataDownloaderDockWidgetBase", "Resolution [m]"))
        self.guiCoordsysL.setText(_translate("SwissGeodataDownloaderDockWidgetBase", "Coord.sys"))
        self.guiTimestampL.setText(_translate("SwissGeodataDownloaderDockWidgetBase", "Timestamp"))
        self.guiGroupExtent.setTitle(_translate("SwissGeodataDownloaderDockWidgetBase", "3. Extent"))
        self.label_6.setText(_translate("SwissGeodataDownloaderDockWidgetBase", "Select mode"))
        self.label_5.setText(_translate("SwissGeodataDownloaderDockWidgetBase", "West"))
        self.label_8.setText(_translate("SwissGeodataDownloaderDockWidgetBase", "South"))
        self.label_7.setText(_translate("SwissGeodataDownloaderDockWidgetBase", "East"))
        self.label_9.setText(_translate("SwissGeodataDownloaderDockWidgetBase", "North"))
        self.guiGroupFiles.setTitle(_translate("SwissGeodataDownloaderDockWidgetBase", "4. Files"))
        self.guiDownloadBtn.setText(_translate("SwissGeodataDownloaderDockWidgetBase", "Download"))