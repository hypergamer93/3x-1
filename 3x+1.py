import time

print("3x + 1")

startNumber = 0
number = 0

while True:
    
    startNumber += 1
    
    number = startNumber
    
    fileName = str(int(startNumber)) + ".txt"
    
    f = open(fileName, "a")
    
    f.write(str(int(startNumber)) + " ")
    
    time.sleep(0.01)
    
    while number != 1:
        
        if (number % 2) == 0:
            
            number /= 2
            
            print(number)
            
        else:
            
            number *= 3
            
            number += 1
            
            print(int(number))
        
        f.write(str(int(number)) + " ")
        