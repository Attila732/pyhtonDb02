import re
text=input("Szám: ")


if(re.match("^[0-9]*$",text)):

    print("ok")
else:
    print("no")    