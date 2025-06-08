from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QFileDialog, QPlainTextEdit
from PySide6.QtGui import QFont, QTextCursor, QColor, QTextFormat

import consts

class Editor(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.filePath = None
        self.unsavedChanges = False

        self.txtEditor = QPlainTextEdit()
        
        self.font = QFont()
        self.font.setPointSize(consts.DEFAULT_FONT_SIZE)
        self.txtEditor.setFont(self.font)

        self.txtEditor.textChanged.connect(self._onTextChanged)

        self.lblHeader = QLabel("Editor")
        self.lblHeader.setStyleSheet("font-weight: bold")

        layout.addWidget(self.lblHeader)
        layout.addWidget(self.txtEditor)

    def _onTextChanged(self):
        self.unsavedChanges = True
        self.lblHeader.setText("Editor (ungespeicherte Änderungen)")

    def open(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Datei auswählen", "", "Textdateien (*.txt)")
        if not fileName:
            return None
        with open(fileName, 'r', encoding='utf-8') as file:
            content = file.read()
            self.txtEditor.setPlainText(content)
        self.filePath = fileName
        self.unsavedChanges = False
        self.lblHeader.setText("Editor")
        return self.filePath

    def save(self):
        if not self.filePath:
            fileName, _ = QFileDialog.getSaveFileName(self, "Datei speichern", "", "Textdateien (*.txt)")
            if not fileName:
                return None
            else:
                self.filePath = fileName
        with open(self.filePath, "w", encoding="utf-8") as file:
            file.write(self.txtEditor.toPlainText())
        self.unsavedChanges = False
        self.lblHeader.setText("Editor")
        return self.filePath

    def setError(self, lineNumber):
        if lineNumber != None:
            self.highlight_line(lineNumber)
        else:
            self.txtEditor.setExtraSelections([])

    def highlight_line(self, line_number):
        doc = self.txtEditor.document()
        block = doc.findBlockByNumber(line_number)
        if not block.isValid():
            return

        cursor = QTextCursor(block)
        cursor.movePosition(QTextCursor.StartOfBlock)
        line_count = block.layout().lineCount()
        extra_selections = []

        for i in range(line_count):
            selection = QTextEdit.ExtraSelection()
            selection.format.setBackground(QColor(255, 0, 0, 80))
            selection.format.setProperty(QTextFormat.FullWidthSelection, True)
            selection.cursor = QTextCursor(cursor)
            selection.cursor.movePosition(QTextCursor.StartOfBlock)
            for _ in range(i):
                selection.cursor.movePosition(QTextCursor.Down)
            selection.cursor.select(QTextCursor.LineUnderCursor)
            extra_selections.append(selection)

        self.txtEditor.setExtraSelections(extra_selections)

    def getText(self):
        return self.txtEditor.toPlainText()
    
    def addOnTextChangedHandler(self, handler):
        self.txtEditor.textChanged.connect(handler)

    def increaseFontSize(self):
        self.font.setPointSize(self.font.pointSize() + 1)
        self.txtEditor.setFont(self.font)

    def decreaseFontSize(self):
        self.font.setPointSize(self.font.pointSize() - 1)
        self.txtEditor.setFont(self.font)

    def resetFontSize(self):
        self.font.setPointSize(consts.DEFAULT_FONT_SIZE)
        self.txtEditor.setFont(self.font)