from random import randint, uniform, shuffle
from weapon import Weapon
class Fighter:
    """
    La classe d'un fighter
    """
    def __init__(self, name, description):
        self._name= name
        self._description= description
        self._agility=randint(1,9)
        self._health_points=100
        self._weapon=None
        
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
    
    def get_strength(self):
        return 10-self.get_agility()
    
    def get_weapon(self):
        return self._weapon
    
    
    def punch(self, aFighter):
        """
        punch aFighter
        return the health points of AFighter
        """
        points=int(uniform(0.7,1.0)*10*self.get_strength()/aFighter.get_agility())
        aFighter._health_points=aFighter.get_health_points()-points
        #print(aFighter._health_points)
        return aFighter.get_health_points()
    
    def take_weapon(self, aWeapon):
        weapon=self.get_weapon()
        owner=aWeapon.get_owner
        if weapon:
            weapon._owner=None #on supprime le proprietaire de l'arme actuelle
        self._weapon=aWeapon
        aWeapon._owner=self #on affecte une arme a son proprietaire
            
    
    
    

# Ensuite on va créer deux fighters marcel et maurice




# print(maurice.get_health_points())
# marcel.punch(maurice)
# print(maurice.get_health_points())

# bazooka=Weapon("bazooka",10,1)
# marcel = Fighter("marcel", '') # on affecte dans la variable marcel une instance de la classe Fighter
# maurice = Fighter('maurice', '') # on affecte dans la variable maurice une instance de la classe Fighter
# marcel.set_description('il est le meilleur')
# pistolet=Weapon("pistolet", 2, 10)
# marcel.take_weapon(bazooka)
# maurice.take_weapon(bazooka)
# print(bazooka.get_owner().get_name())
# print(marcel.get_weapon().get_name())
# marcel.take_weapon(pistolet)
# print(bazooka.get_owner())
