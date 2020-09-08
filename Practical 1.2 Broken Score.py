score = float(input("Enter score: "))
while 0 <= score >= 101:
    print("Invalid score")
    score = float(input("Enter score: "))
else:
    if 100 >= score >= 90:
        print("Excellent")
    elif 89 >= score >= 50:
        print("Passable")
    else:
        print("Bad")