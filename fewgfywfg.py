import re
string=input()
if(re.match(r"(?=.[A-Z])(?=.[-@$])(?=.*[0-9])[a-zA-Z0-9_@$]{8,}",str)):
    print("Valid string")
else:
    print("Invalid string")
     