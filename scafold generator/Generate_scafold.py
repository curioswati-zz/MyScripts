''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''The script is a project scafold generator.
It creates all the neccesary files and subdirectories.'''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
root = sys.argv[1]
Primary_root_files = [".htaccess","version.txt","ti.php","index.php","README.md"] 
Primary_root_dirs = ["assets","app","bin","changelog","config","db","docs","log","lib","public","test","tmp"]
primary_assets = ["css","img","js","others"]
app_sub_dirs = ["assets","folder_one","folder_two","folder_n-1","folder_n"]
folders_in_app_sub_dirs = ["db","assets","others"]
files_in_app_sub_dirs = ["config.php","folder_one.php"]

''''''''''''''''''''''''''''''''''''''''''''
'''Required Modules'''
''''''''''''''''''''''''''''''''''''''''''''
import os,sys

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''creating a file with the input name in the input dir'''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def createFile(name,dir_):
    filename = dir_+name
    f = open(filename,'w')
    f.close()

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''creating a directory with the input name.
Also checks if the directory already exist or not.'''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def createDir(dir_):
    if not os.path.isdir(dir_):
        os.mkdir(dir_)
    else:
        print "directory already exist"
        exit()

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''creating SubFolders in assets.
The list inside contains the names of subfolders in_ ssets'''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def createAssets(assets):
    subfolders_in_assets_folder_in_app = ["img","text_files","downloads","others"]
    for folder in subfolders_in_assets_folder_in_app:
        createDir(assets+folder)


'''Main Modules'''
def main():
    createDir(root)
    for item in Primary_root_files:                                       #Creating the files in the root directory.
        createFile(item,root+'/')
        
    for item in Primary_root_dirs:                                        #Creating the subdirectories in the root directory.
        createDir(root+"/"+item)
          
    for item in primary_assets:                                           #Creating Primary assets.
        createDir(root+"/assets/"+item)

    for item in app_sub_dirs:                                             #Creating subdirs in app directory under root.
        createDir(root+"/app/"+item)
        if item == "assets":
            createAssets(root+"/app/"+item+"/")                           #Creating secondary assets in assets under app.
            
    for item in app_sub_dirs[1:]:                                         #excluding the assets.
        
        for key in folders_in_app_sub_dirs:                               #Creating subfolders in sub_dirs_of_app.
            createDir(root+"/app/"+item+"/"+key)
            if key == "db":
               createFile("access.php",root+"/app/"+item+"/db/")
            elif key == "assets":
                createAssets(root+"/app/"+item+"/assets/")                #Creating secondary assets.
                
        for key in files_in_app_sub_dirs:                                 #Creating files in sub_dirs_of_app.
            createFile(key,root+"/app/"+item+"/")
            
if __name__ == main():
    main()
