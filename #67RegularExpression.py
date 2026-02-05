#67 Python Regular Expression
import re
txt = "The rain in Spain"
pattern1 = "[a-n]"
a = re.findall(pattern1,txt)
print(a)
b = re.findall("[a-z]",txt)
print(b)
