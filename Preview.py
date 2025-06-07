from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit
from PySide6.QtGui import QFont

import consts

class Preview(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.txtPreview = QTextEdit()
        self.txtPreview.setReadOnly(True)
        self.font = QFont()
        self.font.setPointSize(consts.DEFAULT_FONT_SIZE)
        self.txtPreview.setFont(self.font)

        layout.addWidget(QLabel("Vorschau"))
        layout.addWidget(self.txtPreview)
    
    def setText(self, text):
        self.txtPreview.setPlainText(text)
    
    def increaseFontSize(self):
        self.font.setPointSize(self.font.pointSize() + 1)
        self.txtPreview.setFont(self.font)

    def decreaseFontSize(self):
        self.font.setPointSize(self.font.pointSize() - 1)
        self.txtPreview.setFont(self.font)

    def resetFontSize(self):
        self.font.setPointSize(consts.DEFAULT_FONT_SIZE)
        self.txtPreview.setFont(self.font)