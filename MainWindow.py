import sys, os

from PySide6.QtWidgets import QWidget, QApplication, QHBoxLayout, QFileDialog, QMessageBox

from Generator import Generator
from Editor import Editor
from Preview import Preview
from PersonList import PersonList
from AboutDialog import AboutDialog

from BaseMainWindow import BaseMainWindow

import consts

class MainWindow(BaseMainWindow):
    def __init__(self):
        super().__init__(f"{consts.APP_TITLE} {consts.APP_VERSION}", "icons/icon.png", 1200, 800)

        self.addMenuAction("&Datei", "Öffnen...", self.open_file)
        self.addMenuAction("&Datei", "Speichern", self.save_file)
        self.addMenuSeparator("&Datei")
        self.addMenuAction("&Datei", "Individuelle Texte generieren...", self.save_generated_texts)
        self.addMenuSeparator("&Datei")
        self.addMenuAction("&Datei", "Beenden", self.close)
        self.addMenuAction("&Hilfe", "Handbuch", lambda: os.startfile(os.path.join("doc", "Handbuch.pdf")))
        self.addMenuSeparator("&Hilfe")
        self.addMenuAction("&Hilfe", f"Über {consts.APP_TITLE}...", lambda: AboutDialog().exec())

        self.addToolbarAction("icons/zoom_in.png", "Schrift vergrößern", self.increaseFontSize)
        self.addToolbarAction("icons/zoom_out.png", "Schrift verkleinern", self.decreaseFontSize)
        self.addToolbarAction("icons/reset_zoom.png", "Schriftgröße zurücksetzen", self.resetFontSize)

        widget = QWidget()
        layout = QHBoxLayout(widget)

        self.lstPersons = PersonList()
        self.lstPersons.addOnChangedHandler(self.on_person_selected)

        self.txtPreview = Preview()

        self.txtEditor = Editor()
        self.txtEditor.addOnTextChangedHandler(self.on_text_changed)

        layout.addWidget(self.txtEditor, stretch=3)
        layout.addWidget(self.lstPersons, stretch=1)
        layout.addWidget(self.txtPreview, stretch=3)
        
        self.setCentralWidget(widget)

        self.generator = Generator()
        self.texts = []

    def increaseFontSize(self):
        self.txtEditor.increaseFontSize()
        self.lstPersons.increaseFontSize()
        self.txtPreview.increaseFontSize()

    def decreaseFontSize(self):
        self.txtEditor.decreaseFontSize()
        self.lstPersons.decreaseFontSize()
        self.txtPreview.decreaseFontSize()

    def resetFontSize(self):
        self.txtEditor.resetFontSize()
        self.lstPersons.resetFontSize()
        self.txtPreview.resetFontSize()

    def on_text_changed(self):
        try:
            self.texts = self.generator.generate(self.txtEditor.getText())
        except Exception as e:
            self.txtEditor.setError(int(f"{e}"))
            self.lstPersons.populate([])
            self.txtPreview.clear()
            return
        
        self.txtEditor.setError(None)

        selected_person = self.lstPersons.getSelectedPerson()
        
        self.lstPersons.populate(self.texts)

        if selected_person:
            index = self.lstPersons.getIndex(selected_person)
            if index:
                self.lstPersons.setCurrentIndex(index)
                self.on_person_selected(index)
            else:
                self.txtPreview.clear()

    def on_person_selected(self, index):
        for text in self.texts:
            if text[0] == index.data():
                self.txtPreview.setText(text[0], text[1])
                break
    
    def open_file(self):
        if self.txtEditor.unsavedChanges:
            reply = QMessageBox.question(self, consts.APP_TITLE, "Änderungen speichern?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                self.txtEditor.save()

        filePath = self.txtEditor.open()
        if filePath:
            self.setWindowTitle(f"{consts.APP_TITLE} {consts.APP_VERSION} - {filePath}")
    
    def save_file(self):
        filePath = self.txtEditor.save()
        if filePath:
            self.setWindowTitle(f"{consts.APP_TITLE} {consts.APP_VERSION} - {filePath}")
        else:
            self.setWindowTitle(f"{consts.APP_TITLE} {consts.APP_VERSION}")

    def save_generated_texts(self):
        if self.texts and len(self.texts) > 0:
            directory = QFileDialog.getExistingDirectory(self, "Ordner auswählen", "", QFileDialog.ShowDirsOnly)
            if directory: 
                for text in self.texts:
                    self._writeFile(os.path.join(directory, text[0] + ".txt"), text[1])
                QMessageBox.information(self, consts.APP_TITLE, f"{len(self.texts)} Texte generiert.")

    def _writeFile(self, file_path, content):
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

    def closeEvent(self, event):
        if self.txtEditor.unsavedChanges:
            reply = QMessageBox.question(self, consts.APP_TITLE, "Änderungen vor dem Beenden speichern?", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Yes)
            if reply == QMessageBox.Cancel:
                event.ignore()
                return
            elif reply == QMessageBox.Yes:
                result = self.txtEditor.save()
                if result == None:
                    event.ignore()
                    return
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())