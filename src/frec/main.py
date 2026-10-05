#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 12:50:50 2026

@author: iancoccimiglio
"""

# What is a package manager?
# A utility which can install, update, delete, and manage a package.

PACKAGE_MANAGERS = []


RK_OSX = ["mac_receipts", "app_store"]
RK_LINUX = ["dpkg", "rpm", "pacman", "apk"]
RK_XPLATFORM = ["brew", "macports", "nix", "flatpak", "snap"]

RECORD_KEEPERS = [RK_OSX, RK_LINUX, RK_XPLATFORM]