#1.
import re
def check(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)
str=input() #gdg27ASF
print(check(str)) #true

#2.
import re
def match(text):

        if re.search('\w*ab.\w*',  text):
                return 'matched'
        else:
                return('Not matched!')
str1=input()#jfoioje234
print(match(str1)) #Not matched!

#3.
def num_check(string):
      if re.search(r'\d+$', string):
           return 'yes'
      else:
          return'NO!'
str2=input()
print(num_check(str2))

#4.
import re
str3=input() #print 1,2,45,645,334 and 45
results = re.finditer(r"([0-9]{1,3})", str3)
for n in results:
     print(n.group(0)) #1
                       # 2
                       # 345
                       # 3
                       # 56
                       # 5

#5.
import re
def text_match(text):
        patterns = '^[A-Z]*$'
        if re.search(patterns,  text):
                return 'matched!'
        else:
                return('Not matched!')

str4=input() #ASDFGDG
print(text_match(str4)) #matched!





