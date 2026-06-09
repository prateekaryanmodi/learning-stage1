#waf to calculate the sum of first n natural numbers
def cal_sum(n):
    if (n==0 ):
        return 0
    return cal_sum(n-1)+n
total=cal_sum(3)
print(total)
