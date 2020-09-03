##Create a range with decimal increment

def newRange(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step
        
x = newRange(0, 5, 0.2)
next(x)


##Chercher les occcurences des lettres dans un fichier, par block


