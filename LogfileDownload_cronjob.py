from re import T
from urllib.request import urlopen
import time


jahr = int(time.strftime("%Y"))
monat = int(time.strftime("%m"))
tag = int(time.strftime("%d"))

ipAddress = "192.168.178.101"
pfad = ""  # Speichert die Logfiles im aktuellen Verzeichnis.

LogAddress = "http://" + ipAddress + "/log/" + str(jahr) + "/" + str(monat).zfill(2) + "/" + str(tag).zfill(2) + ".log"
dateiname = pfad + str(jahr) + "-" + str(monat).zfill(2) + "-" + str(tag).zfill(2) + ".txt"
html = urlopen(LogAddress).read().decode("utf-8")
datei = open(dateiname, "w")
datei.write(html)
