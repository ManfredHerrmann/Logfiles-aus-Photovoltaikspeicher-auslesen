# Logfile Download aus Photovoltaikspeicher auslesen
Dieses Python Skript liest die Logfiles aus einem Pythovoltaik Speicher eines Herstellers aus Leipzig aus. Falls auf euerem Rechner noch kein Python3 installiert, ist bitte erst die *README_Python_install.md* lesen.

Bei GitHub seid ihr schon gelandet und habt die README Datei gefunden. Jetzt müsst ihr nur noch das ganze auf euren Computer herunterladen. 
Dazu einfach oben rechts auf den grünen Butten der mit *Code* beschriftet ist anklicken. Es öffnet sich ein kleines Fenster und dort klickt ihr auf Download ZIP. Nach dem Download einfach in euer Download Verzeichnis schauen und die ZIP Entpacken.

Bei mir sieht das dann so aus. 
*C:\Users\galli\Downloads\Logfiles-aus-Photovoltaikspeicher-auslesen-main\Logfiles-aus-Photovoltaikspeicher-auslesen-main*
Jetzt könnt ihr das Verzeichnis *Logfiles-aus-Photovoltaikspeicher-auslesen-main* in dem die ganzen Dateien enthalten sind irgendwohin schieben, wo ihr es haben möchtet. 

Dort bearbeitet ihr erst einmal die **config.ini** deren Aufbau ich hier erkläre.

Der Aufbau der Datei sieht dann so aus:
```
[conf]
ipAddress = 192.168.178.27
tag = 0
monat = 0
jahr = 0
pfad = logfiles
append = no
```
**ipSpeicher:**
Ist die IP-Adresse des Stromspeichers. Diese kann auf dem Display des Speichers abgelesen werden. Das funktioniert auch in der Fernabschaltung.

**tag, monat und jahr:**
Hier wird angegeben ab welchen Datum die Logfiles aus dem Speicher gelesen werden sollen. Am idealsten ist natürlich das Inbetriebnahmedatum des Speichers.

**pfad:**
Hier am besten alles so lassen wir es voreingestellt ist. Die Logfeils werden dann beim Ausführen des Skripts automatisch in einen Ordner namens logfiles geschrieben. Ist dieser noch nicht vorhanden wird er automascht erstellt.

**append:** 
Mit diesem Parameter kann eingestellt werden ob für jeden Tag eine eigene Datei erstellt wird oder ob alles in eine Datei geschrieben wird. Ist in den Parametern *tag, monat oder jahr* eine 0 eingetragen ist diese funktion gesperrt und es werden immer alle Logfiles in einzelne Dateien geschrieben. Da beim aktiven weiterschreiben (eine Datei) wird die Datei erst geleert und dann neu gefüllt.

Mögliche einstellungen sind *yes* und *no*


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



