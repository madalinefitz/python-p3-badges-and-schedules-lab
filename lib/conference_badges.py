import ipdb
def badge_maker(name):
    return(f"Hello, my name is {name}.")

def batch_badge_creator(names):
    badges=[]
    for name in names:
        badges_string = (f"Hello, my name is {name}.")
        badges.append(badges_string)
    return badges
        

def assign_rooms(names):
    rooms=[]
    for name in names:
        rooms_message=(f"Hello, {name}! You'll be assigned to room {names.index(name) + 1}!")
        rooms.append(rooms_message)
    return rooms



def printer(names):
    for message in batch_badge_creator(names):
        print(message)
    for message in assign_rooms(names):
        print(message)
    
