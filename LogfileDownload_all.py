from ast import arg
from re import T
from urllib.request import urlopen
import calendar
import time

import argparse


def logread(args):
    for jahr in range(int(args.jahr), int(time.strftime("%Y")) + 1):
        for monat in range(1, 12 + 1):
            for tag in range(1, calendar.monthrange(jahr, monat)[1] + 1):
                LogAddress = (
                    "http://" + args.ip + "/log/" + str(jahr) + "/" + str(monat).zfill(2) + "/" + str(tag).zfill(2) + ".log"
                )
                dateiname = args.pfad + str(jahr) + "-" + str(monat).zfill(2) + "-" + str(tag).zfill(2) + ".txt"
                try:
                    html = urlopen(LogAddress).read().decode("utf-8")
                    print(str(jahr) + "." + str(monat).zfill(2) + "." + str(tag).zfill(2) + " Logfile geschrieben")
                    datei = open(dateiname, "w")
                    # datei = open("logfile.txt", "a")
                    datei.write(html)
                except:
                    print(str(jahr) + "." + str(monat).zfill(2) + "." + str(tag).zfill(2) + " Kein Logfile geschrieben")
                    continue


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-jahr")
    parser.add_argument("-ip")
    parser.add_argument("-pfad")
    args = parser.parse_args()
    if args.jahr == None:
        args.jahr = time.strftime("%Y")
    if args.ip == None:
        print("ACHTUNG!!!")
        print("Keine IP Adresse angegeben")
        print("Bitte den Parameter -ip mit der IP Adresse des Speichers angeben. Beispiel -ip 192.168.178.23")
        exit()
    if args.pfad == None:
        args.pfad = ""

    logread(args)


if __name__ == "__main__":
    main()
