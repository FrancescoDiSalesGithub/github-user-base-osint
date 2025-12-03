import requests
import sys

def write_bmp(directory,index):
    with open (directory+str(index)+".bmp","wb") as file_png:
        file_png.write(picture.content)


def write_jpg(directory,index):
    with open (directory+str(index)+".jpg","wb") as file_png:
        file_png.write(picture.content)


def write_png(directory,index):
    with open (directory+str(index)+".png","wb") as file_png:
        file_png.write(picture.content)


def write_gif(directory,index):
    with open (directory+str(index)+".gif","wb") as file_png:
        file_png.write(picture.content)

def write_webp(directory,index):
    with open (directory+str(index)+".webp","wb") as file_png:
        file_png.write(picture.content)

def write_svg(directory,index):
    with open (directory+str(index)+".svg","wb") as file_png:
        file_png.write(picture.content)

functions_dictionary = {
    "image/png":write_png,
    "image/bmp":write_bmp,
    "image/jpg":write_jpg,
    "image/gif":write_gif,
    "image/webp":write_webp,
    "image/svg+xml":write_svg
}    



if len(sys.argv) != 4:
    print("python3 download-range.py '/my/dir' 1000 2000")
else:

    target_dir = sys.argv[1]
    number_of_users = sys.argv[2]
    number_of_users_end = sys.argv[3]

    if(number_of_users > number_of_users_end):
        print("the range is invalid please check your arguments")
        print("python3 download.py '/my/dir' 1000 2000")
        exit(-1)

    for i in range(int(number_of_users),int(number_of_users_end)):

        try:
            print("[+] - downloading user id: {}".format(i));
            picture = requests.get("https://avatars.githubusercontent.com/u/{}?v=4".format(i))

            content_type=picture.headers.get("Content-Type");

            if content_type in functions_dictionary:
                functions_dictionary[content_type](target_dir,i)
            else:
                write_jpg(target_dir,i)

        except Exception as e:
            print(e)
   
