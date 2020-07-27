#!/usr/bin/env python3
from PIL import Image
import os

def main():
    user = os.path.expanduser("~")
    inPath = os.path.join(user,"supplier-data/images/")
    for file in os.listdir(inPath):
        f,e = os.path.splitext(file)
        outfile = f+".jpeg"
        print(f,outfile)
        if file!=outfile:
            try:
                with Image.open(inPath+file) as im:
                    im.resize((600,400)).convert("RGB").save(inPath+outfile,"jpeg")
            except OSError:
                pass
if __name__ == "__main__":
    main()