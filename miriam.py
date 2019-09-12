
z=str(input("pfund oder dollar"))

h=float(input("Gib mal ein nummer"))

y = h * 1.09
k= h * 0.89

if z=="dollar":
    print("Das sind" , str(y) , "$.")

if z=="pfund":
    print("Das sind" , str(k) , "Pfund.")
