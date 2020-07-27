#! /usr/bin/env python3
import os
import requests

def main():
    dir = "/data/feedback/"
    url = ""+"/feedback"
    data_keys = ["title","name","date","feedback"]
    for file in os.listdir(dir):
        with open(file) as feedback_file:
            feedback_data = feedback_file.readlines()
            dictionary_containing_data = {}
            count = 0
            for data in feedback_data:
                dictionary_containing_data[data_keys[count]] = data.strip()
                count+=1
            
            response = requests.post(url, data=dictionary_containing_data)
            print(response.request.body)
