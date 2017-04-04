#!/usr/bin/python

import subprocess
import sys
import inspect

def get_disk_usage():
    cmd = 'df'
    p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output = p.communicate()[0]
    availSpace = output.split('\n')[1].split()[3]
    return int(int(availSpace.strip()) / 1024) #in MB

def main():
    if len(sys.argv) <= 1:
        print "Please provide an argument"
    else:
        fset = [obj for name, obj in inspect.getmembers(sys.modules[__name__]) if inspect.isfunction(obj)]
        found = False

        for f in fset:
            if f.func_name == sys.argv[1]:
                fn = f.func_name + "()"
                result = eval(fn)
                print result

                found = True
                break

        if not found:
            print "Invalid argument: " + sys.argv[1]

#---------------- Main ----------------
if __name__ == "__main__":
    main()