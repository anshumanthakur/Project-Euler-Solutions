# cook your code here
def check_pal(c):
    c_str = str(c)
    size = len(c_str)
    is_pal = True
    for i in range(0,int(size/2)):
        if c_str[i]!=c_str[size-i-1]:
            is_pal=False
            break
    if is_pal==True:
        return True
    else:
        return False

n=3
a = pow(10,n)-1
max_p =0

while (a>1):
    b=a
    while(b>1):
        c = a*b
        is_pal = check_pal(c)
        if is_pal==True and c>max_p:
            max_p= c
        else:
            b-=1
    a-=1
print(max_p)
