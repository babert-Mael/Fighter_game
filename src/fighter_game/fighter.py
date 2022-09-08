from random import randint
class Fighter:
    """
    La classe d'un fighter
    """
    def __init__(self, name, description):
        self._name= name
        self._description= description
        self._agility=randint(1,9)
        self._health_points=100
        
    def get_name(self):
        return self._name

    def get_description(self):
        return self._description
    
    def set_description(self, desc):
        self._description=desc

    def get_agility(self):
        return self._agility

    def get_health_points(self):
        return self._health_points
    
    def get_strenght(self):
        return 10-self.get_agility()
    
    def punch(self, aFighter):
        """
        punch aFighter
        return the health points of AFighter
        """
        points=int(uniform(0.7,1.0)*10*self.get_strength()/aFighter.get_agility())
        aFighter._health_points=aFighter.get_health_points()-points
        print(aFighter._health_points)
        return aFighter.get_health_points()
    

# Ensuite on va créer deux fighters marcel et maurice

marcel = Fighter("marcel", '') # on affecte dans la variable marcel une instance de la classe Fighter
maurice = Fighter('maurice', '') # on affecte dans la variable maurice une instance de la classe Fighter
print(marcel.get_name())
marcel.set_description('il est le meilleur')
print(marcel.get_agility())
print(marcel.get_strenght())