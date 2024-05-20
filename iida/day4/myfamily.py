from Introfamily import IntroFam
import sys
args = sys.argv

fam = IntroFam(args[1], args[2], args[3])
print(fam.name_out())
print(fam.age_out())
print(fam.cat_out())