# Logfile Download aus Photovoltaikspeicher auslesen
Dieses Python Skripte lesen die Logfiles aus einem Pythovoltaik Speicher eines Herstellers aus Leipzig aus.

###LogfileDownload_all.py

Dieses Skript liest alle Logfiles aus dem Speicher aus. Dieses Skript ist entwickelt worden, um erstmalig alle Logfiles aus dem Speicher zu lesen, um hier ebenfalls eine Historie zu besitzen. Man kann das Skript auch mehrfach benutzen und vorhandene Logfiles werden dann einfach überschrieben. 

Es wird per Kommandozeilenparameter gesteuert. Die ich hier kurz erkläre.

**-jahr**
    definiert das Jahr in dem der Speicher in Betrieb genommen worden ist.

**-ip** 
    Gibt die IP-Adresse des Speichers an. Diese kann im Display direkt am Speicher abgelesen werden.

**-pfad**
    hier gibt man den Speicherpfad der runtergeladenen Logfiles an.
    
Das Skript liest immer ein komplettes Jahr. Also geben wir z.B. dem Parameter **jahr** 2021 mit dann wird das Skript
beim 01.01.2021 beginnen zu lesen. Sollte es an diesem Tag noch kein Logfile geben, weil der Speicher erst am 06.07.2021 das erstem in Betrieb gegangen ist so bekommt man die Rückmeldung das kein Logfile geschrieben wurde. Das passiert so lange bis der 31.12. des aktuellen Jahres erreicht worden ist.


###LogfileDownload_cronjob.py

Dieses Skript ist für die Zeitgesteuerte Ausführung entwickelt worden. Hier wird immer nur das vom aktuellen Tag gültige Logfile aus dem Speicher gelesen und gespeichert. Die Systemzeit ist hierfür maßgeblich.
Da ich noch viel mehr Parameter aus dem Speicher auslese und in eine SQL Datenbank schreibe habe ich mir einen kleinen Raspberry PI in mein heimisches Netzwerk gehängt der 24/7 mitläuft. Die Zeitsteuerung habe ich mittels Cronjob auf dem Raspberry umgesetzt. Dazu müssen folgende Parameter in der **crontab** gesetzt werden.

```
# Schreibt um 23:59 Uhr das Logfile auf die Speicherkarte
59 23 * * * /usr/bin/python3 /home/michael/pvanlage/Logfile_Downloader/Logfile_Download_cron.py

# Schreibt zur jeden vollen Stunden das Logfile auf die Speicherkarte
0 * * * * /usr/bin/python3 /home/michael/pvanlage/Logfile_Downloader/Logfile_Download_cron.py
```
