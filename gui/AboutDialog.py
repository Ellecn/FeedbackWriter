from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout, QPushButton
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt

import consts

class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Über " + consts.APP_TITLE)
        self.setFixedSize(260, 200)
        self.setWindowIcon(QIcon("icons/icon.png"))

        layout = QVBoxLayout()

        lblIcon = QLabel()
        lblIcon.setPixmap(QPixmap("icons/icon.png"))

        lblLink = QLabel()
        lblLink.setText('<a href="https://github.com/Ellecn/FeedbackWriter">https://github.com/Ellecn/FeedbackWriter</a>')
        lblLink.setTextFormat(Qt.RichText)
        lblLink.setTextInteractionFlags(Qt.TextBrowserInteraction)
        lblLink.setOpenExternalLinks(True)

        layout.addWidget(lblIcon, alignment=Qt.AlignHCenter)
        layout.addWidget(QLabel(consts.APP_TITLE), alignment=Qt.AlignHCenter)
        layout.addWidget(QLabel(f"Version {consts.APP_VERSION}"), alignment=Qt.AlignHCenter)
        layout.addWidget(lblLink, alignment=Qt.AlignHCenter)

        btnOk = QPushButton("OK")
        btnOk.clicked.connect(self.accept)
        layout.addWidget(btnOk)

        self.setLayout(layout)