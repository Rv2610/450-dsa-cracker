def repeat(s):
    l = set()
    for i in s:
       a= int(s.count(i))
       if a > 1:
           l.add(i)

    for  i in l:
        print("the characters ",i, "is repeated")
           
           
       

repeat("rohhhitt")