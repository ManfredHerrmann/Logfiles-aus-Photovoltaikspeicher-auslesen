# Changelog

### Version 1.0
##### 2022-05-27

Erstmalige Veröffentlichung. Bitte die README.md beachten.

### Version 1.1
##### 2022-05-28 

**LogfileDownload_all.py**

* Skript ist per Configfile konfigurierbar.
* Es kann ein genauer Startzeitpunkt eingestellt werden.
* Das Skript beendet sich nach dem Lese des Tagesaktuellen Logfiles
* Download beschränken auf aktuellen Tag, Monat, Jahr

**LogfileDownload_cronjob.py**

Hier wurden noch keine weiteren Anpassungen vorgenommen. 

### Version 1.2
##### 2022-05-28 

**LogfileDownload_all.py**

* Die Ausgabe kann mittels output = False abgeschalten werden.
* config.ini angepasst
* README.md angepasst

### Version 1.3
##### 2022-05-28 

**LogfileDownload_all.py**

* Dateiname LogfileDownload_all.py auf LogfileDownload.py geändert.
* README angepasst.

### Version 1.4
##### 2022-05-28 

**LogfileDownload_all.py**

* Fehlerbehebung

### Version 2.0
##### 2022-05-29 

**LogfileDownload_all.py**

* Verzeichnis für die Logfiles wird automatisch angelegt dabei
  ist es egal von wo an das Skript aufruft. Das Verzeichnis wird immer
  unterhalb des Verzeichnisses angelegt in dem das eigentliche Skript liegt.

* Ablaufverbesserungen
* Leichte Geschwindigkeitsverbesserung
