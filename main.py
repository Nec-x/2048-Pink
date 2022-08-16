# This is where the main movement functions of the board will go. Including the merging
import copy
import random
import copy_helper as ch
score = 0
def win(gb: 'Gameboard') -> bool:
    ''' Checks if 2048 is on the board'''
    for row in gb:
        for cell in row:
            if cell == 2048:
                return True
    return False

def move_left(gb: 'Gameboard') -> 'New Gameboard':
    ''' This function will move the numbers to the left and merge them.'''
    global score
    #Remove all zeros
    new_gb = [[num for num in row if num != 0] for row in gb]
    for row in new_gb:
        for num in range(len(row)):
            if (num + 1) >= len(row): pass
            else:
                if row[num] == row[num+1]:
                    row[num] *= 2
                    score += row[num]
                    row.pop(num+1)

    for row in new_gb:
        while len(row) != 4: row.append(0)

    return new_gb




def move_right(gb: 'Gameboard') -> 'New Gameboard':
    ''' This moves the gameboard to the right'''
    new_gb = copy.deepcopy(gb)
    for row in new_gb: row.reverse()
    new_gb = move_left(new_gb)
    for row in new_gb: row.reverse()
    return new_gb


def transpose(gb: 'Gameboard') -> 'New Gameboard':
    ''' This transposes the gameboard (rows are columns, columns are rows)'''

    new_gb = [[],[],[],[]]
    for col in range(4):
        for row in range(4):
            new_gb[row].append(gb[col][row])
    return new_gb


def move_up(gb: 'Gameboard') -> 'New Gameboard':
    ''' Moves the gameboard up'''

    transposed = transpose(gb)
    transposed = move_left(transposed)
    transposed = transpose(transposed)
    return transposed


def move_down(gb: 'Gameboard') -> 'New Gameboard':
    ''' Moves the gameboard down'''

    transposed = transpose(gb)
    transposed = move_right(transposed)
    transposed = transpose(transposed)
    return transposed


def game_over(gb: 'Gameboard') -> bool:
    ''' Check to see if any more moves can be performed.'''
    zero_check = False

    for row in gb:
        for cell in row:
            if cell == 0: zero_check = True

    if zero_check != True:
        if ch.move_left(gb) == gb:
            if ch.move_down(gb) == gb:
                if ch.move_up(gb) == gb:
                    if ch.move_right(gb) == gb:
                        return True
    return False

def random_token(gb: 'Gameboard') -> "Dict or Bool":
    ''' Picks a random spot and returns a location where a random tile will be placed.'''
    lst = [(count,cell_count) for count, row in enumerate(gb) for cell_count, cell in enumerate(row) if cell == 0]
    if len(lst) == 0: return True
    random_location = random.choice(lst)
    if random.random()*100 < 90:
        num = 2
    else: num = 4
    return {'row': random_location[0], 'cell': random_location[1], 'value': num}

class GB:
    def __init__(self):
        self.gb = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]

    def clear(self):
        self.gb = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]
#left is up, right is down
if __name__ == '__main__':
    gameboard = [[2,3,3,3],
                 [2,2,3,3],
                 [3,4,3,3],
                 [4,4,4,4]]