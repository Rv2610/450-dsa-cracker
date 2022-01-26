def palandrom(s):
    str = ""
    for i in s:
        str = i + str
    if str == s:
        print("it is palandrom")
    else:
        print("not palandrom")


palandrom("radar")
palandrom("rohit")
