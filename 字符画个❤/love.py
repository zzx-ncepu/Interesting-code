import time

words = input('输入你想说的话：')
for item in words.split():
    letterlist = []
    for y in range(12,-12,-1):
        list_x = []
        letters = ' '
        for x in range(-30,30):
            expression = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
            if expression <= 0:
                letters += item[(x-y)%len(item)]
            else:
                letters += ' '
        list_x.append(letters)
        letterlist += list_x
    print('\n'.join(letterlist))
    time.sleep(1.5)