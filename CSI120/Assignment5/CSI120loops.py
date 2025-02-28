#This will be my assignment on how to print out matrixs with inner and outter loops
i= 1 #This variable will be used for rows
k = 1

while i <= 3: #This will stop the program loop from going beyond 3 rows
    j=1
    while j <= 3: #This will make each row only print out 3 variable results
        print(f"{k}", end=" ")
        j+= 1
        k+= 1 #This will increase the variable bring printed out
    k-= 1 #This will reduce the varibale so that the row below follows
          #the assignment example k=4, 4-1, k=3
    print()
    i += 1
    
