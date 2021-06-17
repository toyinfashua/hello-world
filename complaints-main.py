'''
User Case Story (French Customer)
1. The system should welcome me as a user
2. The system should ask me to submit complain
3. The system should tell me when my when my complain is submitted
User Case Story (Team)
1. The system should list all the complain
2. The system should ask me to pick a complain
4. The system should be able to detect the language used in a complain text
5. The system should be able to translate from one language to the other base on specification
'''
# User Case Story (Customer)
import numpy as np
welcomMessage1 = "Bienvenue client \n"
print(welcomMessage1)  # welcoming the french customer
choiceA = "Oui" or "oui"
#creating an empty dictionary - as a receiver for customer complaints
genComplaints = {}
tckt_no = 1

#asking the customer for their name
Nom = input("S'il te plait, quelle est ton nom? \n")

# asking the customer if they have a complaint
Compl_check = input("Tu as un complaint? Entrez Oui a Non \n ")

# asking the customer to submit the complaint
if Compl_check == choiceA:
    compl1 = input("S'il te plait, ecrivez votre plainte: \n")
    genComplaints[tckt_no] = {"Nom": Nom, "Plainte": compl1}
    tckt_no += 1
else:
  print("Aureviour, a bien tot.")

# verify if they have another complaint
verify = input("Avez-vous une autre plainte? Oui a Non \n")

# setting a boolean condition to the while loop & asking the customer to submit additional complaints
while verify == choiceA:  
    compl2 = input("ecrivez votre plainte. \n")
    genComplaints[tckt_no] = {"Nom": Nom, "Plainte": compl2}
    tckt_no += 1
    verify = input("Avez-vous une autre plainte? Oui au Non \n")

# Once verification for complaints is done, we assure client that the complaints have been received.
print("Nous avons recu votre soumission(s).")

# # User Case Story (Team)
# to List all the complaints
# first asking the team if they would like to see the complaints list
Request = input(
    'Souhaitez-vous voir la liste des plaintes? \n ') 
if Request == choiceA:
    print(genComplaints)
    while Request == choiceA:
  # Asking team to pick a complaint ticket number and display the chosen ticket complaint
      selectCompl = input("S'il vous plait, entres un ticket Number: \n")
      translatefrom = (genComplaints[int(selectCompl)])
      translatefrom= str(translatefrom)

      from deep_translator import GoogleTranslator
      translated = GoogleTranslator(source="auto", target="en").translate(translatefrom)
      print(translated)
      Request = input(
      'Souhaitez-vous voir la liste des plaintes? \n ')
print("Merci beuacoup pour votre temps")