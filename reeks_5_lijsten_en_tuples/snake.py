def beweeg(coord, richting):
    pos_x, pos_y = coord
    match richting:
        case '>':
            pos_x += 1
        case '<':
            pos_x -= 1
        case '^':
            pos_y += 1
        case 'v':
            pos_y -= 1
        case _:
            return ValueError(f'Foutieve ingave: {richting}')
    return pos_x, pos_y

def teruggekeerd(richting_lijst):
    r1, r2 = richting_lijst
    match r1:
        case '>':
            return r2 == '<'
        case '<':
            return r2 == '>'
        case '^':
            return r2 == 'v'
        case 'v':
            return r2 == '^'
    return False    

def laatste_levende_positie(richting_lijst):
    is_teruggekeerd = False
    coord = (0,0)
    i = 0
    aantal = 0
    while not is_teruggekeerd and i < len(richting_lijst):
        laatst = coord
        coord = beweeg(coord, richting_lijst[i])
        if i != 0:
            is_teruggekeerd = teruggekeerd([richting_lijst[i], richting_lijst[i-1]])
        if is_teruggekeerd == False:
            aantal += 1
        else:
            coord = laatst
        i += 1
    return aantal, coord[0], coord[1]

print(laatste_levende_positie(['>', '<', '^']))
print(laatste_levende_positie(['v', '>', 'v', '<', '^', '^']))