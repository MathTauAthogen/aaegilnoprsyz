 //TODO: Kill stage directions (using regex to delete all between brackets)
 c = []
 t = raw_input()
 while(t != "000"):
     c += [t] 
     t = raw_input()
 te = []
 for i in c:
     b = ".".join(i.split(".")[1:]).lower().split(" ")
     b.sort()
     b=" ".join([i.split(".")[0]+"."]+b)
     te += [b] 
 print("\n".join(te))
