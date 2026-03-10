import os
import shutil

def dirfound(dir_name):
    if(os.path.exists(dir_name)):
        return True  
    else:
        return False

def movefiles(old_path,dir_name,file_name):
    if dirfound(dir_name):
        shutil.move(old_path,dir_name+"/"+file_name)

    else:
        os.mkdir(dir_name)
        shutil.move(old_path,dir_name+"/"+file_name)

def getdir(pdir):
    if dirfound(pdir):
        for files in os.listdir(pdir):
            file_analysis(path=pdir,file=files)

    else:
        print("Directory are not founded.")

def file_analysis(path,file):

    if file.endswith(".pdf") or file.endswith(".doc") or file.endswith(".txt") or file.endswith(".odt") or file.endswith(".rtf"):
        dir_name="Documents"
        movefiles(path+"/"+file,dir_name,file)

    elif file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".gif") or file.endswith(".bmp") or file.endswith(".svg") or file.endswith(".heic"):
        dir_name="images"
        movefiles(path+"/"+file,dir_name,file)

    elif file.endswith(".mp3") or file.endswith(".mp4") or file.endswith(".wav") or file.endswith(".acc") or file.endswith(".flac") or file.endswith(".m4a") :
        dir_name="videos"
        movefiles(path+"/"+file,dir_name,file)
        
    elif file.endswith(".xls") or file.endswith(".xlsx") or file.endswith(".csv") or file.endswith(".ods"):
        dir_name="spreadsheet"
        movefiles(path+"/"+file,dir_name,file)
        
    elif file.endswith(".zip") or file.endswith(".rar") or file.endswith(".7z") or file.endswith(".tar") :
        dir_name="compress"
        movefiles(path+"/"+file,dir_name,file)
        
    elif file.endswith(".exe") or file.endswith(".msi") or file.endswith(".bin") or file.endswith(".apk"):
        dir_name="program files"
        movefiles(path+"/"+file,dir_name,file)

    elif file.endswith(".html") or file.endswith(".htm") or file.endswith(".css") or file.endswith(".js") :
        dir_name="web"
        movefiles(path+"/"+file,dir_name,file)

    else:
        print(file,"File type not in execution.")

def main():
    dir_name=input("Enter a Directory: ")
    getdir(dir_name)
    print("process completed...")

if __name__=="__main__":
    main()



        