#!/usr/bin/python3
""" A python script that adds all arguments to a
    python list, then saves them to a file """


import os
import sys
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


arg_list = []
if os.path.exists("add_item.json"):
    arg_list = load_from_json_file("add_item.json")
args = sys.argv[1:]
for arg in args:
    arg_list.append(arg)
save_to_json_file(arg_list, "add_item.json")
