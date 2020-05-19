ao = open("animals.txt")
an = open("animals_new.txt", "w")
lines = ao.readlines()
lines = [word.rstrip() for word in lines]
an.write(" ".join(lines))
ao.close()
an.close()
