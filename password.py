import random

#A function do shuffle all thr chracter of a string
def shuffle(string):
    templist = list(string)
    random.shuffle(templist)
    return ''.join(templist)

#Main program starts
uppercaseLetter1 = chr(random.randint(65,90)) 
uppercaseLetter2 = chr(random.randint(65,90))
uppercaseLetter3 = chr(random.randint(65,90))
lowercaseLetter1 = chr(random.randint(97,122))
lowercaseLetter2 = chr(random.randint(97,122))
lowercaseLetter3 = chr(random.randint(97,122))
lowercaseLetter4 = chr(random.randint(97,122))
lowercaseLetter5 = chr(random.randint(97,122))
symbols1 = chr(random.randint(33,47)) 
symbols2 = chr(random.randint(33,47))
 #Generate a random Uppercase letter (based on ASCII)
#Generate more characters here
#...

#Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + \
           lowercaseLetter1 + lowercaseLetter2 + lowercaseLetter3 + \
           lowercaseLetter4 + lowercaseLetter5 + symbols1 + symbols2
          
password = shuffle(password)

#Output
print(password)