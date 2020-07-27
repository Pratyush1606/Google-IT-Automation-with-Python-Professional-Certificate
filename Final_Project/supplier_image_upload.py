#!/usr/bin/env python3
import requests
import os

def main():
    user = os.path.expanduser("~")
    inPath = os.path.join(user,"supplier-data/images/")
    url = "http://34.69.229.201/upload/" #Replace the url here
    for file in os.listdir(inPath):
        f,e = os.path.splitext(file)
        outFile = f+".jpeg"
        if outFile==file:
            with open(inPath+file,'rb') as opened:
                r = requests.post(url,files={"file":opened})

if __name__=="__main__":
    main()
