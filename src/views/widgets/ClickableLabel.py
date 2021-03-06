from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QLabel
from src.models.SessionWrapper import SessionWrapper


class ClickableLabel(QLabel):
    clicked = pyqtSignal()
    rightClicked = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        bg_color = "#333e44"
        txt_color = "#fff"
        if 'bg_color' in kwargs:
            bg_color = kwargs['bg_color']
        if 'txt_color' in kwargs:
            txt_color = kwargs['txt_color']
        style = """
                       QLabel{
                           color: %s;
                           font-size: %s;
                           margin: 0 10px;
                           background-color: %s;
                       }
                       """ % (txt_color, SessionWrapper.number_to_size[SessionWrapper.regular_size], bg_color)
        self.setStyleSheet(style)
        self.setMaximumHeight(45)
        # self.fixWidth()

    def mousePressEvent(self, ev):
        if ev.button() == Qt.LeftButton:
            self.clicked.emit()
        elif ev.button() == Qt.RightButton:
            self.rightClicked.emit()

    def fixWidth(self):
        length = len(self.text())
        if length > 2:
            self.setFixedWidth(int(length*9.5))


class ActiveLabel(QLabel):
    clicked = pyqtSignal()
    rightClicked = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        if 'bg_color' in kwargs:
            bg_color = kwargs['bg_color']
        else:
            bg_color = "#445566"

        if 'front_color' in kwargs:
            front_color = kwargs['front_color']
        else:
            front_color = "#ffffff"
        style = """
                       QLabel{
                           color: %s;
                           font-size: %s;
                           padding: 10px;
                           background-color: %s;
                       }
                       """ % (front_color, SessionWrapper.number_to_size[SessionWrapper.regular_size], bg_color)
        self.setStyleSheet(style)
        self.setMaximumHeight(45)
        # self.fixWidth()

    def mousePressEvent(self, ev):
        if ev.button() == Qt.LeftButton:
            self.clicked.emit()
        elif ev.button() == Qt.RightButton:
            self.rightClicked.emit()

    def fixWidth(self):
        length = len(self.text())
        if length > 2:
            self.setFixedWidth(int(length*9.5))


class ForgotPasswordLabel(QLabel):
    clicked = pyqtSignal()
    rightClicked = pyqtSignal()

    def __init__(self, *args):
        super().__init__(*args)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        style = """
                       QLabel{
                           color: %s;
                           font-size: %s;
                           margin: 0 10px;
                           text-decoration: underline;
                       }
                       """ % (SessionWrapper.font_color, '16px')
        self.setStyleSheet(style)
        self.setMaximumHeight(45)
        self.fixWidth()

    def mousePressEvent(self, ev):
        if ev.button() == Qt.LeftButton:
            self.clicked.emit()
        elif ev.button() == Qt.RightButton:
            self.rightClicked.emit()

    def fixWidth(self):
        length = len(self.text())
        if length > 2:
            self.setFixedWidth(int(length*9.5))
