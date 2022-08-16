import copy
import random
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