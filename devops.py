#!/usr/bin/python

import subprocess
import sys
import inspect, signal
import os
import csv
import re
import xml.etree.ElementTree as ET
from subprocess import check_output

#Returns available disk space
def get_avail_disk_space():
    cmd = 'df'
    p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output = p.communicate()[0]
    avail_space = output.split('\n')[1].split()[3]
    return int(int(avail_space.strip()) / 1024) #in MB

#Returns free memory
def get_free_mem():
    cmd = 'free'
    p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output = p.communicate()[0]
    free_mem = output.split('\n')[1].split()[3]
    return int(int(free_mem.strip()) / 1024)  # in MB

#Returns an array of PIDs that their names match process_name
def get_pid(process_name):
    try:
        return map(int, check_output(["pidof", process_name]).split())
    except:
        return []

#Kills processes by name
def kill_process(process_name):
    pids = get_pid(process_name)
    for pid in pids:
        os.kill(pid, signal.SIGKILL)

def configure(conf, processor, dest):
    conf_map = dict([(row[0], row[1]) for row in csv.reader(open(conf, 'r'), delimiter='=')])

    tree = ET.parse(processor)
    root = tree.getroot()
    settings = root.findall('setting')

    dest_tree = ET.parse(dest)
    dest_root = dest_tree.getroot()

    for setting in settings:
        path = setting.attrib.get('path')
        attribute = setting.attrib.get('attribute')
        key = setting.attrib.get('key')

        elements = dest_root.findall(path)
        for ele in elements:
            value = conf_map[key]
            ele.set(attribute, value)

    dest_tree.write(dest, 'utf8')

def replace_variables(dict, text):
    for key, value in dict.items():
        while True:
            t = text.replace('${' + key + '}', value)
            if t == text:
                break
            else:
                text = t
    return text

def main():
    if len(sys.argv) <= 1:
        print "Please provide an argument"
    else:
        fset = [obj for name, obj in inspect.getmembers(sys.modules[__name__]) if inspect.isfunction(obj)]
        found = False

        for f in fset:
            fn_call = sys.argv[1]
            if "(" in fn_call:
                p = fn_call.index("(")
            else:
                p = len(fn_call)
                fn_call = fn_call + "()"

            fn_name = fn_call[0:p]
            if f.func_name == fn_name:
                result = eval(fn_call)
                print result
                found = True
                break

        if not found:
            print "Invalid argument: " + sys.argv[1]

#---------------- Main ----------------
if __name__ == "__main__":
    main()