color_list = ['Blue', 'Red', 'Black', 'Pink', 'Brown', 'Yellow']
n = input('what is your favorite color?:')
x = str(n)
for n in color_list:
    if n == str.format(x):
        print('your color is at index',color_list.index(str(x)),'in my list')
if x not in color_list:
    print('sorry, i could not find your color')

