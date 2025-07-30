#Breach Bot Starter Code
breachYear = 2017

#Greets user
print("Hello! I'm Breach Bot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts year of breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since the Hong Kong Registration and Electoral Office data breach.")

#Introduces breach
print("Would you like to learn about the Hong Kong Registration and Electoral Office data breach?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organization's response, or (c) I would like to hear your reflection")
  topic = input()
  
  if topic.lower() == "a":
    print("In 2017, 3.7 million voter registration records were stolen in Hong Kong. The laptops containing voter registration data were stolen.")
  
  elif topic.lower() == "b":
    print("The election alerted voters to the data breach. Hong Kong’s Personal Data (Privacy) Ordinance increased fines for mishandling user data, enforcing the security of user data.")
  
  elif topic.lower() == "c":
    break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")

#Introduces my take
print("\nI'm excited to share my perspective on this. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

#Shares my take
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to the CIA triad, (b) my reaction, (c) my advice or (d) none")
  topic = input()

  if topic.lower() == "a":
    print("The data breach connects to confidentiality because confidential voter registration data was leaked to unauthorized malicious actors when the laptops were stolen.")

  elif topic.lower() == "b":
    print("We disagree with the Hong Kong Registration and Electoral Office’s response because even though they informed voters of the breach and the Hong Kong PDPO increased fines for mishandling data, the office did not increase its security measures for voter data. The office should propose safer ways to store the data instead of in two vulnerable, cheap laptops.")

  elif topic.lower() == "c":
    print("I would convince victims to take action by urging the Registration and Electoral Office to store voter registration data more securely. My advice would be to be careful when including personal information, even to the government, in case of data breaches like this.")

  elif topic.lower() == "d":
    break
    
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")

  input("Press enter to continue\n")

#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")
