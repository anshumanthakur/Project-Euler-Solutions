def num_sum(n):
    ans = (n*(n+1))/2
    return ans

def num_sq(n):
    ans = (n*(n+1)*(2*n+1))/6
    return ans

n = 100
ans = pow(num_sum(n),2) - num_sq(n)
print(ans)