from Circle import circle

def main():
    myCircle=circle()

    n=5
    printArea(myCircle,n)
    
    print("\nRadius is",myCircle.radius)
    print("n is",n)

def printArea(c,times):
    print("Radius \t\tArea")
    while times >= 1:
        print(c.radius,"\t\t",c.getArea())
        c.radius = c.radius + 1
        times = times -1

if __name__ == "__main__":
    main()