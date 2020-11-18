
import os
import random
import shutil
 

XmlPath=r'xml_test'

pictureBasePath=r"Insight-MVT_Annotation_Train"

saveBasePath=r"picture_test"
 
total_xml = os.listdir(XmlPath)
num=len(total_xml)
list=range(num)
if os.path.exists(saveBasePath)==False:
     os.makedirs(saveBasePath)
 
 
for xml in total_xml:
    xml_temp=xml.split("__")
    folder=xml_temp[0]
    filename=xml_temp[1].split(".")[0]+".jpg"
    # print(folder)
    # print(filename)
    temp_pictureBasePath=os.path.join(pictureBasePath,folder)
    filePath=os.path.join(temp_pictureBasePath,filename)
    # print(filePath)
    newfile=xml.split(".")[0]+".jpg"
    newfile_path=os.path.join(saveBasePath,newfile)
    print(newfile_path)
    shutil.copyfile(filePath, newfile_path)
