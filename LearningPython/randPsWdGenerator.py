import random

#random password generator that must include 1 upercase, a number, and 
#and a special character and then shuffle them all.
restart = "yes"

while restart != "no":
    randPass = ""

    lenPass = int(input("How long do you wnat your password to be?:"))

    numCaps = int(input("How many capital letters would you like?: "))
    #numLow = int(input("How many lowercase letters would you like?: "))
    numNumb = int(input("How many numbers would you like?: "))
    numSpec = int(input("How many special characters would you like?: "))
    numLow = lenPass-(numCaps+numNumb+numSpec)
    

    restartSizeError = "no"
    if numLow <0:
        restartSizeError = str(input("""You provided more characters than the length you wanted
        do you want to restart? """))
    if restartSizeError == "yes":
        continue

    for x in range(numCaps):
        randPass += ""+chr(random.randint(65,90))
    
    for x in range(numNumb):
        randPass += ""+chr(random.randint(48,57))

    for x in range(numLow):
        randPass += ""+chr(random.randint(97,122))
    
    for x in range(numSpec):
        randPass += ""+chr(random.randint(33,47))

    
    # num1 = chr(random.randint(48,57))
    # num2 = chr(random.randint(48,57))
    # spec1 = chr(random.randint(33,47))
    # lchar1 = chr(random.randint(97,122))
    # lchar1 = chr(random.randint(97,122))
    # lchar2 = chr(random.randint(97,122))
    # lchar3 = chr(random.randint(97,122))


    # randPass = uchar1+spec1+num1+num2+lchar1+lchar2+lchar3

    print (randPass)

    shuffle = "yes"

    while shuffle == "yes":
        shuffle = str(input("Do you want to shuffle, yes or no?: "))

        if shuffle == "yes":
            shrandPass = ''.join(random.sample(randPass,len(randPass)))
            print(shrandPass)


    restart = str(input("Do not like password? Would you like to restart? "))

    if restart == "yes":
        continue
    elif restart == "no":
        break





