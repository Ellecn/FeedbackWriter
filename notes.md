Roadmap / Changelog
===================

Version 0.1 (6.6.2025)
----------------------

Version 0.2 (6.6.2025)
----------------------

- [x] Link in AboutDialog klickbar machen
- [x] Icon in AboutDialog hinzufügen
- [x] Schriftgröße einstellbar machen
- [x] Schriftart im Editor für bessere Lesbarkeit anpassen

Version 0.3 (6.6.2025)
-----------------------

- [x] Warnung beim Beenden und öffnen, falls es noch ungespeicherte Änderungen gibt
- [x] Indikator anzeigen, falls es ungespeicherte Änderungen gibt
- [x] Zeile highlighten, in der es einen Fehler gibt

Version 0.4 (7.6.2025)
----------------------

- [x] Meldung anzeigen, sobald das Generieren der individuellen Texte abgeschlossen ist
- [x] Alle icons in eigenen Ordner packen

Version 0.5
-----------

- [ ] Tags fett hervorheben
- [ ] Anzeige, wie lang die generierten Texte sind (als Nummer hinter den Namen in der Liste?)

Backlog
-------

- [ ] Handbuch erweitern (z. B. reinschreiben, dass zwei Zeilen unter einer tag-Zeile nicht erlaubt sind)
- [ ] Lizenztext zum AboutDialog hinzufügen (für die App und für die Icons)
- [ ] Zeilennummern im Editor anzeigen
- [ ] File not found message, wenn das Handbuch nicht gefunden wird

Version 1.0
-----------

- [ ] Ähnlichkeitsanalyse

Version 2.0
-----------

- [ ] Textbaustein-Bibliothek

Ausführbares Programm erzeugen (win64)
======================================

1) Versionsnummer in Code und Handbuch anpassen
2) (pip install pyinstaller)
3) cd to project folder
4) pyinstaller --clean --onefile --windowed --name FeedbackWriter --icon icons\icon.ico MainWindow.py --> exe landet im dist-Ordner im project folder
5) icon-Ordner, zeugnis_beispiel.txt und Handbuch.pdf zur exe kopieren
6) dist-Ordner umbenennen in "FeedbackWriterX.X-win64"
7) FeedbackWriterX.X-win64.zip erstellen
8) FeedbackWriterX.X-win64-Ordner, build-ordner und *.spec-Dateien löschen