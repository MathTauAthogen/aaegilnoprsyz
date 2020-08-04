#TODO: Add comments
#This is a file for the "Organize Plays" MathCamp event.

#Helper functions I may or may not have stolen from the web.

def removeDuplicates(aList): #Sorted List Required
    temp = [aList[0]]
    for i, val in enumerate(aList):
        if(i != 0 and temp[-1] != val):
            temp += [val]
    return temp

def two_lists(lst1, lst2):
    result = []

    for pair in zip(lst1, lst2):
        result.extend(pair)

    if len(lst1) != len(lst2):
        lsts = [lst1, lst2]
        smallest = min(lsts, key = len)
        biggest = max(lsts, key = len)
        rest = biggest[len(smallest):]
        result.extend(rest)

    return result

#-------------------------------------------

punctuation = [".", "!", ",", "?"]

endpunc = [".", "!", "?"]

with open("play.txt","r") as f:
     c = f.readlines()
     c = c[::2]

te = []

for i in c:
    z = ".".join(i.split(".")[:1])
    ia = ".".join(i.split(".")[1:]).lower()[:-1]
    g = []
    h = []
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
                h += [temp]
                count = 0
                temp = ""
    g += [temp]
    m = g
    temp2 = []
    for j in m:
        b = j
        for za in punctuation:
            b = (za + " ").join(b.split(" " + za + " "))
            b = (za + " ").join(b.split(" " + za))
        b = b.split(" ")
        b.sort()
        b = removeDuplicates(b)
        temp2 += [" ".join(b).strip()]
        try:
            temp2[-1] = (temp2[-1][0].upper()+temp2[-1][1:])
        except:
            pass #Not sure why this works but this does; it probably deals with the empty strings, but without this the program errors due to an IndexError.
    te = te + [" ".join([z + "."] + two_lists(temp2, h))]
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
     f.write("\n\n".join(tg))
