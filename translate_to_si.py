####################################################################################################
#    
#   Simple Sinhala translator (v0.1)
#   --------------------------------
#
#   Developed By: Dananjaya M. Perera (dananjaya01@gmail.com) (https://github.com/dzero1)
#
#   This simple application can be use to translate any text file to sinhala language.
#   I'm using google translater api, with batch line translating to increese the efficiency. 
#   If the translator gives an error because of the length of the text, you can reduce the 
#   "batchCount" and try again.
#
#   Usage example:
#       Python3 translate_to_si.py "/Path/to/your/file"
#   
#   This is required python 3.x
#
#
#   This piece of software has no warranty and I release this under GNU v3 license.
#   So feel free to take the idea or you can take this code to you project.
#
#   Please keep the originality and credits.
#   
#   Thank you.
####################################################################################################


import time
import googletrans
import sys
import os
import math

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

batchCount = 400
batchLines = ""

print ("Simple Sinhala translator")
print ("-------------------------")
print (" ")
print (f"{bcolors.WARNING}Heating up the engine....{bcolors.ENDC}")
print (" ")

# import translater
from googletrans import Translator
translator = Translator()
translator = Translator(service_urls=['translate.googleapis.com'])

# Read the args to get the file
filepath = sys.argv[1]
filename, file_extension = os.path.splitext(sys.argv[1])
print(f"{bcolors.OKBLUE}Reading:{bcolors.ENDC}", filepath)

#input("Press Enter to continue...")

# Open output file
outfilename = filename+'_translated'+file_extension
print(f"{bcolors.OKCYAN}Output file:{bcolors.ENDC}", outfilename)
print (" ")
fileOutput = open(filename+'_translated'+file_extension, 'w')

# Open the file and using readlines()
file = open(filepath, 'r')
Lines = file.readlines()

lineLen = len(Lines)
lang = ""

# If we didn't provide the src language, it will auto detect by scaning lines.
if len(sys.argv) == 2:
    for line in Lines:
        src_lang = translator.detect(line)
        if (src_lang.confidence > 0):
            lang = src_lang.lang
            break
else :
    lang = sys.argv[2]

count = 0

old_progress = 0

# Read line by line
for line in Lines:
    count += 1

    if count % batchCount == 0:
        #if not batchLines.strip().isdigit() and batchLines.strip().find('-->') == -1 and len(batchLines.strip()) > 0:
        result = translator.translate(batchLines.strip(), src=lang, dest='si')
        text = result.text  + "\n"
        fileOutput.writelines(text)
        batchLines = ""

    else :
        # collecting lines batch
        batchLines += line

    progress = int((count/lineLen) * 100)
    if (progress % 10 == 0 and old_progress != progress):
        old_progress = progress
        print("Progress: ", progress, "%")

fileOutput.close()

print (" ")
print (f"{bcolors.OKGREEN}Translation complete. Thanks for using Simple Sinhala translator (v0.1). (By dzero1){bcolors.ENDC}")
print (" ")
print (" ")