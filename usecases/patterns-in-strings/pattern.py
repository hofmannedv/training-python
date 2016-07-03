# -----------------------------------------------------------
# find number patterns in strings
#o
# (C) 2016 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------
#

# use the regex module
import re

text1 = "this is contract 14556-658, London, postcode SE30AF"
text2 = "computer 2345-56, value EUR 255.18"

# digits with a hyphen
pattern1 = re.compile('\d+-\d+')

# single pattern
m = pattern1.match('123-456')
print (m.group())

# detect all patterns
m = pattern1.findall('123-456 789-012')
print (m)

# detect pattern in text
m = pattern1.findall(text1)
print (m)

# postcode pattern
pattern2 = re.compile('[A-Z]+\d+[A-Z]+')
print (pattern2.findall(text1))

# float pattern
pattern3 = re.compile('\d+\.\d+')
print (pattern3.findall(text2))
