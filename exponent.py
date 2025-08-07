def expo(num, exp):
        numberout = 1
        for i in range(exp):
            numberout = numberout * num
        return numberout

x = int(input("Enter number: "))
y = int(input("Enter number to exponent: "))

print("Your output "  + str(expo(x, y)))
