from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QLabel
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtCore
import sqlite3


class Checked(QWidget):
    def __init__(self, module):
        super(Checked, self).__init__()
        loadUi("check_classes.ui", self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.checkBox.setText(module)
        self.checkBox.setStyleSheet("border:none;")

    def isCheck(self):
        if self.checkBox.isChecked():
            return True

    def get_module(self):
        if self.isCheck():
            return self.checkBox.text()



