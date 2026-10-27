num = int(input("enter a factorial num ;"))
fact=1
if num < 0:
    print("factorial of 0 is not exit print right number ")
if num > 0 :
    for i in range (1,num +1):
        fact = fact*i 

        print(fact)
