# Eintrag in der CRONTAB unter dem User root
#
# xxxx ist durch den Benutzernamen zu ersetzen.
# Alle anderen Pfade können natürlich ebenfalls angepasst werden.
# 59 23 * * * /usr/bin/python3 /home/xxxx/PVAnlage/Logfiles/WriteLogfile.py
# 0 * * * * /usr/bin/python3 /home/xxxx/PVAnlage/Logfiles/WriteLogfile.py
# Achtung in der Crontab als auch unter Anacron funtionieren keine relativen Pfade.
# Also die Pfade immer genau angeben


from re import T
from urllib.request import urlopen
import time


jahr = int(time.strftime("%Y"))
monat = int(time.strftime("%m"))
tag = int(time.strftime("%d"))

ipAddress = "192.168.178.101"
# pfad = "/home/xxxx/PVAnlage/Logfiles/Logfiles/"
pfad = ""  # Speichert die Logfiles im aktuellen Verzeichnis.

LogAddress = "http://" + ipAddress + "/log/" + str(jahr) + "/" + str(monat).zfill(2) + "/" + str(tag).zfill(2) + ".log"
dateiname = pfad + str(jahr) + "-" + str(monat).zfill(2) + "-" + str(tag).zfill(2) + ".txt"
html = urlopen(LogAddress).read().decode("utf-8")
datei = open(dateiname, "w")
datei.write(html)
