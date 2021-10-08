
#Првоерка числа на простоту 
# O(n log(log n))
def prime(n):
    numb = list(range(n+1))
    numb[0] = numb[1] = False
    for i in range(2, n):
        if numb[i]:
            for j in range(2 * i, n+1, i ):
                numb[j] = False
    return numb #[i for i in numb if i]


print(prime(20))
