__author__ = 'matthias'

import subprocess as sub
import os
import string

ordner = "bilder"
fileNames = ['IMG_7633.JPG', "IMG_7634.JPG", "IMG_7635.JPG", 'IMG_7633.JPG', "IMG_7634.JPG", "IMG_7743.JPG"]
outputName = "speichern.jpg"
# 3x2 = 3 spalte, 2 zeilen
anordnung = "3x2"


NumFiles = len(fileNames)

labels = list(string.ascii_lowercase)[0:NumFiles]
print labels

p = os.chdir("./" + ordner)

command = ["montage", "-tile", anordnung, "-geometry", "1600x1200+10+1", "-pointsize", "60"]

i = 0
for names in fileNames:
    command.append("-label")
    command.append(labels[i] + ")")
    command.append(names)
    print names
    i += 1


command.append(outputName)
print command

p = sub.call(command)

print p