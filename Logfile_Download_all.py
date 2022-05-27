from re import T
from urllib.request import urlopen
import calendar
import time

# Jahr der Inbetriebnahme
inbetriebnahmeJahr = 2021

# IP Adresse des Speichers
ipAddress = "192.168.178.101"  # IP Adresse des Speichers

# Pfad in dem die Logs gespeichert werden sollen.
# Wichtig ist das am Ende ein / eingefügt wird.
# Bei keiner Pfadangabe werden die Logfiles in das aktuelle Verzeichnis geschrieben.

pfad = ""


for jahr in range(inbetriebnahmeJahr, int(time.strftime("%Y")) + 1):
    for monat in range(1, 12 + 1):
        for tag in range(1, calendar.monthrange(jahr, monat)[1] + 1):
            LogAddress = (
                "http://" + ipAddress + "/log/" + str(jahr) + "/" + str(monat).zfill(2) + "/" + str(tag).zfill(2) + ".log"
            )
            dateiname = pfad + str(jahr) + "-" + str(monat).zfill(2) + "-" + str(tag).zfill(2) + ".txt"
            try:
                html = urlopen(LogAddress).read().decode("utf-8")
                print(str(jahr) + "." + str(monat).zfill(2) + "." + str(tag).zfill(2) + " Logfile geschrieben")
                datei = open(dateiname, "w")
                # datei = open("logfile.txt", "a")
                datei.write(html)
            except:
                print(str(jahr) + "." + str(monat).zfill(2) + "." + str(tag).zfill(2) + " Kein Logfile geschrieben")
                continue
