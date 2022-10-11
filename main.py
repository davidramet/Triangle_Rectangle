coteA = input("Veuillez saisir le cote A : ")
coteA = int(coteA)
coteB = input("Veuillez saisir le cote B : ")
hypothenuse = input("Veuillez saisir l'hypothenuse : ")
hypothenuse = int(hypothenuse)

if ((coteA * coteA) + (coteB * coteB) == (hypothenuse * hypothenuse)):
  print("le triangle est rectangle ! ")
else:
  print("Le triangle n'est pas rectangle !")
