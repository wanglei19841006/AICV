import os
path ='H:\ImageNet\Images\temp'#\ILSVRC2013_DET_test'

#fout =open('H:\\ImageNet\\Images\\temp3.txt','w')
#for root,dirs,files in os.walk(path):
#    for filepath in files:
#        pathname=os.path.join(root,filepath)
#        print(os.path.join(root,filepath))
#        fout.write(pathname+'\n')
#
#fout.close()

#----------------------------------------------------  
#fout = open('H:\\ImageNet\\Images\\temp3.txt','w')
#dirs = os.listdir(path)
#for dir in dirs:
#    print dir
#    fout.write(dir+'\n')
#fout.close()

#----------------------------------------------------
path ='H:\\ImageNet\\Images\\temp'
print path
list_name=[]
listdir(path, list_name)
def listdir(path, list_name):  
    print path
    for file in os.listdir(path):  
        print file
        file_path = os.path.join(path, file)  
        if os.path.isdir(file_path):  
            listdir(file_path, list_name)  
        elif os.path.splitext(file_path)[1]=='.JPEG':  
            list_name.append(file_path)
            print file_path
            
fout =open('H:\\ImageNet\\Images\\temp\\temp1.txt','w') 
for it in range(len(list_name)):
    fout.write(list_name[it]+'\n')
fout.close()          