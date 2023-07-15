def Triangle(n):
    for i in range (n):    
        for j in range (i):
            print(end="* ")
        print()
    
def Square(n):
    
    for i in range (n):    
        for j in range (n):
            print(end="* ")
        print()

def RevTriangle(n):
    
    k=(2*n)-2
    for i in range (n):
        
        for j in range (k):
            print(end=" ")
        k-=2
        
        for j in range (i+1):
            print("* ", end="")
        print()

def Pyramid(n):
    
    k=(2*n)-2
    for i in range (n):
        
        for j in range (k):
            print(end=" ")
        k-=1
        
        for j in range (i+1):
            print("* ", end="")
        print()
        
def RevPyramid(n):
    
    k=(2*n)-2
    for i in range (n,0,-1):
            
        for j in range (k,0,-1):
            print(end=" ")
        k+=1
        
        for j in range (i,0,-1):
            print("* ", end="")        
        print()

n = 7
print("What pattern do you wish to print")

Triangle(n)
RevTriangle(n)
Square(n)
Pyramid(n)
RevPyramid(n)
