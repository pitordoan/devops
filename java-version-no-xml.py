import os
import json
from sets import Set
from os import walk

#Gets java versions used in maven projects under directory mvn_project_dir
def get_java_versions(mvn_project_dir):
    version_dict = {}
    f = []

    for (rootdir, dirnames, filenames) in walk(mvn_project_dir):
        if not rootdir.startswith(mvn_project_dir + '/.'):
            for fn in filenames:
                if fn == 'pom.xml':
                    version_set = set()

                    path = os.path.join(rootdir, fn)
                    with open(path, 'r') as f:
                        for line in f:
                            if line.find('<javaVersion>') >= 0:
                                p = line.find('>')
                                q = line.find('</')
                                version = line[p + 1:q]
                                version_set.add(version)

                    key = os.path.basename(rootdir)
                    version_dict[key] = list(version_set)

    return version_dict

#Set java version (new_java_ver) for all maven projects under directory mvn_project_dir
def set_java_version(mvn_project_dir, new_java_ver):
    for (rootdir, dirnames, filenames) in walk(mvn_project_dir):
        if not rootdir.startswith(mvn_project_dir + '/.'):
            for fn in filenames:
                if fn == 'pom.xml':
                    lines = []

                    path = os.path.join(rootdir, fn)
                    with open(path, 'r+') as f:
                        for line in f:
                            if line.find('<javaVersion>') >= 0:
                                p = line.find('>')
                                q = line.find('</')
                                version = line[p + 1:q]
                                line = line.replace(version, new_java_ver)
                                lines.append(line)
                            else:
                                lines.append(line)

                        f.seek(0)
                        f.truncate()
                        f.write(''.join(lines))


if __name__ == "__main__":
    java_versions = get_java_versions('./maven-project')
    print json.dumps(java_versions, ensure_ascii=False)
    #output: {"maven-project": ["1.7", "1.8"], "moduleC": ["1.5", "1.6"], "moduleB": ["1.7", "1.8"], "moduleA": ["1.6"]}

    set_java_version('./maven-project', '1.9')
