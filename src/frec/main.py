#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 01:51:48 2026

@author: iancoccimiglio
"""

import os
import shutil

# %% Mode 1, take an object, find the owner

# Owners
# Brew
# Conda
# DMG
#print("Hello World")

def check_name(name: str):
    # Gather info
    pkg_name=shutil.which(name)
    print(pkg_name)
    pkg_list = pkg_name.split("/")
    #print(pkg_list)
    if "homebrew" in pkg_list:
        print(f"{name} is owned by brew")
    else:
        print(f"I don't know who {name} belongs to")
    
check_name("python3")
check_name("uv")
check_name("conda")
check_name("gcc")
