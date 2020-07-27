#!/usr/bin/env python3

import os
from PIL import Image

def main():
        inPath = os.getcwd()
        outPath = r"/opt/icons/"
        for file in os.listdir(inPath):
                f,e = os.path.splitext(file)
                if file!=outfile:
                        try:
                                with Image.open(file) as im:
                                        im.rotate(270).resize((128,128)).convert("RGB").save(outPath+f,"jpeg")
                        except OSError:
                            pass
if __name__ == "__main__":
    main()
