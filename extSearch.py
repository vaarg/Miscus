#!/bin/python

# Searches for unique mentions of files in a plaintext file.
# Searches for these with an inputed <ext>
# E.g.: "python access_log.txt js" -> Searches for unique .js files in an access log.

import os
import re # For regular expressions
import sys

if len(sys.argv) != 3:
    print(f"Usage is {os.path.basename(__file__)} <textfile.txt> <ext>")
    sys.exit()

file_name = sys.argv[1]
ext = sys.argv[2]
file_exists = os.path.exists(file_name)

if file_exists == False:
    print(f"{file_name} doesn't exist!")
else:
    file = open(file_name)
    content = file.read()
    reg_content = re.findall(f'[^/]*\.{ext} ', content)
    uniq_content = list(set(reg_content))
    for i in uniq_content:
        print(i)
