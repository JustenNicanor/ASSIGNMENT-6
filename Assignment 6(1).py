#Create a program that ask 4 numbers. 
#Print the 4 numbers from highest to lowest using only if-else statement

def Four_Numbers():
    Firstnum = int(input("Enter First number:"))
    Secondnum = int(input("Enter Second number:"))
    Thirdnum = int(input("Enter Third number:"))
    Fourthnum = int(input("Enter Fourth number:"))
    if Firstnum > Secondnum and Secondnum > Thirdnum and Thirdnum > Fourthnum:
        print (f"Highest to lowest of numbers: {Firstnum},{Secondnum},{Thirdnum},{Fourthnum}")
    elif Firstnum > Secondnum and Secondnum > Fourthnum and Fourthnum > Thirdnum:
        print (f"Highest to lowest of numbers: {Firstnum},{Secondnum},{Fourthnum},{Thirdnum}")
    elif Firstnum > Thirdnum and Thirdnum > Secondnum and Secondnum > Fourthnum:
        print (f"Highest to lowest of numbers: {Firstnum},{Thirdnum},{Secondnum},{Fourthnum}")
    elif Firstnum > Thirdnum and Thirdnum > Fourthnum and Fourthnum > Secondnum:
        print (f"Highest to lowest of numbers: {Firstnum},{Thirdnum},{Fourthnum},{Secondnum}")
    elif Firstnum > Fourthnum and Fourthnum > Secondnum and Secondnum > Thirdnum:
        print (f"Highest to lowest of numbers: {Firstnum},{Fourthnum},{Secondnum},{Thirdnum}")
    elif Firstnum > Fourthnum and Fourthnum > Thirdnum and Thirdnum > Secondnum:
        print (f"Highest to lowest of numbers: {Firstnum},{Fourthnum},{Thirdnum},{Secondnum}")
    elif Secondnum > Firstnum and Firstnum > Thirdnum and Thirdnum > Fourthnum:
        print (f"Highest to lowest of numbers: {Secondnum},{Firstnum},{Thirdnum},{Fourthnum}")
    elif Secondnum > Firstnum and Firstnum > Fourthnum and Fourthnum > Thirdnum:
        print (f"Highest to lowest of numbers: {Secondnum},{Firstnum},{Fourthnum},{Thirdnum}")
    elif Secondnum > Thirdnum and Thirdnum > Firstnum and Firstnum > Fourthnum:
        print (f"Highest to lowest of numbers: {Secondnum},{Thirdnum},{Firstnum},{Fourthnum}")
    elif Secondnum > Thirdnum and Thirdnum > Fourthnum and Fourthnum > Firstnum:
        print (f"Highest to lowest of numbers: {Secondnum},{Thirdnum},{Fourthnum},{Firstnum}")
    elif Secondnum > Fourthnum and Fourthnum > Firstnum and Firstnum > Thirdnum:
        print (f"Highest to lowest of numbers: {Secondnum},{Fourthnum},{Firstnum},{Thirdnum}")
    elif Secondnum > Fourthnum and Fourthnum > Thirdnum and Thirdnum > Firstnum:
        print (f"Highest to lowest of numbers: {Secondnum},{Fourthnum},{Thirdnum},{Firstnum}")

    
        









num = Four_Numbers()