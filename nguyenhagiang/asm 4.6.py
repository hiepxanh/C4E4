def  get_even_list(num_list):
    i=0
    for x in num_list:
        if x%2==1:
            del num_list[i]
        i=i+1    
    return num_list

even_list = get_even_list([1, 2, 5, -10, 9, 6])
if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
