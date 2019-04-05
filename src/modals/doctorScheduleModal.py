from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTextEdit


class DoctorScheduleModal(QDialog):
    def __init__(self, title, text):
        super().__init__()
        self.setWindowIcon(QIcon('resources/assets/images/icon.ico'))
        self.setObjectName("doctor_schedule")
        body = QVBoxLayout()
        text_section = QTextEdit()
        text_section.setText(text)
        text_section.setReadOnly(True)
        text_section.setAlignment(Qt.AlignLeft)
        text_section.setMinimumHeight(350)
        body.addWidget(text_section)
        self.resize(400, 370)
        self.setWindowTitle(title)
        self.setLayout(body)
        self.exec_()


