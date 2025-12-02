import requests
import sys


if len(sys.argv) != 3:
    print("python3 download.py '/my/dir' 1000")
else:

    target_dir = sys.argv[1]
    number_of_users = sys.argv[2]


    for i in range(1,int(number_of_users)):
        try:
            print("[+] - downloading user id: {}".format(i));
            picture = requests.get("https://avatars.githubusercontent.com/u/{}?v=4".format(i))
            with open(str(target_dir+str(i)),"wb") as file:
                file.write(picture.content)
        except Exception as e:
            print(e)
