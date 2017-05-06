import os
from os import walk

#Gets stats of all files in a given directory
def get_file_stats(dir):
    version_dict = {}
    f = []

    for (rootdir, dirnames, filenames) in walk(dir):
        if not rootdir.startswith(dir + '/.'):
            for fn in filenames:
                path = os.path.join(rootdir, fn)
                stats = os.stat(path)
                print path, oct(stats.st_mode)[4:], stats.st_uid, stats.st_size, 'bytes'


if __name__ == "__main__":
    get_file_stats('.')
