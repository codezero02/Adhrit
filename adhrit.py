import zipfile
import os
import sys
import subprocess
import shlex
import argparse
import webbrowser
from Recons.apkRecon import apkRip
from Recons.apkExtract import apkInfo
from Recons.StaticAnalyzer import CodeAnalyzer
from Recons.VirusTotal import APICheck




__author__ = 'Abhishek J M  ( jmabhishek@gmail.com )'


class Adhrit :

    def __init__(self) :

        self.apk_name = ""


    def Welcome(self) :
        os.system('toilet -F metal -f bigascii12 ADHRIT')
        print "\t\twww.github.com/abhi-r3v0/Adhrit "
	print "\n\n"


    def apkripper(self, apk_name) :
        apkRip(apk_name)

    def apkextractor(self, apk_name) :
        apkInfo(apk_name)

    def codeanalyzer(self) :
        CodeAnalyzer()

    def vtanalyzer(self, apk_name) :
        APICheck(apk_name)


#Main fuction starts here
def main() :

    adhrit = Adhrit()
    parser = argparse.ArgumentParser(description = "Help")
    parser.add_argument("-a", help="Dump package info and extract contents and perform analysis")
    parser.add_argument("-r", help="Analyze APK without extraction")
    parser.add_argument("-e", help="Extract APK contents only")
    parser.add_argument("-c", help="Perform static analysis")
    parser.add_argument("-w", help="Just the welcome :P")
    parser.add_argument("-v", help="Check footprints in VirusTotal database")
    args = parser.parse_args()

    if args.a :
        adhrit.Welcome()
        adhrit.apkripper(args.a)
       	adhrit.apkextractor(args.a)
        adhrit.vtanalyzer(args.a)
        adhrit.codeanalyzer()


    elif args.r :
        adhrit.Welcome()
        adhrit.apkripper(args.r)


    elif args.e :
        adhrit.Welcome()
        adhrit.apkextractor(args.e)


    elif args.c :
        adhrit.Welcome();
        adhrit.apkextractor(args.c)
        adhrit.codeanalyzer()


    elif args.w :
        adhrit.Welcome()


    elif args.v :
        adhrit.Welcome()
        adhrit.vtanalyzer(args.v)



if __name__ == "__main__" :
    main()