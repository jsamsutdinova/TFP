class LeafElement: 

	'''Class representing objects at the bottom or Leaf of the hierarchy tree.'''

	def __init__(self, *args): 

		''''Takes the first positional argument and assigns to member variable "position".'''
		self.position = args[0] 

	def showDetails(self): 

		'''Prints the position of the child element.'''
		print("\t", end ="") 
		print(self.position) 


class CompositeElement: 

	'''Class representing objects at any level of the hierarchy 
	tree except for the bottom or leaf level. Maintains the child 
	objects by adding and removing them from the tree structure.'''

	def __init__(self, *args): 

		'''Takes the first positional argument and assigns to member 
		variable "position". Initializes a list of children elements.'''
		self.position = args[0] 
		self.children = [] 

	def add(self, child): 

		'''Adds the supplied child element to the list of children 
		elements "children".'''
		self.children.append(child) 

	def remove(self, child): 

		'''Removes the supplied child element from the list of 
		children elements "children".'''
		self.children.remove(child) 

	def showDetails(self): 

		'''Prints the details of the component element first. Then, 
		iterates over each of its children, prints their details by 
		calling their showDetails() method.'''	
		print(self.position) 
		for child in self.children: 
			print("\t", end ="") 
			child.showDetails() 


"""main method"""

if __name__ == "__main__":
    army = CompositeElement("Армия")
    army_elves = CompositeElement("Отряд эльфов")
    army_orcs = CompositeElement("Отряд орков")
    army_minotaurs = CompositeElement("Отряд минотавров")
    army_centaurs = CompositeElement("Отряд кентавров")
    army_cyclops = CompositeElement("Отряд циклопов")
    army_hydras = CompositeElement("Отряд гидр")
    army_dragons = CompositeElement("Отряд драконов")
    army_knights = CompositeElement("Отряд рыцарей")
    _army_elves = LeafElement("Поддотряд эльфов")
    _army_orcs = LeafElement("Поддотряд орков")
    _army_minotaurs = LeafElement("Поддотряд минотавров")
    _army_centaurs = LeafElement("Поддотряд кентавров")
    _army_cyclops = LeafElement("Поддотряд циклопов")
    _army_hydras = LeafElement("Поддотряд гидр")
    _army_dragons = LeafElement("Поддотряд драконов")
    _army_knights = LeafElement("Поддотряд рыцарей")
    minotaur = LeafElement("Минотавр")
    cyclop = LeafElement("Циклоп")
    dragon = LeafElement("Дракон")
    knight = LeafElement("Рыцарь")
    _minotaur = CompositeElement("Минотавр")
    _cyclop = CompositeElement("Циклоп")
    _dragon = CompositeElement("Дракон")

    army.add(_minotaur)
    army.add(_cyclop)
    army.add(_dragon)
    army.add(army_elves)
    army.add(army_orcs)
    army.add(army_minotaurs)
    army.add(army_centaurs)
    army.add(army_cyclops)
    army.add(army_hydras)
    army.add(army_dragons)
    army.add(army_knights)
    army_cyclops.add(cyclop)
    army_centaurs.add(_army_centaurs)
    army_cyclops.add(_army_cyclops)
    army_cyclops.add(cyclop)
    army_cyclops.add(cyclop)
    army_dragons.add(_army_dragons)
    army_dragons.add(dragon)
    army_elves.add(_army_elves)
    army_hydras.add(_army_hydras)
    army_hydras.add(_army_hydras)
    army_knights.add(_army_knights)
    army_knights.add(knight)
    army_knights.add(knight)
    army_minotaurs.add(_army_minotaurs)
    army_minotaurs.add(minotaur)
    army_orcs.add(_army_orcs)

    army.showDetails()
	