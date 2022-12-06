from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5.uic import loadUi
from PyQt5 import QtGui, QtWidgets
import sys
import sqlite3
from PyQt5.QtWidgets import QCheckBox, QPushButton
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore
import icon


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("menu.ui", self)
        self.even_buttons()
        self.event_func()

    def even_buttons(self):
        self.btnMenu.clicked.connect(self.expandir)
        self.btnHome.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))

        self.btnModule.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.pushButton_13.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))

        self.btnprofessor.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.pushButton_14.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))

        self.btnStudent.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4))
        self.pushButton_12.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4))

        self.btnSalle.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_5))
        self.pushButton_11.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_5))

        self.btnSetting.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_6))
        self.btnTable.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_7))
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_7))

        self.btnExit.clicked.connect(lambda: self.close())


    def expandir(self):
        width = self.menulzquerdo.width()
        if width == 50:
            new_width = 180
            self.btnMenu.setIcon(QtGui.QIcon(":/icons/icons/left.png"))
        elif width == 180:
            new_width = 50
            self.btnMenu.setIcon(QtGui.QIcon(":/icons/icons/menu_bl.png"))

        try:
            self.animation = QPropertyAnimation(self.menulzquerdo, b"minimumWidth")
            self.animation.setStartValue(width)
            self.animation.setEndValue(new_width)
            self.animation.setDuration(350)
            self.animation.setEasingCurve(QEasingCurve.InOutCirc)
            self.animation.start()
        except:
            self.btnMenu.setIcon(QtGui.QIcon(":/icons/icons/menu_bl.png"))
            self.animation.setStartValue(50)
            self.animation.setEndValue(50)
            self.animation.setDuration(350)
            self.animation.setEasingCurve(QEasingCurve.InOutCirc)
            self.animation.start()

    def event_func(self):
        from func import Func
        f = Func(self)

        self.btnSaved.clicked.connect(lambda: f.save_settings())
        self.pushButton_34.clicked.connect(lambda: f.show_modules())
        self.pushButton_29.clicked.connect(lambda: f.add_prof())
        self.pushButton_31.clicked.connect(lambda: f.show_profs())
        self.pushButton_33.clicked.connect(lambda: f.search_prof())
        self.pushButton_30.clicked.connect(lambda: f.delete_prof())

        self.pushButton_20.clicked.connect(lambda: f.add_class())
        self.pushButton_21.clicked.connect(lambda: f.show_classes())
        self.pushButton_19.clicked.connect(lambda: f.search_class())
        self.pushButton_23.clicked.connect(lambda: f.delete_class())

        self.pushButton_24.clicked.connect(lambda: f.add_group())
        self.pushButton_26.clicked.connect(lambda: f.search_group())
        self.pushButton_25.clicked.connect(lambda: f.delete_group())
        self.pushButton_28.clicked.connect(lambda: f.search_group())

        self.pushButton_35.clicked.connect(lambda: f.add_Module())
        self.pushButton_39.clicked.connect(lambda: f.search_Module())
        self.pushButton_36.clicked.connect(lambda: f.delete_module())
        self.pushButton_37.clicked.connect(lambda: f.getProfs_Groups())

        f.getProfs_Groups()




if __name__ == '__main__':
    window = QApplication(sys.argv)
    gui = Main()
    gui.show()
    window.exec_()