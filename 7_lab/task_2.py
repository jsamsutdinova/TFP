#!/usr/bin/env python3
""" Laboratory work 7. Task 2 """

from abc import ABC, abstractmethod


class Component(ABC):
    """
    Interface for objects in the disk system
    """
    @abstractmethod
    def showDetails(self):
        pass


class ChildElement: 
	def __init__(self, *args): 
		self.position = args[0] 

	def showDetails(self): 
		print("\t", end ="") 
		print(self.position) 


class ParentElement: 
	def __init__(self, *args): 
		self.position = args[0] 
		self.children = [] 

	def add(self, child): 
		self.children.append(child) 

	def remove(self, child): 
		self.children.remove(child) 

	def showDetails(self): 
		print(self.position) 
		for child in self.children: 
			print("\t", end ="") 
			child.showDetails() 


if __name__ == "__main__":
    main_folder = ParentElement("Disk C") 

    programs = ParentElement("Programs") 
    program_1 = ChildElement("Chrome") 
    program_2 = ChildElement("Visual Studio Code") 
    program_3 = ChildElement("Microsoft Teams")
    programs.add(program_1)
    programs.add(program_2)
    programs.add(program_3)
    main_folder.add(programs)

    documents = ParentElement("Documents")
    lab = ParentElement("Laboratory Work")
    file_1 = ChildElement("Lab_1.odt")
    file_2 = ChildElement("Lab_2.odt")
    file_3 = ChildElement("Lab_3.odt")
    file_5 = ChildElement("Book.pdf")
    lab.add(file_1)
    lab.add(file_2)
    lab.add(file_3)
    documents.add(file_5)
    documents.add(lab)
    main_folder.add(documents)
    main_folder.showDetails() 
