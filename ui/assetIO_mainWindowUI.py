# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ozgur/maya/scripts/oy-maya-scripts/oyTools/oyProjectManager/ui/assetIO_mainWindow.ui'
#
# Created: Tue Oct  6 12:50:42 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(398, 604)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_verticalWidget = QtGui.QWidget(self.centralwidget)
        self.main_verticalWidget.setObjectName("main_verticalWidget")
        self.main_verticalLayout = QtGui.QVBoxLayout(self.main_verticalWidget)
        self.main_verticalLayout.setObjectName("main_verticalLayout")
        self.main_gridLayout = QtGui.QGridLayout()
        self.main_gridLayout.setObjectName("main_gridLayout")
        self.server_label = QtGui.QLabel(self.main_verticalWidget)
        self.server_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.server_label.setObjectName("server_label")
        self.main_gridLayout.addWidget(self.server_label, 0, 0, 1, 1)
        self.server_comboBox = QtGui.QComboBox(self.main_verticalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.server_comboBox.sizePolicy().hasHeightForWidth())
        self.server_comboBox.setSizePolicy(sizePolicy)
        self.server_comboBox.setEditable(False)
        self.server_comboBox.setObjectName("server_comboBox")
        self.main_gridLayout.addWidget(self.server_comboBox, 0, 1, 1, 1)
        self.project_label = QtGui.QLabel(self.main_verticalWidget)
        self.project_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.project_label.setObjectName("project_label")
        self.main_gridLayout.addWidget(self.project_label, 1, 0, 1, 1)
        self.project_comboBox = QtGui.QComboBox(self.main_verticalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.project_comboBox.sizePolicy().hasHeightForWidth())
        self.project_comboBox.setSizePolicy(sizePolicy)
        self.project_comboBox.setEditable(False)
        self.project_comboBox.setObjectName("project_comboBox")
        self.main_gridLayout.addWidget(self.project_comboBox, 1, 1, 1, 1)
        self.sequence_label = QtGui.QLabel(self.main_verticalWidget)
        self.sequence_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sequence_label.setObjectName("sequence_label")
        self.main_gridLayout.addWidget(self.sequence_label, 2, 0, 1, 1)
        self.sequence_comboBox = QtGui.QComboBox(self.main_verticalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sequence_comboBox.sizePolicy().hasHeightForWidth())
        self.sequence_comboBox.setSizePolicy(sizePolicy)
        self.sequence_comboBox.setEditable(False)
        self.sequence_comboBox.setObjectName("sequence_comboBox")
        self.main_gridLayout.addWidget(self.sequence_comboBox, 2, 1, 1, 1)
        self.main_verticalLayout.addLayout(self.main_gridLayout)
        self.main_tabWidget = QtGui.QTabWidget(self.main_verticalWidget)
        self.main_tabWidget.setEnabled(True)
        self.main_tabWidget.setObjectName("main_tabWidget")
        self.saveAsset_tab = QtGui.QWidget()
        self.saveAsset_tab.setEnabled(True)
        self.saveAsset_tab.setObjectName("saveAsset_tab")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.saveAsset_tab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.saveAsest_verticalWidget = QtGui.QWidget(self.saveAsset_tab)
        self.saveAsest_verticalWidget.setObjectName("saveAsest_verticalWidget")
        self.saveAsset_verticalLayout = QtGui.QVBoxLayout(self.saveAsest_verticalWidget)
        self.saveAsset_verticalLayout.setObjectName("saveAsset_verticalLayout")
        self.saveAsset_gridWidget = QtGui.QWidget(self.saveAsest_verticalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveAsset_gridWidget.sizePolicy().hasHeightForWidth())
        self.saveAsset_gridWidget.setSizePolicy(sizePolicy)
        self.saveAsset_gridWidget.setObjectName("saveAsset_gridWidget")
        self.saveAsset_gridLayout = QtGui.QGridLayout(self.saveAsset_gridWidget)
        self.saveAsset_gridLayout.setObjectName("saveAsset_gridLayout")
        self.assetType_comboBox1 = QtGui.QComboBox(self.saveAsset_gridWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.assetType_comboBox1.sizePolicy().hasHeightForWidth())
        self.assetType_comboBox1.setSizePolicy(sizePolicy)
        self.assetType_comboBox1.setObjectName("assetType_comboBox1")
        self.saveAsset_gridLayout.addWidget(self.assetType_comboBox1, 0, 1, 1, 1)
        self.note_lineEdit1 = QtGui.QLineEdit(self.saveAsset_gridWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.note_lineEdit1.sizePolicy().hasHeightForWidth())
        self.note_lineEdit1.setSizePolicy(sizePolicy)
        self.note_lineEdit1.setObjectName("note_lineEdit1")
        self.saveAsset_gridLayout.addWidget(self.note_lineEdit1, 7, 1, 1, 1)
        self.version_horizontalLayout = QtGui.QHBoxLayout()
        self.version_horizontalLayout.setObjectName("version_horizontalLayout")
        self.version_spinBox = QtGui.QSpinBox(self.saveAsset_gridWidget)
        self.version_spinBox.setMinimum(1)
        self.version_spinBox.setMaximum(99999999)
        self.version_spinBox.setObjectName("version_spinBox")
        self.version_horizontalLayout.addWidget(self.version_spinBox)
        self.version_pushButton = QtGui.QPushButton(self.saveAsset_gridWidget)
        self.version_pushButton.setObjectName("version_pushButton")
        self.version_horizontalLayout.addWidget(self.version_pushButton)
        self.saveAsset_gridLayout.addLayout(self.version_horizontalLayout, 5, 1, 1, 1)
        self.assetType_label1 = QtGui.QLabel(self.saveAsset_gridWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.assetType_label1.sizePolicy().hasHeightForWidth())
        self.assetType_label1.setSizePolicy(sizePolicy)
        self.assetType_label1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.assetType_label1.setObjectName("assetType_label1")
        self.saveAsset_gridLayout.addWidget(self.assetType_label1, 0, 0, 1, 1)
        self.baseName_label1 = QtGui.QLabel(self.saveAsset_gridWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.baseName_label1.sizePolicy().hasHeightForWidth())
        self.baseName_label1.setSizePolicy(sizePolicy)
        self.baseName_label1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.baseName_label1.setObjectName("baseName_label1")
        self.saveAsset_gridLayout.addWidget(self.baseName_label1, 2, 0, 1, 1)
        self.subName_comboBox1 = QtGui.QComboBox(self.saveAsset_gridWidget)
        self.subName_comboBox1.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.subName_comboBox1.sizePolicy().hasHeightForWidth())
        self.subName_comboBox1.setSizePolicy(sizePolicy)
        self.subName_comboBox1.setEditable(True)
        self.subName_comboBox1.setObjectName("subName_comboBox1")
        self.saveAsset_gridLayout.addWidget(self.subName_comboBox1, 3, 1, 1, 1)
        self.shot_comboBox1 = QtGui.QComboBox(self.saveAsset_gridWidget)
        self.shot_comboBox1.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.shot_comboBox1.sizePolicy().hasHeightForWidth())
        self.shot_comboBox1.setSizePolicy(sizePolicy)
        self.shot_comboBox1.setObjectName("shot_comboBox1")
        self.saveAsset_gridLayout.addWidget(self.shot_comboBox1, 1, 1, 1, 1)
        self.user_comboBox1 = QtGui.QComboBox(self.saveAsset_gridWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.user_comboBox1.sizePolicy().hasHeightForWidth())
        self.user_comboBox1.setSizePolicy(sizePolicy)
        self.user_comboBox1.setObjectName("user_comboBox1")
        self.saveAsset_gridLayout.addWidget(self.user_comboBox1, 6, 1, 1, 1)
        self.user_label1 = QtGui.QLabel(self.saveAsset_gridWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.user_label1.sizePolicy().hasHeightForWidth())
        self.user_label1.setSizePolicy(sizePolicy)
        self.user_label1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.user_label1.setObjectName("user_label1")
        self.saveAsset_gridLayout.addWidget(self.user_label1, 6, 0, 1, 1)
        self.subName_label1 = QtGui.QLabel(self.saveAsset_gridWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.subName_label1.sizePolicy().hasHeightForWidth())
        self.subName_label1.setSizePolicy(sizePolicy)
        self.subName_label1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.subName_label1.setObjectName("subName_label1")
        self.saveAsset_gridLayout.addWidget(self.subName_label1, 3, 0, 1, 1)
        self.baseName_comboBox1 = QtGui.QComboBox(self.saveAsset_gridWidget)
        self.baseName_comboBox1.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.baseName_comboBox1.sizePolicy().hasHeightForWidth())
        self.baseName_comboBox1.setSizePolicy(sizePolicy)
        self.baseName_comboBox1.setEditable(True)
        self.baseName_comboBox1.setObjectName("baseName_comboBox1")
        self.saveAsset_gridLayout.addWidget(self.baseName_comboBox1, 2, 1, 1, 1)
        self.version_label1 = QtGui.QLabel(self.saveAsset_gridWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.version_label1.sizePolicy().hasHeightForWidth())
        self.version_label1.setSizePolicy(sizePolicy)
        self.version_label1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.version_label1.setObjectName("version_label1")
        self.saveAsset_gridLayout.addWidget(self.version_label1, 5, 0, 1, 1)
        self.shot_label1 = QtGui.QLabel(self.saveAsset_gridWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.shot_label1.sizePolicy().hasHeightForWidth())
        self.shot_label1.setSizePolicy(sizePolicy)
        self.shot_label1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.shot_label1.setObjectName("shot_label1")
        self.saveAsset_gridLayout.addWidget(self.shot_label1, 1, 0, 1, 1)
        self.note_label1 = QtGui.QLabel(self.saveAsset_gridWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.note_label1.sizePolicy().hasHeightForWidth())
        self.note_label1.setSizePolicy(sizePolicy)
        self.note_label1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.note_label1.setObjectName("note_label1")
        self.saveAsset_gridLayout.addWidget(self.note_label1, 7, 0, 1, 1)
        self.revision_label1 = QtGui.QLabel(self.saveAsset_gridWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.revision_label1.sizePolicy().hasHeightForWidth())
        self.revision_label1.setSizePolicy(sizePolicy)
        self.revision_label1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.revision_label1.setObjectName("revision_label1")
        self.saveAsset_gridLayout.addWidget(self.revision_label1, 4, 0, 1, 1)
        self.revision_horizontalLayout = QtGui.QHBoxLayout()
        self.revision_horizontalLayout.setObjectName("revision_horizontalLayout")
        self.revision_spinBox = QtGui.QSpinBox(self.saveAsset_gridWidget)
        self.revision_spinBox.setObjectName("revision_spinBox")
        self.revision_horizontalLayout.addWidget(self.revision_spinBox)
        self.revision_pushButton = QtGui.QPushButton(self.saveAsset_gridWidget)
        self.revision_pushButton.setObjectName("revision_pushButton")
        self.revision_horizontalLayout.addWidget(self.revision_pushButton)
        self.saveAsset_gridLayout.addLayout(self.revision_horizontalLayout, 4, 1, 1, 1)
        self.saveAsset_verticalLayout.addWidget(self.saveAsset_gridWidget)
        self.assets_listWidget1 = QtGui.QListWidget(self.saveAsest_verticalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.assets_listWidget1.sizePolicy().hasHeightForWidth())
        self.assets_listWidget1.setSizePolicy(sizePolicy)
        self.assets_listWidget1.setObjectName("assets_listWidget1")
        self.saveAsset_verticalLayout.addWidget(self.assets_listWidget1)
        self.saveButtons_horizontalWidget = QtGui.QWidget(self.saveAsest_verticalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButtons_horizontalWidget.sizePolicy().hasHeightForWidth())
        self.saveButtons_horizontalWidget.setSizePolicy(sizePolicy)
        self.saveButtons_horizontalWidget.setObjectName("saveButtons_horizontalWidget")
        self.saveCanel_horizontalLayout = QtGui.QHBoxLayout(self.saveButtons_horizontalWidget)
        self.saveCanel_horizontalLayout.setObjectName("saveCanel_horizontalLayout")
        self.save_button = QtGui.QPushButton(self.saveButtons_horizontalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_button.sizePolicy().hasHeightForWidth())
        self.save_button.setSizePolicy(sizePolicy)
        self.save_button.setObjectName("save_button")
        self.saveCanel_horizontalLayout.addWidget(self.save_button)
        self.cancel_button1 = QtGui.QPushButton(self.saveButtons_horizontalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_button1.sizePolicy().hasHeightForWidth())
        self.cancel_button1.setSizePolicy(sizePolicy)
        self.cancel_button1.setObjectName("cancel_button1")
        self.saveCanel_horizontalLayout.addWidget(self.cancel_button1)
        self.saveAsset_verticalLayout.addWidget(self.saveButtons_horizontalWidget)
        self.horizontalLayout_3.addWidget(self.saveAsest_verticalWidget)
        self.main_tabWidget.addTab(self.saveAsset_tab, "")
        self.openAsset_tab = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.openAsset_tab.sizePolicy().hasHeightForWidth())
        self.openAsset_tab.setSizePolicy(sizePolicy)
        self.openAsset_tab.setObjectName("openAsset_tab")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.openAsset_tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.openAsset_verticalWidget = QtGui.QWidget(self.openAsset_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.openAsset_verticalWidget.sizePolicy().hasHeightForWidth())
        self.openAsset_verticalWidget.setSizePolicy(sizePolicy)
        self.openAsset_verticalWidget.setObjectName("openAsset_verticalWidget")
        self.openAsset_verticalLayout = QtGui.QVBoxLayout(self.openAsset_verticalWidget)
        self.openAsset_verticalLayout.setMargin(6)
        self.openAsset_verticalLayout.setObjectName("openAsset_verticalLayout")
        self.openAsset_gridWidget = QtGui.QWidget(self.openAsset_verticalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openAsset_gridWidget.sizePolicy().hasHeightForWidth())
        self.openAsset_gridWidget.setSizePolicy(sizePolicy)
        self.openAsset_gridWidget.setObjectName("openAsset_gridWidget")
        self.openAsset_gridLayout = QtGui.QGridLayout(self.openAsset_gridWidget)
        self.openAsset_gridLayout.setObjectName("openAsset_gridLayout")
        self.assetType_label2 = QtGui.QLabel(self.openAsset_gridWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.assetType_label2.sizePolicy().hasHeightForWidth())
        self.assetType_label2.setSizePolicy(sizePolicy)
        self.assetType_label2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.assetType_label2.setObjectName("assetType_label2")
        self.openAsset_gridLayout.addWidget(self.assetType_label2, 0, 0, 1, 1)
        self.assetType_comboBox2 = QtGui.QComboBox(self.openAsset_gridWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.assetType_comboBox2.sizePolicy().hasHeightForWidth())
        self.assetType_comboBox2.setSizePolicy(sizePolicy)
        self.assetType_comboBox2.setObjectName("assetType_comboBox2")
        self.openAsset_gridLayout.addWidget(self.assetType_comboBox2, 0, 1, 1, 1)
        self.shot_label2 = QtGui.QLabel(self.openAsset_gridWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.shot_label2.sizePolicy().hasHeightForWidth())
        self.shot_label2.setSizePolicy(sizePolicy)
        self.shot_label2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.shot_label2.setObjectName("shot_label2")
        self.openAsset_gridLayout.addWidget(self.shot_label2, 1, 0, 1, 1)
        self.shot_comboBox2 = QtGui.QComboBox(self.openAsset_gridWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.shot_comboBox2.sizePolicy().hasHeightForWidth())
        self.shot_comboBox2.setSizePolicy(sizePolicy)
        self.shot_comboBox2.setObjectName("shot_comboBox2")
        self.openAsset_gridLayout.addWidget(self.shot_comboBox2, 1, 1, 1, 1)
        self.baseName_label2 = QtGui.QLabel(self.openAsset_gridWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.baseName_label2.sizePolicy().hasHeightForWidth())
        self.baseName_label2.setSizePolicy(sizePolicy)
        self.baseName_label2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.baseName_label2.setObjectName("baseName_label2")
        self.openAsset_gridLayout.addWidget(self.baseName_label2, 2, 0, 1, 1)
        self.subName_label2 = QtGui.QLabel(self.openAsset_gridWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.subName_label2.sizePolicy().hasHeightForWidth())
        self.subName_label2.setSizePolicy(sizePolicy)
        self.subName_label2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.subName_label2.setObjectName("subName_label2")
        self.openAsset_gridLayout.addWidget(self.subName_label2, 3, 0, 1, 1)
        self.subName_comboBox2 = QtGui.QComboBox(self.openAsset_gridWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.subName_comboBox2.sizePolicy().hasHeightForWidth())
        self.subName_comboBox2.setSizePolicy(sizePolicy)
        self.subName_comboBox2.setObjectName("subName_comboBox2")
        self.openAsset_gridLayout.addWidget(self.subName_comboBox2, 3, 1, 1, 1)
        self.baseName_comboBox2 = QtGui.QComboBox(self.openAsset_gridWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.baseName_comboBox2.sizePolicy().hasHeightForWidth())
        self.baseName_comboBox2.setSizePolicy(sizePolicy)
        self.baseName_comboBox2.setObjectName("baseName_comboBox2")
        self.openAsset_gridLayout.addWidget(self.baseName_comboBox2, 2, 1, 1, 1)
        self.openAsset_verticalLayout.addWidget(self.openAsset_gridWidget)
        self.assets_listWidget2 = QtGui.QListWidget(self.openAsset_verticalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.assets_listWidget2.sizePolicy().hasHeightForWidth())
        self.assets_listWidget2.setSizePolicy(sizePolicy)
        self.assets_listWidget2.setObjectName("assets_listWidget2")
        self.openAsset_verticalLayout.addWidget(self.assets_listWidget2)
        self.openButtons_horizontalWidget = QtGui.QWidget(self.openAsset_verticalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openButtons_horizontalWidget.sizePolicy().hasHeightForWidth())
        self.openButtons_horizontalWidget.setSizePolicy(sizePolicy)
        self.openButtons_horizontalWidget.setObjectName("openButtons_horizontalWidget")
        self.openButtons_horizontalLayout = QtGui.QHBoxLayout(self.openButtons_horizontalWidget)
        self.openButtons_horizontalLayout.setMargin(6)
        self.openButtons_horizontalLayout.setObjectName("openButtons_horizontalLayout")
        self.open_button = QtGui.QPushButton(self.openButtons_horizontalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_button.sizePolicy().hasHeightForWidth())
        self.open_button.setSizePolicy(sizePolicy)
        self.open_button.setObjectName("open_button")
        self.openButtons_horizontalLayout.addWidget(self.open_button)
        self.reference_button = QtGui.QPushButton(self.openButtons_horizontalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reference_button.sizePolicy().hasHeightForWidth())
        self.reference_button.setSizePolicy(sizePolicy)
        self.reference_button.setObjectName("reference_button")
        self.openButtons_horizontalLayout.addWidget(self.reference_button)
        self.import_button = QtGui.QPushButton(self.openButtons_horizontalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.import_button.sizePolicy().hasHeightForWidth())
        self.import_button.setSizePolicy(sizePolicy)
        self.import_button.setObjectName("import_button")
        self.openButtons_horizontalLayout.addWidget(self.import_button)
        self.cancel_button2 = QtGui.QPushButton(self.openButtons_horizontalWidget)
        self.cancel_button2.setObjectName("cancel_button2")
        self.openButtons_horizontalLayout.addWidget(self.cancel_button2)
        self.openAsset_verticalLayout.addWidget(self.openButtons_horizontalWidget)
        self.horizontalLayout_2.addWidget(self.openAsset_verticalWidget)
        self.main_tabWidget.addTab(self.openAsset_tab, "")
        self.main_verticalLayout.addWidget(self.main_tabWidget)
        self.verticalLayout.addWidget(self.main_verticalWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 398, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Settings = QtGui.QAction(MainWindow)
        self.actionOpen_Settings.setObjectName("actionOpen_Settings")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSave_Asset = QtGui.QAction(MainWindow)
        self.actionSave_Asset.setObjectName("actionSave_Asset")
        self.actionSave_Settings = QtGui.QAction(MainWindow)
        self.actionSave_Settings.setObjectName("actionSave_Settings")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen_Settings)
        self.menuFile.addAction(self.actionSave_Asset)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_Settings)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.main_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "asset IO", None, QtGui.QApplication.UnicodeUTF8))
        self.server_label.setText(QtGui.QApplication.translate("MainWindow", "Server", None, QtGui.QApplication.UnicodeUTF8))
        self.server_comboBox.setStatusTip(QtGui.QApplication.translate("MainWindow", "Select a Server", None, QtGui.QApplication.UnicodeUTF8))
        self.project_label.setText(QtGui.QApplication.translate("MainWindow", "Project", None, QtGui.QApplication.UnicodeUTF8))
        self.project_comboBox.setStatusTip(QtGui.QApplication.translate("MainWindow", "Select a Project", None, QtGui.QApplication.UnicodeUTF8))
        self.sequence_label.setText(QtGui.QApplication.translate("MainWindow", "Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.sequence_comboBox.setStatusTip(QtGui.QApplication.translate("MainWindow", "Select a Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.main_tabWidget.setStatusTip(QtGui.QApplication.translate("MainWindow", "select a tab to save or open an asset or to manage a project", None, QtGui.QApplication.UnicodeUTF8))
        self.assetType_comboBox1.setStatusTip(QtGui.QApplication.translate("MainWindow", "Select an asset type", None, QtGui.QApplication.UnicodeUTF8))
        self.note_lineEdit1.setStatusTip(QtGui.QApplication.translate("MainWindow", "it is a limited field, try to keep it brief", None, QtGui.QApplication.UnicodeUTF8))
        self.version_spinBox.setStatusTip(QtGui.QApplication.translate("MainWindow", "it is automatically increased by 1", None, QtGui.QApplication.UnicodeUTF8))
        self.version_pushButton.setStatusTip(QtGui.QApplication.translate("MainWindow", "gets the latest version number", None, QtGui.QApplication.UnicodeUTF8))
        self.version_pushButton.setText(QtGui.QApplication.translate("MainWindow", "Get Latest Version", None, QtGui.QApplication.UnicodeUTF8))
        self.assetType_label1.setText(QtGui.QApplication.translate("MainWindow", "Asset Type", None, QtGui.QApplication.UnicodeUTF8))
        self.baseName_label1.setText(QtGui.QApplication.translate("MainWindow", "Base Name", None, QtGui.QApplication.UnicodeUTF8))
        self.subName_comboBox1.setStatusTip(QtGui.QApplication.translate("MainWindow", "if the project supports SubName field, you can enter or select a subName", None, QtGui.QApplication.UnicodeUTF8))
        self.shot_comboBox1.setStatusTip(QtGui.QApplication.translate("MainWindow", "if the type is a shot dependent type this will be activated", None, QtGui.QApplication.UnicodeUTF8))
        self.user_comboBox1.setStatusTip(QtGui.QApplication.translate("MainWindow", "select your user initials", None, QtGui.QApplication.UnicodeUTF8))
        self.user_label1.setText(QtGui.QApplication.translate("MainWindow", "User", None, QtGui.QApplication.UnicodeUTF8))
        self.subName_label1.setText(QtGui.QApplication.translate("MainWindow", "Sub Name", None, QtGui.QApplication.UnicodeUTF8))
        self.baseName_comboBox1.setStatusTip(QtGui.QApplication.translate("MainWindow", "for shot independent types enter or select a baseName", None, QtGui.QApplication.UnicodeUTF8))
        self.version_label1.setText(QtGui.QApplication.translate("MainWindow", "Version", None, QtGui.QApplication.UnicodeUTF8))
        self.shot_label1.setText(QtGui.QApplication.translate("MainWindow", "Shot", None, QtGui.QApplication.UnicodeUTF8))
        self.note_label1.setText(QtGui.QApplication.translate("MainWindow", "Note", None, QtGui.QApplication.UnicodeUTF8))
        self.revision_label1.setText(QtGui.QApplication.translate("MainWindow", "Revision", None, QtGui.QApplication.UnicodeUTF8))
        self.revision_spinBox.setStatusTip(QtGui.QApplication.translate("MainWindow", "increase it when the asset needs a revision", None, QtGui.QApplication.UnicodeUTF8))
        self.revision_pushButton.setStatusTip(QtGui.QApplication.translate("MainWindow", "gets the latest revision number", None, QtGui.QApplication.UnicodeUTF8))
        self.revision_pushButton.setText(QtGui.QApplication.translate("MainWindow", "Get Lastest Revision", None, QtGui.QApplication.UnicodeUTF8))
        self.save_button.setStatusTip(QtGui.QApplication.translate("MainWindow", "Save asset to the server", None, QtGui.QApplication.UnicodeUTF8))
        self.save_button.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_button1.setStatusTip(QtGui.QApplication.translate("MainWindow", "Quit without doing anything", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_button1.setText(QtGui.QApplication.translate("MainWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.saveAsset_tab), QtGui.QApplication.translate("MainWindow", "Save Asset", None, QtGui.QApplication.UnicodeUTF8))
        self.assetType_label2.setText(QtGui.QApplication.translate("MainWindow", "Asset Type", None, QtGui.QApplication.UnicodeUTF8))
        self.assetType_comboBox2.setStatusTip(QtGui.QApplication.translate("MainWindow", "Select an asset type", None, QtGui.QApplication.UnicodeUTF8))
        self.shot_label2.setText(QtGui.QApplication.translate("MainWindow", "Shot", None, QtGui.QApplication.UnicodeUTF8))
        self.shot_comboBox2.setStatusTip(QtGui.QApplication.translate("MainWindow", "if the type is a shot dependent type this will be activated", None, QtGui.QApplication.UnicodeUTF8))
        self.baseName_label2.setText(QtGui.QApplication.translate("MainWindow", "Base Name", None, QtGui.QApplication.UnicodeUTF8))
        self.subName_label2.setText(QtGui.QApplication.translate("MainWindow", "Sub Name", None, QtGui.QApplication.UnicodeUTF8))
        self.subName_comboBox2.setStatusTip(QtGui.QApplication.translate("MainWindow", "if the project supports SubName field, you can select a subName", None, QtGui.QApplication.UnicodeUTF8))
        self.baseName_comboBox2.setStatusTip(QtGui.QApplication.translate("MainWindow", "for shot independent types select a baseName", None, QtGui.QApplication.UnicodeUTF8))
        self.assets_listWidget2.setStatusTip(QtGui.QApplication.translate("MainWindow", "all the asset for the current settings will be listed here", None, QtGui.QApplication.UnicodeUTF8))
        self.open_button.setStatusTip(QtGui.QApplication.translate("MainWindow", "Open the selected asset", None, QtGui.QApplication.UnicodeUTF8))
        self.open_button.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.reference_button.setStatusTip(QtGui.QApplication.translate("MainWindow", "Reference it tho the current scene (Maya only)", None, QtGui.QApplication.UnicodeUTF8))
        self.reference_button.setText(QtGui.QApplication.translate("MainWindow", "Reference", None, QtGui.QApplication.UnicodeUTF8))
        self.import_button.setStatusTip(QtGui.QApplication.translate("MainWindow", "Import the contents to the current scene", None, QtGui.QApplication.UnicodeUTF8))
        self.import_button.setText(QtGui.QApplication.translate("MainWindow", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_button2.setStatusTip(QtGui.QApplication.translate("MainWindow", "Quit without doing anything", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_button2.setText(QtGui.QApplication.translate("MainWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.openAsset_tab), QtGui.QApplication.translate("MainWindow", "Open Asset", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Settings.setText(QtGui.QApplication.translate("MainWindow", "Open Asset", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About oyProjectManager", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Asset.setText(QtGui.QApplication.translate("MainWindow", "Save Asset", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Settings.setText(QtGui.QApplication.translate("MainWindow", "Save Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))

