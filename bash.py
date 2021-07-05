#!/usr/bin/env python
"""""""""""""""""""""
Simple bash commands
"""""""""""""""""""""
# IMPORTS
import os

# AUTHORINFO
__author__ = "Simon Fransen"
__email___ = "Simon.fransen@student.kdg.be"
__status__ = "Finished"


# FUNCTIONS
def call_update():
    command = "sudo apt update -y"
    os.system(command)
    command = "sudo apt upgrade -y"
    os.system(command)

def install_package():
    package = "read varpack"
    os.system(package)
    command = "sudo apt install $varpack"
    os.system(command)

def call_shutdown():
    command = "sudo shutdown -h now"
    os.system(command)

def show_info():
    command = "uname -a"
    os.system(command)