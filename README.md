# Logfile Download aus Photovoltaikspeicher auslesen
Dieses Python Skripte lesen die Logfiles aus einem Pythovoltaik Speicher eines Herstellers aus Leipzig aus.

### LogfileDownload_all.py

Dieses Skript liest alle Logfiles aus dem Speicher aus. Dieses Skript ist entwickelt worden, um erstmalig alle Logfiles aus dem Speicher zu lesen, um hier ebenfalls eine Historie zu besitzen. Man kann das Skript auch mehrfach benutzen und vorhandene Logfiles werden dann einfach überschrieben. 

Das Skript wird mittels Konfigurationsfile gesteuert. In der der Datei **config.ini** können verschiedenste Parameter eingestellt werden. 

```
[conf]
ipSpeicher = 192.168.178.10
tag = 3
monat = 9
jahr = 2021
pfad = log/
fortschreiben = False
```

#### Parameter config.ini

**ipSpeicher** ist die IP Adresse des Stromspeichers

**tag**, **monat** und **jahr** beschreiben ab welchem Datum die Logs gelesen werden sollen. Idealerweise sollte das der Tag der in Betriebnahme sein. Es ist aber auch Möglich für tag, Monat eine *1* einzusetzen. Dann wird am 01.01.jahr angefangen die Logs zu lesen. Sollte es kein Logfile geben bekommt man die Meldung kein Eintrag im Lofgile oder Logfile nicht vorhanden

**pfad** Hier kann man festlegen wohin die Logfiles geschrieben werden. Es ist darauf zu achten das am Ende immer ein    \ (Backslash) angefügt wird. Möchte man das alle Logfiles unterhalb des aktullen Ordners abgelgt werden braucht man nur logfiles\ schreiben. Aber am besten man gibt einen absoluten Pfad ein wie z.B. e:\dokumente\stromspeicher\logfiles\ dann ist es egal aus welchen Ordner man das Skript startet. Wird hingegen kein Pfad angegeben als pfad = dann werden alle Logfiles im aktuellen Ordner angezeigt.

**fortschreiben** kennt zwei Zustände True und False (unbeding auf Groß und Kleinschreibung achten)
Ist der Schalter im Zustand True werden alle Logfiles in eine Datei geschrieben. Ist der Schalter dagegen im Zustand False wird für jeden Tag eine neue Datei angelegt.

#### LogfileDownload_cronjob.py

Dieses Skript ist für die Zeitgesteuerte Ausführung entwickelt worden. Hier wird immer nur das vom aktuellen Tag gültige Logfile aus dem Speicher gelesen und gespeichert. Die Systemzeit ist hierfür maßgeblich. 
Da ich noch viel mehr Parameter aus dem Speicher auslese und in eine SQL Datenbank schreibe habe ich mir einen kleinen Raspberry PI in mein heimisches Netzwerk gehängt der 24/7 mitläuft. Die Zeitsteuerung habe ich mittels Cronjob auf dem Raspberry umgesetzt. Dazu müssen folgende Parameter in der **crontab** gesetzt werden.

Das Skript kann selbstverständlich auch auf einem Windows System gestartet werden. Es wird auch hier nur das Tagesaktuelle Skript herunterladen.

#### Zeitsteuerung unter Linux

Wie schon erwähnt benutze ich unter Linux einen Cronjob um die Zeitsteuerung zu verwirklichen. Dazu muss man nur in die **crontab** mittels 

```
crontab -e
```

einsteigen. 

Folgende Eintragungen haben sich als praktikabel erwiesen.

XXXX Beschreibt den Speicherort eures Skiptes. Also ersetzt das XXXX durch euren Speicherort.

Bei mir ist es z.B.

**/home/pi/pvanlage**

```
# Schreibt um 23:59 Uhr das Logfile auf die Speicherkarte
59 23 * * * /usr/bin/python3 XXXX/LogfileDownload_cronjob.py

# Schreibt zur jeden vollen Stunden das Logfile auf die Speicherkarte
0 * * * * /usr/bin/python3 XXXX/LogfileDownload_cronjob.py
```


