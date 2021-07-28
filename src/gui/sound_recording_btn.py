# coding: utf8

__contact__ = "info@hytech-imaging.fr"
__copyright__ = "Copyright (c) 2021 Hytech Imaging"

from qgis.PyQt.QtWidgets import QPushButton, QToolBar
from qgis.PyQt.QtCore import pyqtSignal, QObject


class SammoSoundRecordingBtn(QObject):
    onChangeSoundRecordingStatusSignal = pyqtSignal(bool)

    def __init__(self, parent: QObject, toolBar: QToolBar):
        super().__init__()
        self.parent = parent
        self.button: QPushButton = None
        self.initGui(parent, toolBar)

    def initGui(self, parent: QObject, toolBar: QToolBar):
        self.button = QPushButton(parent)
        self.button.setText("Sound recording")
        self.button.clicked.connect(self.onClick)
        self.button.setEnabled(False)
        self.button.setCheckable(True)
        toolBar.addWidget(self.button)

    def onStartEffort(self):
        self.button.setEnabled(True)

    def onStopEffort(self):
        self.button.setChecked(False)
        self.button.setEnabled(False)

    def onStartObservation(self):
        if not self.button.isChecked():
            self.onClick()

    def unload(self):
        del self.button

    def onClick(self):
        if self.button.isChecked():
            self.onChangeSoundRecordingStatusSignal.emit(True)
        else:
            self.onChangeSoundRecordingStatusSignal.emit(False)
