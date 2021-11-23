def Quiz():
    import random
    Score = 0
    for i in range (10):
        num1 = random.randint(0,99)
        num2 = random.randint(0,99)
        ans = num1+num2
        print(f" What is {num1} + {num2}?")
        useranswer = int(input("Answer: "))
        if useranswer == ans: 
            Score += 1
            print("CORRECT!")
        else:
            print(f"INCORRECT, the answer is {ans}")
    print (f"Your score is {Score}/10")


quiz_= Quiz()



