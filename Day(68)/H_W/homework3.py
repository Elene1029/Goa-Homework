#3 )Draw stairs


def draw_stairs(n):
    stair = ''
    for i in range(0, n-1):
        stair += ' ' * i + 'I\n'
    return stair+' '*(n-1)+'I'