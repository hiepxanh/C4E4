
def remove_dollar_sign(s):
    s = str(s)
    s_replace = s.replace("$", "")
    return s_replace
remove_dollar_sign("$80% percent of $life is showing $up")
string_with_no_dollars = remove_dollar_sign("$80% percent of $life is showing $up")
if string_with_no_dollars == "80% percent of life is showing up":
    print("Your funtion is correct")
    print(string_with_no_dollars)
    print ("^_^")
else:
    print("Oops, there's a bug")
   

##
#### 2
def get_even_list(l):

    for num in l[:]:
        if num%2 != 0:
            l.remove(num)
    return(l)
l = [1,4,5,-1,10]
print(get_even_list(l))

even_list = get_even_list([1, 2, 5, -10, 9, 6])
if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Oops, bugs detected")
