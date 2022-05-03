#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 3 10:12:31 2022
Edited on Sat Mar 5 05:02:22 2022
@author: dmytrenko.o
"""
import time
t0 = time.time()

import sys
stdOutput = open("outlog.log", "w")
sys.stderr = stdOutput
sys.stdout = stdOutput

import os, zipfile

def unzip(setDir, lang):
    try:
        with open(os.getcwd()+setDir+"/{0}.zip".format(lang), "r") as file:
            fzip = zipfile.ZipFile(file)
            fzip.extractall(setDir)
            fzip.close()
            file.close()
            print ("{0}.zip set was unziped successfuly!".format(lang))
    except:
        print ("Please check {0} and unpack {1} in the {0} folder.".format(setDir, lang))   
    return

if __name__ == "__main__":
        try:
            setDir = sys.argv[1] #format of input set is "train" or "test"
            lang = sys.argv[2] #format of input languale is "uk", "ru" or "en"
        except:
            print ("¯\_(ツ)_/¯ Error input directory of set or language of set!")
            #text = input()
            #lang = input()
    
        unzip(setDir, lang)
    
print ("\n ツ You are lucky! The program successfully finished!\n")
print (time.time() - t0)
