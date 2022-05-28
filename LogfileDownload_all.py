from urllib.request import urlopen
from datetime import date
import time
import calendar
import configparser
import os


def readConfig():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config


def logread(config):
    vonJahr = int(config["conf"]["jahr"])
    vonMonat = int(config["conf"]["monat"])
    vonTag = int(config["conf"]["tag"])

    bisJahr = int(time.strftime("%Y"))
    bisMonat = int(time.strftime("%m"))
    bisTag = int(time.strftime("%d"))

    if vonJahr == 0:
        vonJahr = bisJahr
        config["conf"]["fortschreiben"] = "False"

    if vonMonat == 0:
        vonMonat = bisMonat
        config["conf"]["fortschreiben"] = "False"

    if vonTag == 0:
        vonTag = bisTag
        config["conf"]["fortschreiben"] = "False"

    bisDatum = date(bisJahr, bisMonat, bisTag)

    global fehler
    fehler = 0

    try:
        if str(config["conf"]["fortschreiben"]) == "True":
            os.remove(config["conf"]["pfad"] + "logfile.txt")
    except:
        pass

    for jahr in range(vonJahr, bisJahr + 1):
        for monat in range(vonMonat, 12 + 1):
            for tag in range(vonTag, calendar.monthrange(jahr, monat)[1] + 1):
                nowDatum = date(jahr, monat, tag)
                if nowDatum > bisDatum:
                    return

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

                try:
                    html = ""
                    html = urlopen(LogAddress).read().decode("utf-8")
                    if str(config["conf"]["fortschreiben"]) == "True":
                        datei = open(config["conf"]["pfad"] + "logfile.txt", "a")
                    else:
                        dateiname = (
                            config["conf"]["pfad"] + str(jahr) + "-" + str(monat).zfill(2) + "-" + str(tag).zfill(2) + ".txt"
                        )
                        try:
                            if nowDatum != bisDatum:
                                writeOption = "x"
                            else:
                                writeOption = "w"
                            datei = open(dateiname, writeOption)
                            datei.write(html)
                            print(str(tag).zfill(2) + "." + str(monat).zfill(2) + "." + str(jahr) + " Logfile geschrieben")
                        except:
                            print(str(tag).zfill(2) + "." + str(monat).zfill(2) + "." + str(jahr) + " Lofgile schon vorhanden")

                except:
                    if html != "":
                        print(
                            str(tag).zfill(2) + "." + str(monat).zfill(2) + "." + str(jahr) + " Fehler kein Lofgile geschrieben"
                        )
                        fehler += 1
                    else:
                        print(
                            str(tag).zfill(2)
                            + "."
                            + str(monat).zfill(2)
                            + "."
                            + str(jahr)
                            + " kein Eintrag im Lofgile oder Logfile nicht vorhanden"
                        )
                    continue
            vonTag = 1
        vonMonat = 1


def main():
    logread(config=readConfig())
    print()
    if fehler == 0:
        print("Skript wurde ohne Fehler beendet")
    else:
        print("Es konnten {0} Logfiles nicht gelesen bzw. geschrieben werden".format(fehler))
    print()


if __name__ == "__main__":
    main()
