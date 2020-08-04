te = []
 
 for i in c:
     z = ".".join(i.split(".")[:1])
     ia = ".".join(i.split(".")[1:]).lower()
     g = []
     isin = False
     count = 0 
     temp = ""
     for j in range(len(ia)):
         if ia[j] != "[" and ia[j] != "]":
             temp += ia[j]
         elif ia[j] == "[":
             if(not isin):
                 g += [temp]
                 temp = ""
             isin = True
             count += 1
             temp += ia[j]
         elif ia[j] == "]":
             temp += ia[j]
             count -= 1
             if (count <= 0): 
                 isin = False
                 g += [temp]
                 count = 0
                 temp = ""
     m = g[::2]
     temp2 = []
     for j in m:
         b = j
         for za in punctuation:
             b = (za + " ").join(b.split(" " + za + " "))
             b = (za + " ").join(b.split(" " + za))
         b = b.split(" ")
         b.sort()
         temp2 += [" ".join(b).strip()]
         temp2[-1] = (temp2[-1][0].upper()+temp2[-1][1:])
     te = te + [" ".join([z + "."] + two_lists(temp2, g[1::2]))]
 tg = []
 for i in te:
     j = i
     temp = ""
     need = -1
     for k in j:
         need -= 1
         for ell in endpunc:
             if(k == ell):
                 need = 2
         if(need == 0):
             temp += k.upper()
         else:
             temp += k
     tg += [temp]
 with open("newplay.txt","w") as f:
      f.write("\n".join(tg))
