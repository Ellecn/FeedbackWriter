from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListView, QAbstractItemView
from PySide6.QtGui import QStandardItemModel, QStandardItem, QFont

import consts

class PersonList(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.lstPersons = QListView()
        self.lstPersons.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.font = QFont()
        self.font.setPointSize(consts.DEFAULT_FONT_SIZE)
        self.lstPersons.setFont(self.font)

        self.model = QStandardItemModel(self.lstPersons)
        self.lstPersons.setModel(self.model)

        lblPersons = QLabel("Personen")
        lblPersons.setStyleSheet("font-weight: bold")

        layout.addWidget(lblPersons)
        layout.addWidget(self.lstPersons)
    
    def populate(self, texts):
        self.model.clear()
        for text in texts:
            item = QStandardItem(text[0])
            self.model.appendRow(item)

    def getIndex(self, person):
        for row in range(self.model.rowCount()):
            index = self.model.index(row, 0)
            if index.data() == person:
                return index
        return None

    def getSelectedPerson(self):
        selected_indexes = self.lstPersons.selectionModel().selectedIndexes()
        if selected_indexes:
            selected_index = selected_indexes[0]
            return selected_index.data()
        else:
            return None

    def setCurrentIndex(self, index):
        self.lstPersons.setCurrentIndex(index)

    def addOnChangedHandler(self, handler):
        self.lstPersons.clicked.connect(handler)
    
    def increaseFontSize(self):
        self.font.setPointSize(self.font.pointSize() + 1)
        self.lstPersons.setFont(self.font)

    def decreaseFontSize(self):
        self.font.setPointSize(self.font.pointSize() - 1)
        self.lstPersons.setFont(self.font)

    def resetFontSize(self):
        self.font.setPointSize(consts.DEFAULT_FONT_SIZE)
        self.lstPersons.setFont(self.font)