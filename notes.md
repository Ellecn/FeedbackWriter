Changelog und Roadmap
=====================

Version 0.1 (6.6.2025)
----------------------

Version 0.2 (6.6.2025)
----------------------

- [x] FEATURE: Link in AboutDialog klickbar machen
- [x] FEATURE: Icon in AboutDialog hinzufügen
- [x] FEATURE: Schriftgröße einstellbar machen
- [x] FEATURE: Schriftart im Editor für bessere Lesbarkeit anpassen

Version 0.3 (6.6.2025)
-----------------------

- [x] FEATURE: Warnung beim Beenden und öffnen, falls es noch ungespeicherte Änderungen gibt
- [x] FEATURE: Indikator anzeigen, falls es ungespeicherte Änderungen gibt
- [x] FEATURE: Zeile highlighten, in der es einen Fehler gibt

Version 0.4 (7.6.2025)
----------------------

- [x] FEATURE: Meldung anzeigen, sobald das Generieren der individuellen Texte abgeschlossen ist
- [x] REFACTORING: Alle icons in eigenen Ordner packen

Version 0.5
-----------

- [x] BUG: Beim Pasten eines Textes in den Editor spielt die Formtierung verrückt
- [ ] FEATURE: Tags fett hervorheben
- [ ] FEATURE: Anzeige, wie lang die generierten Texte sind (als Nummer hinter den Namen in der Liste?)

Backlog
-------

- [ ] DOCUMENTATION: Handbuch erweitern (z. B. reinschreiben, dass zwei Zeilen unter einer tag-Zeile nicht erlaubt sind)
- [ ] DOCUMENTATION: Lizenztext zum AboutDialog hinzufügen (für die App und für die Icons)
- [ ] FEATURE: Zeilennummern im Editor anzeigen
- [ ] FEATURE: File not found message, wenn das Handbuch nicht gefunden wird

Version 1.0
-----------

- [ ] FEATURE: Ähnlichkeitsanalyse

Version 2.0
-----------

- [ ] FEATURE: Textbaustein-Bibliothek

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