# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 11:33:37 2017

@author: gerald
"""

import os

#global paths
GerberDir = 'Gerber'
NCDir = 'NC Drill'
zipFile = 'Gerber_NCDrill.zip'


def renameMechanicalLayer():
    "renames *.GM2 file to *.GKO file"
    for filename in os.listdir(GerberDir):
        if filename.endswith(".GM3"):
            
            name = os.path.splitext(filename)[0]
            nfilename = name + '.GKO';
            
            if os.path.isfile(os.path.join(GerberDir, nfilename)):
                os.remove(os.path.join(GerberDir, nfilename))
            
            os.rename(os.path.join(GerberDir, filename), os.path.join(GerberDir, nfilename))
            
            print(os.path.join(GerberDir, filename) + ' --> ' + os.path.join(GerberDir, nfilename))
            continue
        else:
            continue
    return
    

import zipfile
    
def createZIP():
    print("Create zip with gerber and NCDrill files")
    
    #open zip file
    ziph = zipfile.ZipFile(zipFile,'w',zipfile.ZIP_DEFLATED)
    
    # look for gerber files
    os.chdir(GerberDir)
    for filename in os.listdir('./.'):
        if filename.endswith(".GBL"):
            ziph.write(os.path.join(filename))
            print(os.path.join(GerberDir, filename) + ' zipped')
            continue
        elif filename.endswith(".GBO"):
            ziph.write(os.path.join(filename))
            print(os.path.join(GerberDir, filename) + ' zipped')
            continue
        elif filename.endswith(".GBS"):
            ziph.write(os.path.join(filename))
            print(os.path.join(GerberDir, filename) + ' zipped')
            continue
        elif filename.endswith(".GKO"):
            ziph.write(os.path.join(filename))
            print(os.path.join(GerberDir, filename) + ' zipped')
            continue
        elif filename.endswith(".GTL"):
            ziph.write(os.path.join(filename))
            print(os.path.join(GerberDir, filename) + ' zipped')
            continue
        elif filename.endswith(".GTO"):
            ziph.write(os.path.join(filename))
            print(os.path.join(GerberDir, filename) + ' zipped')
            continue
        elif filename.endswith(".GTS"):
            ziph.write(os.path.join(filename))
            print(os.path.join(GerberDir, filename) + ' zipped')
            continue
        elif filename.endswith(".DRL"):
            ziph.write(os.path.join(filename))
            print(os.path.join(GerberDir, filename) + ' zipped')
            continue
        elif filename.endswith(".GL2"):
            ziph.write(os.path.join(filename))
            print(os.path.join(GerberDir, filename) + ' zipped')
            continue
        elif filename.endswith(".GL3"):
            ziph.write(os.path.join(filename))
            print(os.path.join(GerberDir, filename) + ' zipped')
            continue
        else:
            continue
    os.chdir('..\.')
    
    #look for NC Drill file
    os.chdir(NCDir)
    for filename in os.listdir('./.'):
        if filename.endswith(".TXT"):
            ziph.write(os.path.join(filename))
            print(os.path.join(GerberDir, filename) + ' zipped')
            continue
        else:
            continue
    os.chdir('..\.')
    
    # close zip file
    ziph.close()
    return

### Main ###
renameMechanicalLayer()
createZIP()

     
#input("Press enter to exit")




