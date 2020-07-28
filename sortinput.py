//TODO: Kill stage directions (using regex to delete all between brackets)
with open("play.txt","r") as f:
     c = []
     t = f.readline()
     while(t != "000"):
         c += [t]
         t = f.readline()
te = []
for i in c:
     b = ".".join(i.split(".")[1:]).lower().split(" ")
     b.sort()
     b=" ".join([i.split(".")[0]+"."]+b)
     te += [b]
with open("newplay.txt","w") as f:
     f.write("\n".join(te))
