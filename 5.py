isTrue = False
a =2
b = 2.5
strOne = "One"
strThree = "Three"
my_list = ["1","2"]
is_age_above_24 = (a == 24 or strOne == "one")
is_not_aviran = (strThree != "aviran")

if isTrue and is_age_above_21 and not is_not_aviran:
    print("true and two")
elif is_age_above_24 and b == 2.5:
    print("blabla1")
else:
    print("blabla2")

if len(my_list) > 0:
    print("I have items")
else:
    print("i dont have items")

