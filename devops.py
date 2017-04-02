#!/usr/bin/python

import subprocess

def getDiskUsage():
    cmd = 'df -h'
    p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output = p.communicate()[0]
    availSpace = output.split('\n')[1].split()[3]

    return availSpace

print getDiskUsage()

