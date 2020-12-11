#!/usr/bin/env python3
""" Laboratory work 7. Task 1 """

import os
import copy
from shutil import copyfile


class XMLDocument:
    """
    Prototypical class
    """
    def __init__(self, file):
        self.file = file


class PrototypeFile:
    """
    Prototype class
    """
    def __init__(self):
        self._toBeClonedObjects = {}
        self._new_file = ''

    def registerFile(self, name, file):
        """
        Registers the file to be cloned
        """
        self._toBeClonedObjects[name] = file
        self._new_file = name + '.xml'
    
    def unregisterFile(self, name):
        """
        Deletes the copy of file
        """
        del self._toBeClonedObjects[name]
        os.remove(self._new_file)
        print(self._new_file)


    def clone(self, name):
        """
        Clones the prototypical object
        """
        clonedObject = self._toBeClonedObjects.get(name)
        cloned_file = copyfile(clonedObject.file, self._new_file)
        return cloned_file

if __name__=="__main__":
    defaultDocument = XMLDocument('sample.xml')
    prototype = PrototypeFile()
    prototype.registerFile('Version_1', defaultDocument)
    version_1 = prototype.clone('Version_1')
    prototype.registerFile('Version_2', defaultDocument)
    version_2 = prototype.clone('Version_2')
    prototype.unregisterFile('Version_2')
