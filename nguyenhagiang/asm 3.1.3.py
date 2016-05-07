color_list = ['Blue', 'Red', 'Black', 'Pink', 'Brown', 'Yellow']
c=input('What is your favourite color? ')
x=str(c)
for c in color_list:
    if c==str.format(x):
        print('Your color is at index',color_list.index(str(x)),'in my list')
else: print('Sorry, could not find your color')
