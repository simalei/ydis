#!/usr/bin/python3
# Coded by OneParsec
import sys

if sys.platform == 'win32':
    from core.shell_win import *
else:
    from core.shell import *

shell()
