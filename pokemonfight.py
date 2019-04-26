# program

from pokemon import pokemon

p1 = pokemon("Glurak", 50, 136, 130, 185)
p2 = pokemon("Turtok", 50, 135, 152, 186)


def fight(x, y):
    schlag1 = [x.attack - y.defense]
    y.kp = y.kp - list(map(lambda x: 0 if x < 0 else x, schlag1))[0]
    schlag2 = [y.attack - x.defense]
    x.kp = x.kp - list(map(lambda x: 0 if x < 0 else x, schlag2))[0]
    buch = {x.name: x.kp, y.name: y.kp}
    return 
    
print(p1.kp, p2.kp)


# #while True:
#     
#     if p1.kp or p2.kp == 0:
#         print("END OF FIGHT")
        
#         break

pokemon()

