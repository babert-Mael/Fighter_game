#from fighter_game.fighter import Fighter
class Weapon:
    def __init__(self, name, damage, ammos):
        self._name=name
        self._damage=damage
        self._ammos=ammos
        self._owner=None
        
    def get_name(self):
        return self._name
    
    def get_damage(self):
        return self._damage
    
    def get_ammos(self):
        return self._ammos
    
    def get_owner(self):
        return self._owner
    

    def shoot(self, aFighter):
        if self.get_ammos()>=1:
            aFighter._health_points=aFighter._health_points-self.get_damage()
            self._ammos=self._ammos-1
            return self.get_damage()
        else:
            return 0
        
    
            
# bazooka=Weapon("bazooka",10,1)
# marcel = Fighter("marcel", '') # on affecte dans la variable marcel une instance de la classe Fighter
# maurice = Fighter('maurice', '') # on affecte dans la variable maurice une instance de la classe Fighter
# 
# bazooka.shoot(maurice)
# print(maurice.get_health_points())
# bazooka.shoot(maurice)
# print(maurice.get_health_points())