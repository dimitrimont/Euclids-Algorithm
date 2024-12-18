print("===============================================================")
print("Name: Dimitri Montgomery")
print("Euclid Algorithm project")
print("Github user: dimitrimont")
print("===============================================================")
print("")

def euc_alg():
    m = int(input("enter m: "))
    n = int(input("enter n: "))    # Get user input for number values
    m1 = m
    n1 = n

    if m < n:
        temp = m     #if divisor smaller than numerator swap variables
        m = n
        n = temp
        
    print("")
    print("i|       q       m       n       r")
    print("_|____________________________________")
    
    i = 0
    
    while n != 0:
        q = m // n
        r = m % n   # use Euclids Algorithm
        print(f"{i}| \t {q} \t {m} \t {n} \t {r}")  #Display table
        m = n
        n = r
        i += 1
        if m < 0 or n < 0:
            m = 0
            
    print(f"{i}|               {m}       {0}       STOP")
    print("")
    print(f"The GCD of {m1} and {n1} is {m}")    # Display GCD


euc_alg()
