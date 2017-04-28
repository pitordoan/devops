#!/usr/bin/python

#This script is used to get Java versions used in the pom.xml files of projects in maven-project directory.

import os
import xml.etree.ElementTree as ET
import json
from os import walk
from sets import Set

#Gets xml elements by tag name
def __get_xml_elements(xml_file_name, tag):
    tree = ET.parse(xml_file_name)
    root = tree.getroot()
    nodes = []

    def get_node(node, tag):
        for el in node.getchildren():
            get_node(el, tag)
        if node.tag.endswith('}' + tag):
            nodes.append(node)

    get_node(root, tag)
    return nodes

#Sets text of xml elements by tag name
def __set_xml_elements_text(xml_file_name, tag, text):
    tree = ET.parse(xml_file_name)
    root = tree.getroot()
    nodes = []

    def get_node(node, tag):
        for el in node.getchildren():
            get_node(el, tag)
        if node.tag.endswith('}' + tag):
            nodes.append(node)

    get_node(root, tag)
    for node in nodes:
        node.text = text

    tree.write(xml_file_name, 'utf8')

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
                    ver_elements = __get_xml_elements(path, 'javaVersion')

                    for ele in ver_elements:
                        version = ele.text
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
                    path = os.path.join(rootdir, fn)
                    __set_xml_elements_text(path, 'javaVersion', new_java_ver)

if __name__ == "__main__":
    java_versions = get_java_versions('./maven-project')
    print json.dumps(java_versions, ensure_ascii=False)
    #output: {"maven-project": ["1.7", "1.8"], "moduleC": ["1.5", "1.6"], "moduleB": ["1.7", "1.8"], "moduleA": ["1.6"]}

    set_java_version('./maven-project', '1.9')