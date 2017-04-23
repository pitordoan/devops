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

#Configures app-settings.xml with keys/values coming from config.properties and processor file config.xml
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

#Loads a properties file and returns its content as a dictionary
def properties_to_dict(prop_file):
    dict = {}
    with open(prop_file, 'r') as f:
        for line in f:
            line = line.rstrip()
            if "=" not in line: continue
            if line.startswith("#"): continue

            k, v = line.split("=", 1)
            dict[k] = v
    return dict

#Gets available arguments (none private functions in this file)
def __get_available_arguments():
    fset = [obj for name, obj in inspect.getmembers(sys.modules[__name__]) if inspect.isfunction(obj)]
    func_names = []
    for f in fset:
        if not (f.func_name.startswith('__') or f.func_name == 'check_output' or f.func_name == 'main'):
            func_names.append(f.func_name)
    return func_names

#---------------- Main ----------------
def main():
    available_args = __get_available_arguments()

    if len(sys.argv) <= 1:
        print "Usage: devops.py <argument>"
        print "\nAvailable arguments:"
        print "\n".join(available_args)
    else:
        found = False

        for argument in available_args:
            fn_call = sys.argv[1]
            if "(" in fn_call:
                p = fn_call.index("(")
            else:
                p = len(fn_call)
                fn_call = fn_call + "()"

            arg = fn_call[0:p]
            if argument == arg:
                result = eval(fn_call)
                print result
                found = True
                break

        if not found:
            print "Invalid argument: " + sys.argv[1]

if __name__ == "__main__":
    main()