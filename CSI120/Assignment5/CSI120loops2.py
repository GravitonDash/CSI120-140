#This will be my assignment on how to print out matrixs with inner and outter loops
i= 1 #This variable will be used for rows
k = 1

while i <= 5: #This will stop the program loop from going beyond 3 rows
    j=1
    while j <= 5: #This will make each row only print out 3 variable results
        print(f"{k}", end=" ")
        j+= 1
        k+= 1 #This will increase the variable bring printed out
    k-= 1 #This will decrease the variable to  the
          #necessary number for the following row EX: k=6, 6-1= 5, k=5
    k= k*10 ##multiplies the variable for the next row EX: k=5, 5*10= 50
    print()
    i += 1
