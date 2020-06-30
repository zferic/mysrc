from pyparsing import *
import random
test = ["Hello, World!","Hi, Mom!","Good morning, Miss Crabtree!","Yo, Adrian!","Whattup, G?","How's it goin', Dude?","Hey, Jude!","Goodbye, Mr. Chips!"]
word = Word(alphas+"'.")
salutation = Group(OneOrMore(word))
comma = Suppress(Literal(","))
greetee = Group(OneOrMore(word))
endpunc = oneOf("! ?")
greeting = salutation + comma + greetee + endpunc
salutes = []
greetees = []
for t in test:
    salutation, greetee, endpunc = greeting.parseString(t)
    salutes.append( ( " ".join(salutation), endpunc) )
    greetees.append( " ".join(greetee) )
for i in range(50):
    salute = random.choice( salutes )
    greetee = random.choice( greetees )
    print( salute[0], greetee, salute[1] )
