# We note that the set of reduced fracions are exactly those with coprime numerator and denominator,
# and any two reduced fractions with the tuple (numerator,denominator) unequal are themselves unequal. 
# Therefore the number of fractions with denominator d (that are less than 1) is exactly phi(d), where phi is the totient function.
# We can also do this summing over many denominators without multiple counting due to the uniqueness property given above.
# With this knowlege, we see that working out this sum just comes down to efficiently calculating the totient function,
# so this reuses a lot of my code from problem 70.

def main(n):
    fractionTotal = 0
    numGrid = [0 for i in range (n+1)]
    for i in range (2,len(numGrid)):
        #Case where number is prime (entry is 0)
        if numGrid[i] == 0:
            numGrid[i] = i-1
            toEdit = 2*i
            while toEdit<n+1:
                numGrid[toEdit] = i
                toEdit += i 
            fractionTotal += i-1
        else:
            #Case where number is not prime (entry is non-zero and guaranteed to be the largest prime that goes into the number)
            phi = numGrid[i]-1
            toEdit = i//(phi+1)
            while (toEdit%numGrid[i] == 0):
                toEdit //= numGrid[i]
                phi *= numGrid[i]  
            if not (toEdit == 1):
                phi *= numGrid[toEdit]
            numGrid[i] = phi
            fractionTotal += phi
    return fractionTotal