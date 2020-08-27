# -*- coding: utf-8 -*-
"""
Python on LAN
"""

import win32wnet
from win32netcon import RESOURCETYPE_DISK as disk

drive_letter = "R:"
path = ""

win32wnet.WNetAddConnection2(disk , drive_letter , path)

