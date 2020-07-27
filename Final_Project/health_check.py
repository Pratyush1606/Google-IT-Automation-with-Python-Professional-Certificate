#!/usr/bin/env python3
import psutil
import shutil
import socket
import emails

def check_cpu_usage():
    percent = psutil.cpu_percent(1)
    return pecent>80

def available_disk(disk):
    du = shutil.disk_usage(disk)
    percent = (du.free*100)/du.total
    return percent<20

def available_memory():
    mem = psutil.virtual_memory()
    available_mb = mem.available/(1024.0**2)
    return available_mb < 500

def localhost_resolved():
    return socket.gethostbyname(socket.gethostname) != "127.0.0.1"

def send_warning(subject):
    username = "student-01-03addc9c9fb4"
    sender = "automation@example.com"
    receiver = "{}@example.com".format(username)
    body = "Please check your system and resolve the issue as soon as possible."
    message_ = emails.generate(sender=sender,recipient=receiver,subject=subject,body=body)
    emails.send(message=message_)

if __name__ =="__main__":
    if(check_cpu_usage):
        subject = "Error - CPU usage is over 80%"
        send_warning(subject)
    if(available_disk("/")):
        subject = "Error - Available disk space is less than 20%"
        send_warning(subject)
    if(available_memory):
        subject = "Error - Available memory is less than 500MB"
        send_warning(subject)
    if(localhost_resolved):
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
        send_warning(subject)

