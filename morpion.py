case1 = " "
case2 = " "
case3 = " "
case4 = " "
case5 = " "
case6 = " "
case7 = " "
case8 = " "
case9 = " "

i = 0
j="x"
g=0

while i!=10:
    print(case1,"|",case2,"|",case3)
    print("__+___+__")
    print(case4,"|",case5,"|",case6)
    print("__+___+__")
    print(case7,"|",case8,"|",case9)
    ccase = int(input("La croix choisis une case:"))
    if ccase == 1 and (case1!="x" and case1!="o"):
        case1=j
        i=i+1
        if j=="x":
            j="o"
        elif j=="o":
            j="x"
        if case1=="x" and case2=="x" and case3=="x":
            print("Le joueur X a gagné")
            g=1
        if case4=="x" and case5=="x" and case6=="x":
            print("Le joueur X a gagné")
            g=1
        if case7=="x" and case8=="x" and case9=="x":
            print("Le joueur X a gagné")
            g=1
        if case1=="x" and case4=="x" and case7=="x":
            print("Le joueur X a gagné")
            g=1
        if case2=="x" and case5=="x" and case8=="x":
            print("Le joueur X a gagné")
            g=1
        if case3=="x" and case6=="x" and case9=="x":
            print("Le joueur X a gagné")
            g=1
        if case1=="x" and case5=="x" and case9=="x":
            print("Le joueur X a gagné")
            g=1
        if case3=="x" and case5=="x" and case7=="x":
            print("Le joueur X a gagné")
            g=1
        if case1=="o" and case2=="o" and case3=="o":
            print("Le joueur X a gagné")
            g=1
        if case4=="o" and case5=="o" and case6=="o":
            print("Le joueur X a gagné")
            g=1
        if case7=="o" and case8=="o" and case9=="o":
            print("Le joueur X a gagné")
            g=1
        if case1=="o" and case4=="o" and case7=="o":
            print("Le joueur X a gagné")
            g=1
        if case2=="o" and case5=="o" and case8=="o":
            print("Le joueur X a gagné")
            g=1
        if case3=="o" and case6=="o" and case9=="o":
            print("Le joueur X a gagné")
            g=1
        if case1=="o" and case5=="o" and case9=="o":
            print("Le joueur X a gagné")
            g=1
        if case3=="o" and case5=="o" and case7=="o":
            print("Le joueur X a gagné")
            g=1
        elif (case1!=" ") and (case2!=" ") and (case3!=" ") and (case4!=" ") and (case5!=" ") and (case6!=" ") and (case7!=" ") and (case8!=" ") and (case9!=" "):
            print("Personne n'a gagné")
            g=1
        if g==1:
            break
    elif ccase == 2 and (case2!="x" and case2!="o"):
        case2=j
        i=i+1
        if j=="x":
            j="o"
        elif j=="o":
            j="x"
        if case1=="x" and case2=="x" and case3=="x":
            print("Le joueur X a gagné")
            g=1
        if case4=="x" and case5=="x" and case6=="x":
            print("Le joueur X a gagné")
            g=1
        if case7=="x" and case8=="x" and case9=="x":
            print("Le joueur X a gagné")
            g=1
        if case1=="x" and case4=="x" and case7=="x":
            print("Le joueur X a gagné")
            g=1
        if case2=="x" and case5=="x" and case8=="x":
            print("Le joueur X a gagné")
            g=1
        if case3=="x" and case6=="x" and case9=="x":
            print("Le joueur X a gagné")
            g=1
        if case1=="x" and case5=="x" and case9=="x":
            print("Le joueur X a gagné")
            g=1
        if case3=="x" and case5=="x" and case7=="x":
            print("Le joueur X a gagné")
            g=1
        if case1=="o" and case2=="o" and case3=="o":
            print("Le joueur X a gagné")
            g=1
        if case4=="o" and case5=="o" and case6=="o":
            print("Le joueur X a gagné")
            g=1
        if case7=="o" and case8=="o" and case9=="o":
            print("Le joueur X a gagné")
            g=1
        if case1=="o" and case4=="o" and case7=="o":
            print("Le joueur X a gagné")
            g=1
        if case2=="o" and case5=="o" and case8=="o":
            print("Le joueur X a gagné")
            g=1
        if case3=="o" and case6=="o" and case9=="o":
            print("Le joueur X a gagné")
            g=1
        if case1=="o" and case5=="o" and case9=="o":
            print("Le joueur X a gagné")
            g=1
        if case3=="o" and case5=="o" and case7=="o":
            print("Le joueur X a gagné")
            g=1
        elif (case1!=" ") and (case2!=" ") and (case3!=" ") and (case4!=" ") and (case5!=" ") and (case6!=" ") and (case7!=" ") and (case8!=" ") and (case9!=" "):
            print("Personne n'a gagné")
            g=1
        if g==1:
            break
    elif ccase == 3 and (case3!="x" and case3!="o"):
        case3=j
        i=i+1
        if j=="x":
            j="o"
        elif j=="o":
            j="x"
        if case1=="x" and case2=="x" and case3=="x":
            print("Le joueur X a gagné")
            g=1
        if case4=="x" and case5=="x" and case6=="x":
            print("Le joueur X a gagné")
            g=1
        if case7=="x" and case8=="x" and case9=="x":
            print("Le joueur X a gagné")
            g=1
        if case1=="x" and case4=="x" and case7=="x":
            print("Le joueur X a gagné")
            g=1
        if case2=="x" and case5=="x" and case8=="x":
            print("Le joueur X a gagné")
            g=1
        if case3=="x" and case6=="x" and case9=="x":
            print("Le joueur X a gagné")
            g=1
        if case1=="x" and case5=="x" and case9=="x":
            print("Le joueur X a gagné")
            g=1
        if case3=="x" and case5=="x" and case7=="x":
            print("Le joueur X a gagné")
            g=1
        if case1=="o" and case2=="o" and case3=="o":
            print("Le joueur X a gagné")
            g=1
        if case4=="o" and case5=="o" and case6=="o":
            print("Le joueur X a gagné")
            g=1
        if case7=="o" and case8=="o" and case9=="o":
            print("Le joueur X a gagné")
            g=1
        if case1=="o" and case4=="o" and case7=="o":
            print("Le joueur X a gagné")
            g=1
        if case2=="o" and case5=="o" and case8=="o":
            print("Le joueur X a gagné")
            g=1
        if case3=="o" and case6=="o" and case9=="o":
            print("Le joueur X a gagné")
            g=1
        if case1=="o" and case5=="o" and case9=="o":
            print("Le joueur X a gagné")
            g=1
        if case3=="o" and case5=="o" and case7=="o":
            print("Le joueur X a gagné")
            g=1
        elif (case1!=" ") and (case2!=" ") and (case3!=" ") and (case4!=" ") and (case5!=" ") and (case6!=" ") and (case7!=" ") and (case8!=" ") and (case9!=" "):
            print("Personne n'a gagné")
            g=1
        if g==1:
            break
    elif ccase == 4 and (case4!="x" and case4!="o"):
        case4=j
        i=i+1
        if j=="x":
            j="o"
        elif j=="o":
            j="x"
        if case1=="x" and case2=="x" and case3=="x":
            print("Le joueur X a gagné")
            g=1
        if case4=="x" and case5=="x" and case6=="x":
            print("Le joueur X a gagné")
            g=1
        if case7=="x" and case8=="x" and case9=="x":
            print("Le joueur X a gagné")
            g=1
        if case1=="x" and case4=="x" and case7=="x":
            print("Le joueur X a gagné")
            g=1
        if case2=="x" and case5=="x" and case8=="x":
            print("Le joueur X a gagné")
            g=1
        if case3=="x" and case6=="x" and case9=="x":
            print("Le joueur X a gagné")
            g=1
        if case1=="x" and case5=="x" and case9=="x":
            print("Le joueur X a gagné")
            g=1
        if case3=="x" and case5=="x" and case7=="x":
            print("Le joueur X a gagné")
            g=1
        if case1=="o" and case2=="o" and case3=="o":
            print("Le joueur X a gagné")
            g=1
        if case4=="o" and case5=="o" and case6=="o":
            print("Le joueur X a gagné")
            g=1
        if case7=="o" and case8=="o" and case9=="o":
            print("Le joueur X a gagné")
            g=1
        if case1=="o" and case4=="o" and case7=="o":
            print("Le joueur X a gagné")
            g=1
        if case2=="o" and case5=="o" and case8=="o":
            print("Le joueur X a gagné")
            g=1
        if case3=="o" and case6=="o" and case9=="o":
            print("Le joueur X a gagné")
            g=1
        if case1=="o" and case5=="o" and case9=="o":
            print("Le joueur X a gagné")
            g=1
        if case3=="o" and case5=="o" and case7=="o":
            print("Le joueur X a gagné")
            g=1
        elif (case1!=" ") and (case2!=" ") and (case3!=" ") and (case4!=" ") and (case5!=" ") and (case6!=" ") and (case7!=" ") and (case8!=" ") and (case9!=" "):
            print("Personne n'a gagné")
            g=1
        if g==1:
            break
    elif ccase == 5 and (case5!="x" and case5!="o"):
        case5=j
        i=i+1
        if j=="x":
            j="o"
        elif j=="o":
            j="x"
        if case1=="x" and case2=="x" and case3=="x":
            print("Le joueur X a gagné")
            g=1
        if case4=="x" and case5=="x" and case6=="x":
            print("Le joueur X a gagné")
            g=1
        if case7=="x" and case8=="x" and case9=="x":
            print("Le joueur X a gagné")
            g=1
        if case1=="x" and case4=="x" and case7=="x":
            print("Le joueur X a gagné")
            g=1
        if case2=="x" and case5=="x" and case8=="x":
            print("Le joueur X a gagné")
            g=1
        if case3=="x" and case6=="x" and case9=="x":
            print("Le joueur X a gagné")
            g=1
        if case1=="x" and case5=="x" and case9=="x":
            print("Le joueur X a gagné")
            g=1
        if case3=="x" and case5=="x" and case7=="x":
            print("Le joueur X a gagné")
            g=1
        if case1=="o" and case2=="o" and case3=="o":
            print("Le joueur X a gagné")
            g=1
        if case4=="o" and case5=="o" and case6=="o":
            print("Le joueur X a gagné")
            g=1
        if case7=="o" and case8=="o" and case9=="o":
            print("Le joueur X a gagné")
            g=1
        if case1=="o" and case4=="o" and case7=="o":
            print("Le joueur X a gagné")
            g=1
        if case2=="o" and case5=="o" and case8=="o":
            print("Le joueur X a gagné")
            g=1
        if case3=="o" and case6=="o" and case9=="o":
            print("Le joueur X a gagné")
            g=1
        if case1=="o" and case5=="o" and case9=="o":
            print("Le joueur X a gagné")
            g=1
        if case3=="o" and case5=="o" and case7=="o":
            print("Le joueur X a gagné")
            g=1
        elif (case1!=" ") and (case2!=" ") and (case3!=" ") and (case4!=" ") and (case5!=" ") and (case6!=" ") and (case7!=" ") and (case8!=" ") and (case9!=" "):
            print("Personne n'a gagné")
            g=1
        if g==1:
            break
    elif ccase == 6 and (case6!="x" and case6!="o"):
        case6=j
        i=i+1
        if j=="x":
            j="o"
        elif j=="o":
            j="x"
        if case1=="x" and case2=="x" and case3=="x":
            print("Le joueur X a gagné")
            g=1
        if case4=="x" and case5=="x" and case6=="x":
            print("Le joueur X a gagné")
            g=1
        if case7=="x" and case8=="x" and case9=="x":
            print("Le joueur X a gagné")
            g=1
        if case1=="x" and case4=="x" and case7=="x":
            print("Le joueur X a gagné")
            g=1
        if case2=="x" and case5=="x" and case8=="x":
            print("Le joueur X a gagné")
            g=1
        if case3=="x" and case6=="x" and case9=="x":
            print("Le joueur X a gagné")
            g=1
        if case1=="x" and case5=="x" and case9=="x":
            print("Le joueur X a gagné")
            g=1
        if case3=="x" and case5=="x" and case7=="x":
            print("Le joueur X a gagné")
            g=1
        if case1=="o" and case2=="o" and case3=="o":
            print("Le joueur X a gagné")
            g=1
        if case4=="o" and case5=="o" and case6=="o":
            print("Le joueur X a gagné")
            g=1
        if case7=="o" and case8=="o" and case9=="o":
            print("Le joueur X a gagné")
            g=1
        if case1=="o" and case4=="o" and case7=="o":
            print("Le joueur X a gagné")
            g=1
        if case2=="o" and case5=="o" and case8=="o":
            print("Le joueur X a gagné")
            g=1
        if case3=="o" and case6=="o" and case9=="o":
            print("Le joueur X a gagné")
            g=1
        if case1=="o" and case5=="o" and case9=="o":
            print("Le joueur X a gagné")
            g=1
        if case3=="o" and case5=="o" and case7=="o":
            print("Le joueur X a gagné")
            g=1
        elif (case1!=" ") and (case2!=" ") and (case3!=" ") and (case4!=" ") and (case5!=" ") and (case6!=" ") and (case7!=" ") and (case8!=" ") and (case9!=" "):
            print("Personne n'a gagné")
            g=1
        if g==1:
            break
    elif ccase == 7 and (case7!="x" and case7!="o"):
        case7=j
        i=i+1
        if j=="x":
            j="o"
        elif j=="o":
            j="x"
        if case1=="x" and case2=="x" and case3=="x":
            print("Le joueur X a gagné")
            g=1
        if case4=="x" and case5=="x" and case6=="x":
            print("Le joueur X a gagné")
            g=1
        if case7=="x" and case8=="x" and case9=="x":
            print("Le joueur X a gagné")
            g=1
        if case1=="x" and case4=="x" and case7=="x":
            print("Le joueur X a gagné")
            g=1
        if case2=="x" and case5=="x" and case8=="x":
            print("Le joueur X a gagné")
            g=1
        if case3=="x" and case6=="x" and case9=="x":
            print("Le joueur X a gagné")
            g=1
        if case1=="x" and case5=="x" and case9=="x":
            print("Le joueur X a gagné")
            g=1
        if case3=="x" and case5=="x" and case7=="x":
            print("Le joueur X a gagné")
            g=1
        if case1=="o" and case2=="o" and case3=="o":
            print("Le joueur X a gagné")
            g=1
        if case4=="o" and case5=="o" and case6=="o":
            print("Le joueur X a gagné")
            g=1
        if case7=="o" and case8=="o" and case9=="o":
            print("Le joueur X a gagné")
            g=1
        if case1=="o" and case4=="o" and case7=="o":
            print("Le joueur X a gagné")
            g=1
        if case2=="o" and case5=="o" and case8=="o":
            print("Le joueur X a gagné")
            g=1
        if case3=="o" and case6=="o" and case9=="o":
            print("Le joueur X a gagné")
            g=1
        if case1=="o" and case5=="o" and case9=="o":
            print("Le joueur X a gagné")
            g=1
        if case3=="o" and case5=="o" and case7=="o":
            print("Le joueur X a gagné")
            g=1
        elif (case1!=" ") and (case2!=" ") and (case3!=" ") and (case4!=" ") and (case5!=" ") and (case6!=" ") and (case7!=" ") and (case8!=" ") and (case9!=" "):
            print("Personne n'a gagné")
            g=1
        if g==1:
            break
    elif ccase == 8 and (case8!="x" and case8!="o"):
        case8=j
        i=i+1
        if j=="x":
            j="o"
        elif j=="o":
            j="x"
        if case1=="x" and case2=="x" and case3=="x":
            print("Le joueur X a gagné")
            g=1
        if case4=="x" and case5=="x" and case6=="x":
            print("Le joueur X a gagné")
            g=1
        if case7=="x" and case8=="x" and case9=="x":
            print("Le joueur X a gagné")
            g=1
        if case1=="x" and case4=="x" and case7=="x":
            print("Le joueur X a gagné")
            g=1
        if case2=="x" and case5=="x" and case8=="x":
            print("Le joueur X a gagné")
            g=1
        if case3=="x" and case6=="x" and case9=="x":
            print("Le joueur X a gagné")
            g=1
        if case1=="x" and case5=="x" and case9=="x":
            print("Le joueur X a gagné")
            g=1
        if case3=="x" and case5=="x" and case7=="x":
            print("Le joueur X a gagné")
            g=1
        if case1=="o" and case2=="o" and case3=="o":
            print("Le joueur X a gagné")
            g=1
        if case4=="o" and case5=="o" and case6=="o":
            print("Le joueur X a gagné")
            g=1
        if case7=="o" and case8=="o" and case9=="o":
            print("Le joueur X a gagné")
            g=1
        if case1=="o" and case4=="o" and case7=="o":
            print("Le joueur X a gagné")
            g=1
        if case2=="o" and case5=="o" and case8=="o":
            print("Le joueur X a gagné")
            g=1
        if case3=="o" and case6=="o" and case9=="o":
            print("Le joueur X a gagné")
            g=1
        if case1=="o" and case5=="o" and case9=="o":
            print("Le joueur X a gagné")
            g=1
        if case3=="o" and case5=="o" and case7=="o":
            print("Le joueur X a gagné")
            g=1
        elif (case1!=" ") and (case2!=" ") and (case3!=" ") and (case4!=" ") and (case5!=" ") and (case6!=" ") and (case7!=" ") and (case8!=" ") and (case9!=" "):
            print("Personne n'a gagné")
            g=1
        if g==1:
            break
    elif ccase == 9 and (case9!="x" and case9!="o"):
        case9=j
        i=i+1
        if j=="x":
            j="o"
        elif j=="o":
            j="x"
        if case1=="x" and case2=="x" and case3=="x":
            print("Le joueur X a gagné")
            g=1
        if case4=="x" and case5=="x" and case6=="x":
            print("Le joueur X a gagné")
            g=1
        if case7=="x" and case8=="x" and case9=="x":
            print("Le joueur X a gagné")
            g=1
        if case1=="x" and case4=="x" and case7=="x":
            print("Le joueur X a gagné")
            g=1
        if case2=="x" and case5=="x" and case8=="x":
            print("Le joueur X a gagné")
            g=1
        if case3=="x" and case6=="x" and case9=="x":
            print("Le joueur X a gagné")
            g=1
        if case1=="x" and case5=="x" and case9=="x":
            print("Le joueur X a gagné")
            g=1
        if case3=="x" and case5=="x" and case7=="x":
            print("Le joueur X a gagné")
            g=1
        if case1=="o" and case2=="o" and case3=="o":
            print("Le joueur X a gagné")
            g=1
        if case4=="o" and case5=="o" and case6=="o":
            print("Le joueur X a gagné")
            g=1
        if case7=="o" and case8=="o" and case9=="o":
            print("Le joueur X a gagné")
            g=1
        if case1=="o" and case4=="o" and case7=="o":
            print("Le joueur X a gagné")
            g=1
        if case2=="o" and case5=="o" and case8=="o":
            print("Le joueur X a gagné")
            g=1
        if case3=="o" and case6=="o" and case9=="o":
            print("Le joueur X a gagné")
            g=1
        if case1=="o" and case5=="o" and case9=="o":
            print("Le joueur X a gagné")
            g=1
        if case3=="o" and case5=="o" and case7=="o":
            print("Le joueur X a gagné")
            g=1
        elif (case1!=" ") and (case2!=" ") and (case3!=" ") and (case4!=" ") and (case5!=" ") and (case6!=" ") and (case7!=" ") and (case8!=" ") and (case9!=" "):
            print("Personne n'a gagné")
            g=1
        if g==1:
            break