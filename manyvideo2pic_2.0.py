import sys
import os
import shutil,os

def get_dir(path,fileType):
    filelist = []
    allfilelist = os.listdir(path)
	
    for file in allfilelist:
        filepath = os.path.join(path, file)
        if os.path.isdir(filepath):
            interfl = get_dir(filepath, fileType)
            filelist += interfl
        else:
            if filepath.endswith(fileType):
                print('Found：'+filepath)
                filelist += [filepath]
    
    return filelist


mainpath = sys.argv[1]
outputpath = sys.argv[2]
filelist = get_dir(mainpath,'.mp4')
order = 0
for file in filelist:
    #print(file)
    os.makedirs(outputpath+str(order))
    
    #index = file.split(".")[0].split('-')[0]
    #id = file.split(".")[0].split('-')[1]
    line = "python C:/Users/Reth0N/Desktop/video2pic.py " + file + " " + outputpath + str(order)
    os.system(line)
    order += 1
'''for i, j, k in os.walk(mainpath):
    #print(k)
    

'''