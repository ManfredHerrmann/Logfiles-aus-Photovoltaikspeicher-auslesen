from urllib.request import urlopen
from datetime import date
import time
import calendar
import configparser
import os


# Lesen der Konfiguration
def readConfig():
    global config
    config = configparser.ConfigParser()
    config.read(os.path.dirname(__file__) + "/config.ini")
    return config


def logfileSpeicher(LogAddress):
    html = ""
    html = urlopen(LogAddress).read().decode("utf-8")
    return html


# Verzeichnis für die Logfiles anlegen falls es nicht schon vorhanden ist.
def verzeichnisCreate(config):
    global pfad
    pfad = os.path.dirname(__file__) + "/" + config["conf"]["pfad"] + "/"
    if not os.path.isdir(pfad):
        os.makedirs(pfad)
        print("Verzeichnis: " + pfad + " wurde angelegt")


def writeAppend(dateiname):
    datei = open(pfad + "/" + dateiname, "w+")
    return datei


def writeSingle(dateiname):
    datei = open(pfad + "/" + dateiname, "x")
    return datei


# Hier werden die Logfiles aus dem Speicher gelesen
def logfilesLesen(config):
    # Setzen des Zeitraums in dem die Logfiles gelesen werden
    vonJahr = int(config["conf"]["jahr"])
    vonMonat = int(config["conf"]["monat"])
    vonTag = int(config["conf"]["tag"])

    nowJahr = int(time.strftime("%Y"))
    nowMonat = int(time.strftime("%m"))
    nowTag = int(time.strftime("%d"))

    # Von / Bis Zeitruam gleich setzten damit kann man tägliche Logfiles
    # Schreiben und ist geeignet für die Automatische verarbeitung z.B.
    # in einem CronJob
    if vonJahr == 0:
        vonJahr = nowJahr
        config["conf"]["append"] = "no"

    if vonMonat == 0:
        vonMonat = nowMonat
        config["conf"]["append"] = "no"

    if vonTag == 0:
        vonTag = nowTag
        config["conf"]["append"] = "no"

    # Heutiges Datum in ein Datumsformat bringen
    bisDatum = date(nowJahr, nowMonat, nowTag)

    # Datei öffnen für Fortschreiben (Append)
    if config["conf"]["append"] == "yes":
        datei = writeAppend("logfile.txt")

    for jahr in range(vonJahr, nowJahr + 1):
        for monat in range(vonMonat, 12 + 1):
            for tag in range(vonTag, calendar.monthrange(jahr, monat)[1] + 1):
                nowDatum = date(jahr, monat, tag)
                if nowDatum > bisDatum:
                    return
                # URL zum Auslesen des Speichers generieren
                LogAddress = (
                    "http://"
                    + str(config["conf"]["ipSpeicher"])
                    + "/log/"
                    + str(jahr)
                    + "/"
                    + str(monat).zfill(2)
                    + "/"
                    + str(tag).zfill(2)
                    + ".log"
                )

                # Das eigentliche Logfile aus dem Speicher lesen
                try:
                    html = logfileSpeicher(LogAddress)
                except:
                    print(date(jahr, monat, tag).strftime("%d.%m.%Y") + " kein Logfile im Speicher")
                    continue
                # Logfile schreiben (Single)
                if not config["conf"]["append"] == "yes":
                    try:
                        datei = writeSingle(str(date(jahr, monat, tag)) + ".txt")
                    except:
                        print(date(jahr, monat, tag).strftime("%d.%m.%Y") + " Logfile ist bereits vorhanden")
                        continue
                datei.write(html)
                print(date(jahr, monat, tag).strftime("%d.%m.%Y") + " Logfile wurde geschrieben")
            vonTag = 1  # muss auf 1 gesetzt werden sonst begint der neue Tag des Monats ebenfalls bei z.B. 3
        vonMonat = 1  # muss auf 1 gesetzt werden sonst begint der neue Monate des Jahres ebenfalls bei z.B. 3


def main():
    config = readConfig()
    verzeichnisCreate(config)
    logfilesLesen(config)


if __name__ == "__main__":
    main()
