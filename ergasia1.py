given_sentence = raw_input("Dwse thn protash sou ~> ")
givenlist = given_sentence.split()
t = givenlist[-1].count("!")
given_sentence = given_sentence.replace('!','')
given_sentence = given_sentence + "!"*t
print given_sentence