from my_queue import Queue
from fighter import Fighter
from time import sleep
from random import shuffle
def fight(attacker, victim, a=0):
    """
    lance un combat entre 2 joueurs
    retourne le joueur gagnant
    """
    
    print(f"{attacker.get_name()} attaque {victim.get_name()}")
    attacker.punch(victim)
    if victim._health_points>0: #cas général
        sleep(0.5)
        return fight(victim, attacker)
    else: #condition d'arret
        print(f"{attacker.get_name()} a gangé le combat")
        sleep(1)
        return attacker

def do_tournament(fighters):
    """
    Créer un trounoi et retourne le survivant
    """
    q_fighters=Queue()
    for p in fighters:
        q_fighters.enqueue(p)
    while q_fighters.size()!=1:
        fighter1=q_fighters.dequeue()
        fighter2=q_fighters.dequeue()
        q_fighters.enqueue(fight(fighter2,fighter1))
        print("combat suivant")
        
    return f"{q_fighters.dequeue().get_name()} a gagné le tounoi!!!!"
        


fighters_name=['Jean-Pierre', 'Jean', 'Michel', 'Jean-Batiste', 'Marise', 'Marie', 'Rachel', 'Odette']
shuffle(fighters_name)
fighters=[Fighter(name,'') for name in fighters_name]
        
# maurice=Fighter("maurice", "")
# jean=Fighter("jean", "")
# gagnant=fight(maurice, jean)
# print(f"{gagnant.get_name()} a gagné")
gagnant=do_tournament(fighters)
print(gagnant)