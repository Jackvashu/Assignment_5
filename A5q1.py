from unittest import result


# Create You own built-in class method
class Pow:      # class for power multiplication
    def powMet(self):
        x = int(input("Enter number : "))
        n = int(input("Enter power number : "))
        result = x**n
        print(f"{x} power of {n} is : {result}")
    
        
pow_obj = Pow()     #instanciate the pow class
pow_obj.powMet()    # calling tha function with pow object

