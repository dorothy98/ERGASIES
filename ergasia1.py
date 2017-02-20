given_sentence = raw_input("Dwse thn protash sou: ")
givenlist = given_sentence.split()
lastlist = givenlist[-1]
newlist = list(lastlist)
n = 0
for i in reversed(newlist): 
 if i == '!':
  n+=1
 else:
  break
given_sentence = given_sentence.replace('!','')
given_sentence = given_sentence + "!"*n 
print "H protash pou dothike, mono me ta thaymastika pou vriskontai sto telos, einai h ekshs: " 
print given_sentence
 
