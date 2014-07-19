#createDirStructure
import os,sys

Primary_root_files = [".htaccess","version.txt","ti.php","index.php","README.md"] 
Primary_root_dirs = ["assets","app","bin","changelog","config","db","docs","log","lib","public","test","tmp"]

#creating a file with the input name in the input dir
def createFile(name,dir_):
    filename = dir_+name
    f = open(filename,'w')
    f.close()

#creating a directory with the input name
def createDir(dir_):
    if not os.path.isdir(dir_):
        os.mkdir(dir_)
    else:
        print "directory already exist"
        exit()

#creating SubFolders in assets
def createAssets(assets):
    subfolders_in_assets_folder_in_app = ["img","text_files","downloads","others"]
    for folder in subfolders_in_assets_folder_in_app:
        createDir(assets+folder)

#Path for the scafold to create        
root = sys.argv[1]
createDir(root)
for item in Primary_root_files:
    createFile(item,root+'/')        

for item in Primary_root_dirs:
    createDir(root+"/"+item)

    
lst1 = ["css","img","js","others"]
for item in lst1:
    createDir(root+"/assets/"+item)


    
lst = ["assets","folder_one","folder_two","folder_n-1","folder_n"]
for item in lst:
    createDir(root+"/app/"+item)
    if item == "assets":
        createAssets(root+"/app/"+item+"/")                    
for item in lst[1:]:
    lst1=["db","assets","others"]
    for key in lst1:
        createDir(root+"/app/"+item+"/"+key)
        if key == "db":
           createFile("access.php",root+"/app/"+item+"/db/")
        elif key == "assets":
            createAssets(root+"/app/"+item+"/assets/")
    lst1 = ["config.php","folder_one.php"]
    for key in lst1:
        createFile(key,root+"/app/"+item+"/")
