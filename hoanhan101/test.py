def remove_dollar_sign(s):
    s = str(s)
    s_replace = s.replace("$","")
    return s_replace
s = input("Input dollar to replace: ")
print("Result:",remove_dollar_sign(s))

string_with_no_dollar = remove_dollar_sign("80% percent of $life is showing $up")
if string_with_no_dollar == "80% percent of life is showing up":
    print("Your function is correct")
else:
    print("Oops, hoanhan101/test.py:11there's a bug"