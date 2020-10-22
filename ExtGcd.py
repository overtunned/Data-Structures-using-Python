def xgcd(a,b):
    x = 0;
    y = 1;
    t1 =  1;
    t2 = 0;

    while b != 0:

        temp = b;
        quotient = int(a // b); # getting quotient
        b = a % b; # getting remainder
        a = temp;
        temp = x;
        x = t1 -quotient*x;
        t1 = temp;
        temp = y;
        y = t2-quotient*y;
        t2 = temp;
    print(a)   
    return [t1,t2];

xgcd(30,20)
