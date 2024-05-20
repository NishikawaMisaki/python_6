import sys
args=sys.argv

myname = args[1]
age = args[2]
catname = args[3]

import introfamily

cat=introfamily.IntroFam(myname, age, catname)

print(cat.name_out())
print(cat.age_out())
print(cat.cat_out())
