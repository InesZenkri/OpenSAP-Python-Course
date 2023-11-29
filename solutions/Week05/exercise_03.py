def reaction_path(speed):
    return speed*3/10

def brake_distance(speed):
    return (speed/10)**2

def stopping_distance(speed):
    return reaction_path(speed) + brake_distance(speed)

print(stopping_distance(50))