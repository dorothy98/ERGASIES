given_sentence = raw_input("Dwse thn protash sou: ")
givenlist = given_sentence.split()
t = givenlist[-1].count("!")
given_sentence = given_sentence.replace('!','')
given_sentence = given_sentence + "!"*t
print "H protash pou dothike, mono me ta thaymastika pou vriskontai sto telos, einai h ekshs: "
print given_sentence
