pswd=input("Enter the password:")

if len(pswd)<8:
    print("invalid password")
else:
    letters=0
    digits=0
    for x in pswd:
        if ('a'<=x and x<='z') or ('A'<=x and x<='Z'):
            letters+=1
        elif '0'<=x and x<='9':
            digits+=1
        else:
            print("invalid password")
            break
    if digits<2:
        print("invalid password")
    else:
        print("valid password")

