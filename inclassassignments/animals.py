legs = input('Does it have legs [y/n]: ')


if legs =='n':
    live = input('Does it live on land [y/n]: ')
    if live == 'y':
        print("It's a snake!")
    else:
        print("It's a shark!")
else:
    fluffy = input('Is it fluffy [y/n]: ')
    if fluffy == 'y':
        print("It's a cat!")
    else:
        print("It's a gator!")