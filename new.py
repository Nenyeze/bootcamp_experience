# 1. Our machine should be able to validate entry using - username and password
# 2. Our machine should be able to create accounts
# 3. Receive Deposit
# 4. Change user password
# 5. Make withdrawals, Check balance before withdrawing, retain minimum balance
# 6. Generate account No
# 7. Greet user based on the time

import datetime
import random
from os import system

clear = lambda: system ("cls")

allowedUsers = {
    'onyekachi': 'imagine',
    'chinenye': 'pleasant',
    'victory': 'laptop',
    'ijeoma': 'admin'
}

openingBalance = {
    'onyekachi': 120000,
    'chinenye': 200000,
    'victory': 200000,
    'ijeoma': 180000
}

def validate ():
    global username, password
    print ("Please provide your details again")
    username = input ("Username ")
    if username in allowedUsers:
        password = input("Password ")
        if password == allowedUsers[username]:
            login()
        else:
            pass
    return (username, password)

def generateAccountNumber (username):
    return random.randrange(2232200000, 2232299999)

def time_greetings (username):
    login_time = int(datetime.datetime.now().strftime("%H"))
    if (login_time > 4) and (login_time < 12):
        print ("Good morning", username.capitalize())
    elif (login_time > 12) and (login_time < 17):
        print ("Good afternoon", username.capitalize())
    elif (login_time > 17) and (login_time < 20):
        print ("Good evening", username.capitalize())
    else:
        print ("Good Night", username.capitalize())


def checkAccountBalance (username):
    # accountBalance = username.openingBalance
    accountBalance = openingBalance[username]
    print ("Your account balance is", accountBalance)


def deposit():
    amount = int(input("How much are you depositing"))
    # print ("Deposit successful")

    newbalance = openingBalance[username] + amount
    print ("Your account Balance is", newbalance)


def changePassword ():
    currentPassword = allowedUsers[username]
    newpassword = input("What is your new password")
    allowedUsers[username] = newpassword
    print ("Your old password is", currentPassword, "and your new password is", allowedUsers[username])


def login ():
    passhash = len(password)
    hashed = "*" * passhash
    login_time = datetime.datetime.now().strftime("%H:%M:%S")
    login_date = datetime.datetime.now().date()
    print ("Welcome", username.capitalize(), "Your Password is", hashed)
    print ("Hello", username.capitalize(), "Your account balance is", openingBalance[username])
    print ("Your Account Number is", generateAccountNumber(username))
    print ("You logged in today", login_date, "by", login_time)
    time_greetings(username)
    print ("What would you like to do today?")
    print ("1. Check Account Balance \n2. Deposit Funds \n3. Withdraw Funds \n4. Change Password")
    try:
          userchoice = int(input())
          if userchoice == 1:
            checkAccountBalance(username)
          elif userchoice == 2:
               deposit()
          elif userchoice == 3:
            pass
          elif userchoice == 4:
            changePassword()
          else:
               print("You have selected a wrong choice")
            #    closing()
    except ValueError:
          print("You should select numbers not text")
          login()




validate()