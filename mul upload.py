import os
import requests

def count(dir_path):
    count=0
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            count+=1
    return count

dir_path='F:\\WEB DEVELOPMENT\\media\\upload'

def upload_files(files,post_url):
    try:
        response=requests.post(post_url,files)
        print("file uploaded sucessfully")
        print(response.text)

        return 1
    except:
        print("an error occoured")
        return -1      

def main(dir_path):
    print("We have found a total of ",count(dir_path),"files in the folder")
    item_count=count(dir_path)
    suss=0
    post_url="https://httpbin.org/post"
    i=0
    for path in os.listdir(dir_path):
        i+=1
        if os.path.isfile(os.path.join(dir_path, path)):
                files={i:open(os.path.join(dir_path, path),"r")}
                suss+=upload_files(files, post_url)
    print("Out of ",item_count,", successfully uploded ",suss)

if __name__=='__main__':
    dir_path=r'F:\\WEB DEVELOPMENT\\media\\upload'
    main(dir_path)