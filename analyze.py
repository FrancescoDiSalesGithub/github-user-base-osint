import sys
import os

if len(sys.argv) != 2:
    print("Usage: python3 analyze.py '/my/dir'")
    sys.exit(1)

directory = sys.argv[1]

formats = ["PNG", "JPG", "GIF"]

for item in os.listdir(directory):
    filepath = os.path.join(directory, item)
    if not os.path.isfile(filepath):
        continue  # Salta cartelle

    try:
        with open(filepath, "rb") as file:
            header = file.read(8) 
            file.seek(0)  

            if header.startswith(b'\x89PNG'):
                ext = ".png"
            elif header.startswith(b'\xFF\xD8'):
                ext = ".jpg"
            elif header.startswith(b'GIF'):
                ext = ".gif"
            else:
                ext = ".unknown"

            print("[+] Analyze file: {}, detected format: {}".format(item,ext))
            with open(filepath + ext, "wb") as binary:
                binary.write(file.read())

    except Exception as e:
        print(f"Error processing {item}: {e}")
