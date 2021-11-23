def Quiz():
    import random
    for i in range (10):
        num1 = random.randint(0,99)
        num2 = random.randint(0,99)
        ans = num1+num2
        print(f" what is {num1} + {num2}?")
        plrans = int(input("Answer: ")) 
        if plrans == ans : 
            Score = Score + 1
            print("CORRECT!")
        else: 
            print(f"INCORRECT the answer is {ans}")
    print(f"Your score is,{Score}/10 ")



quiz_ = Quiz()