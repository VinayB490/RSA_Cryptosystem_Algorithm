def prime(a,b):
    for i in range(2,a):
        if a%i==0:
            print(i)
            return False
    for i in range(2,b):
        if b%i==0:
            print(i)
            return False
    return True
def gcd(a,b):
    if a>b:
        small=b
    else:
        small=a
    for i in range(1,small+1):
        if((a%i==0)and(b%i==0)):
            gcdi=i
    return gcdi
while(True):
    print("***************** RSA *****************")
    while(True):
        p=int(input('Enter a prime number :'))
        q=int(input('Enter a prime number :'))
        if(prime(p,q) and (p>1 and q>1) and p!=q):
            break
        else:
            print('Not distinct prime or less than 2 try again')
    n=p*q
    phin=(p-1)*(q-1)
    e=1627
    #e=int(input('Enter Public key'))
    while(True):
        if(gcd(e,phin)==1):
            break
        else:
            e=int(input('Enter "e" were phi(n) = ',phin,' :'))
    for i in range(1,e*e*e):
        if((e*i)%phin==1):
            d=i
            break
    print('Public key = (',e,',',n,')')
    print('Private key = (',d,',',n,')')

    while(True):
        m=int(input('Enter Message : '))    
        print('Cipher : ',(m**e)%n)
        c=int(input('Enter Cipher : '))
        print('Message : ',(c**d)%n)
        k=input('Press y to try new message y/n')
        if(k=='n' or k=='no' or k=='No' or k=='NO' or k=='N'):
            break
    k=input('Press y to try new keys y/n')
    if(k=='n' or k=='no' or k=='No' or k=='NO' or k=='N'):
        print()
        print()
        print()
        break





