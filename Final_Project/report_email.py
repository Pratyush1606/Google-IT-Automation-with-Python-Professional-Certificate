#!/usr/bin/env python3
import os 
from datetime import date
import reports
import emails

def message():
    user = os.path.expanduser("~")
    dir = os.path.join(user,"supplier-data/descriptions/")
    info_fruit = []
    for file in os.listdir(dir):
        with open(dir+file) as filename:
            data = filename.readlines()
            info_fruit.append(("name: "+data[0].strip(),"weight: "+data[1].strip()))

    paragraph = "" #For generating the paragraph of the PDF
    for info in info_fruit:
        paragraph+= info[0]+ "<br/>" + info[1] + "<br/>" + "<br/>"
    return paragraph
if __name__ == "__main__":
    username = "student-01-03addc9c9fb4" #Replace here with the username of the receiver
    filename = "/tmp/processed.pdf"
    today = date.today().strftime("%B %d, %Y")
    title = "Processed Update on "+today
    reports.generate(filename=filename,title=title,additional_info=message())

    sender = "automation@example.com"
    receiver = "{}@example.com".format(username)
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attach_file = filename
    message_ = emails.generate(sender=sender,recipient=receiver,subject=subject,body=body,attachment_path=attach_file)
    emails.send(message=message_)