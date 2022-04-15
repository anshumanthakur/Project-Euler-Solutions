def find_gcd(a,b):
    if a%b==0:
        return b
    else:
        return find_gcd(b,a%b)


num = 20
a = 1
lcm = 2
for i in range(3,num+1):
    b=i
    a=find_gcd(lcm,b)
    lcm = (lcm*b)/a
print(lcm)
