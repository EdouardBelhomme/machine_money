def myFunction(money, price):
    rendu_money = [0, 0, 0, 0, 0, 0]
    tab_money = [1, 5, 10, 25, 50, 100]

#   for elem in rendu_money:
        

    difference = (money *100) - (price *100)
    print (difference)
    if (difference / 100 >= 1):
        # difference -> 401
        # difference % 100 -> 1

        reste = difference % 100
        somme = difference - reste
        print (somme)
        rendu_money[5] = somme / 100
        difference = reste

    if (difference / 50 >= 1):
        reste = difference % 50
        somme = difference - reste
        print (somme)
        rendu_money[4] = somme / 50
        difference = reste

    if (difference / 25 >= 1):
        reste = difference % 25
        somme = difference - reste
        print (somme)
        rendu_money[3] = somme / 25
        difference = reste

    if (difference / 10 >= 1):
        reste = difference % 10
        somme = difference - reste
        print (somme)
        rendu_money[2] = somme / 10
        difference = reste

    if (difference / 5 >= 1):
        reste = difference % 5
        somme = difference - reste
        print (somme)
        rendu_money[1] = somme / 5
        difference = reste

    if (difference / 1 >= 1):
        print (somme)
        rendu_money[0] = difference
        #rendu_money[5] = (difference % 100) / 100

    print(rendu_money)

    return rendu_money

myFunction(1.5, 0.99) # [1, 0, 0, 0, 1, 4] -> 1c, 0 5c, 0 10c, 0 25c, 0 50c, 4 1€