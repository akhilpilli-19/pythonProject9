import re
txt = "Use of pythom in Machine Learning"
x = re.search("^Use.*Learning", txt)
if (x) :
    print("yes! we have a match!")
else:
    print("no match")