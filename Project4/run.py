#! /usr/bin/env python3
import os
import requests

def main():
    user = os.path.expanduser("~")
    dir = os.path.join(user,"supplier-data/descriptions/")
    dir_images = os.path.join(user,"supplier-data/images/")
    url = "http://34.69.229.201/fruits/"
    data_keys = ["name","weight","description"]
    for file in os.listdir(dir):
        with open(dir+file) as feedback_file:
            #print(file)
            feedback_data = feedback_file.readlines()
            dictionary_containing_data = {}
            description = ""
            for i in range(2,len(feedback_data)):
                description=description+feedback_data[i].strip('\n').replace(u'\xa0',u'')
                        
            dictionary_containing_data["name"] = dfeedback_dataata[0].strip()
            dictionary_containing_data["weight"] = int(feedback_data[1].strip().split(" ")[0])
            dictionary_containing_data["description"] = description
            dictionary_containing_data["image_name"] = dir_images+file.strip(".txt")+".jpeg"
            #print(dictionary_containing_data)
            
            response = requests.post(url, json=dictionary_containing_data)
if __name__ == "__main__":
    main()
