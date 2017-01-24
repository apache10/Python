#walk thorugh all the directories for given path
import os
import sys
import glob


#The method walk() generates the file names in a directory
# tree by walking the tree either top-down or bottom-up.
def readFilesDirectory(var):
	rootsP = next(os.walk(var))[0]
	print("rootsP= %s" %rootsP)
	listDir=[]
	for roots, dirs, files in os.walk(rootsP):
	    listDir.append(roots)
	directoryFiles=[]
	for r in reversed(listDir):
	    # print r+":-"
	    # print"\n"
	    os.chdir(r)
	    #in this case we are takin all type of file  
	    #in directories present in list listDir
	    for file in glob.glob("*.*"):
	    	directoryFiles.append(r+":-\t"+file)
	    # 	print(file)
	    # print "\n\n"
	for i in range(0,len(directoryFiles)):
		print directoryFiles[i]