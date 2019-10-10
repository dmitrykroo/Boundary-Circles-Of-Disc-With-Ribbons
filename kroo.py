class XtraLetter:
    def __init__(self, _l, b1, b2):
        self.l = _l
        self.i = b1
        self.o = b2


print('Enter a word in lowercase Latin letters, such that each letter occurs in it exactly twice: ')
string = input()

if string == '':
    print('The number of boundary components is 1')
    exit()

letter_set = list(set(string))
letter_dict = dict(zip(letter_set, [[-1, -1] for k in letter_set]))

for i, letter in enumerate(string):
    if letter_dict[letter][0] == -1:
        letter_dict[letter][0] = i
    elif letter_dict[letter][1] == -1:
        letter_dict[letter][1] = i
    else:
        print('Incorrect string')
        exit()

for z in letter_dict:
    if letter_dict[z][0] * letter_dict[z][1] < 0:
        print('Incorrect string')
        exit()

xtra_string = [XtraLetter(l, False, False) for l in string]

counter = 0

for i, x in enumerate(xtra_string):
    if not x.o:
        begflag = (i == 0)

        begpoint = (x.l, 'o', i)
        point = (x.l, 'o', i)

        xtra_string[point[2]].o = True
        while True:
            nextstop = letter_dict[point[0]][0] if letter_dict[point[0]][0] != point[2] else letter_dict[point[0]][1]

            direction = 1 if nextstop > point[2] else -1
            point = (point[0], point[1], nextstop)

            if point[1] == 'o':
                xtra_string[point[2]].o = True
            else:
                xtra_string[point[2]].i = True

            change = -1 if point[1] == 'i' else 1

            nextindex = point[2] + change * direction
            if begflag and nextindex == len(xtra_string):
                counter += 1
                break

            nextlet = xtra_string[nextindex].l
            nextpos = 'o' if (letter_dict[nextlet][1] == nextindex and change * direction == -1
                or letter_dict[nextlet][0] == nextindex and change * direction == 1) else 'i'

            point = (nextlet, nextpos, nextindex)

            if point[1] == 'o':
                xtra_string[point[2]].o = True
            else:
                xtra_string[point[2]].i = True

            if point == begpoint:
                counter += 1
                break
    if not x.i:
        begpoint = (x.l, 'i', i)
        point = (x.l, 'i', i)

        xtra_string[point[2]].o = True
        while True:
            nextstop = letter_dict[point[0]][0] if letter_dict[point[0]][0] != point[2] else letter_dict[point[0]][1]

            direction = 1 if nextstop > point[2] else -1
            point = (point[0], point[1], nextstop)

            if point[1] == 'o':
                xtra_string[point[2]].o = True
            else:
                xtra_string[point[2]].i = True


            change = -1 if point[1] == 'i' else 1

            nextindex = point[2] + change * direction

            nextlet = xtra_string[nextindex].l
            nextpos = 'o' if (letter_dict[nextlet][1] == nextindex and change * direction == -1
                or letter_dict[nextlet][0] == nextindex and change * direction == 1) else 'i'

            point = (nextlet, nextpos, nextindex)

            if point[1] == 'o':
                xtra_string[point[2]].o = True
            else:
                xtra_string[point[2]].i = True

            if point == begpoint:
                counter += 1
            #    print('')
                break

print('The number of boundary components is {}'.format(counter))
