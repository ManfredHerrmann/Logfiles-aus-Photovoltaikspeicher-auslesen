# Logfile Download aus Photovoltaikspeicher auslesen
Dieses Python Skripte lesen die Logfiles aus einem Pythovoltaik Speicher eines Herstellers aus Leipzig aus.

Es ist entwickelt worden, um erstmalig alle Logfiles aus dem Speicher zu lesen, damit legt man sich eine Historie an. Das Skript kann auch mehrfach gestartet werden. Es wird wieder bei dem Startdatum begonnen welches in der **config.ini** hinterlegt ist und läuft bis zum aktuellen Datum durch. Sind für einen Zeitraum schon Logfiles vorhanden werden sie nicht wieder neu geschrieben (warum ich diese nicht einfach überschreibe, soll sich jeder selbst denken). Nach dem ersten erfolgreichen Durchlauf kann das Startdatum in der **config.ini** auch näher an das aktuelle Datum heranrücken. Wir haben die vergangenen Logfiles schon.

Ich habe schon die **config.ini** im vorherigen Abschnitt erwähnt. Aber was macht diese Datei eigentlich? Die **config.ini** ist eine einfache Art und Weise Skripte anzupassen, ohne den eigentlichen Quellcode anzupassen.

Wichtig ist nur das man für jede neue Version auch das dazugehörige **config.ini** verwendet.

Der Aufbau der Datei sieht dann so aus:

```
[conf]
ipSpeicher = 192.168.178.10
tag = 3
monat = 9
jahr = 2021
pfad = log/
fortschreiben = False
output = True
```

Im folgenden Abschnitt erkläre ich kurz was die einzelnen Parameter bedeuten und welche Auswirkungen sie auf unser Skript haben.

**ipSpeicher** ist die IP-Adresse des Stromspeichers

**tag**, **monat** und **jahr** beschreiben ab welchem Datum die Logs gelesen werden sollen. Idealerweise sollte das der Tag der Inbetriebnahme sein. 

Es ist aber auch möglich für *tag, monat* eine *1* einzusetzen. Dann wird am 01.01.jahr angefangen die Logsfiles aus dem Speicher zu lesen. Beendet wird das Skript immer mit Erreichen des aktuellen Datums. 

Eine *0* als Parameter bewirkt das hierfür beim Programmablauf der aktuelle Tag, Monat oder Jahr eingesetzt wird. Der Durchlauf endet auch hier mit Erreichen des aktuellen Datums. Setzt man alle drei Parameter auf *0* könnte man das Skript automatisiert um 23:59 Uhr ausführen, um für diesen Tag das aktuelle Logfile zu bekommen. So hat man stets die Aktuellen Logfiles gespeichert. 

Ist *tag* oder *monat* auf *0* gesetzt können nur noch einzelne Dateien pro Tag geschrieben werden. Da man sonst bei einem Mehrfach Aufruf des Skripts ein und das selbe Logfile hintereinander hätte. 

Es werden keine vorhandenen Logfiles überschrieben (warum ich das so gemacht habe, darüber kann jeder für sich selber nachdenken) mit Ausnahme des aktuellen Datums. Dieses Logfile wird überschrieben. Da man sonst keinen neuen Tagesstand herunterladen könnte.

**pfad** hier kann man festlegen, wohin die Logfiles geschrieben werden. Es ist darauf zu achten das am Ende immer ein    \ (Backslash) angefügt wird. Möchte man das alle Logfiles unterhalb des aktuellen Ordners abgelegt werden braucht man nur Logsfiles\ schreiben. Aber am besten man gibt einen absoluten Pfad ein wie z.B. e:\dokumente\stromspeicher\logfiles\ dann ist es egal aus welchem Ordner man das Skript startet. Wird hingegen kein Pfad angegeben als pfad = dann werden alle Logfiles im aktuellen Ordner angezeigt.

**fortschreiben** kennt zwei Zustände True und False (unbedingt auf Groß und Kleinschreibung achten)
Ist der Schalter im Zustand True werden alle Logfiles in eine Datei geschrieben. Ist der Schalter dagegen im Zustand False wird für jeden Tag eine neue Datei angelegt.

**output** Dieser Schalter kann die Textausgabe des Skripts ein bzw. ausschalten. Dabei gilt *True* aktiv und *False* deaktiviert.


#### Zeitsteuerung unter Linux

Wie schon erwähnt benutze ich unter Linux einen Cronjob um die Zeitsteuerung zu verwirklichen. Dazu muss man nur in die **crontab** mittels 

```
crontab -e
```

einsteigen. 

Folgende Eintragungen haben sich als praktikabel erwiesen.

XXXX Beschreibt den Speicherort eures Skriptes. Also ersetzt das XXXX durch euren Speicherort.

Bei mir ist es z.B.

**/home/pi/pvanlage**

```
# Schreibt um 23:59 Uhr das Logfile auf die Speicherkarte
59 23 * * * /usr/bin/python3 XXXX/LogfileDownload.py

# Schreibt zu jedem vollen Stunden das Logfile auf die Speicherkarte
0 * * * * /usr/bin/python3 XXXX/LogfileDownload.py
```


