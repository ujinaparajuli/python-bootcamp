def ap(fname="Hello"):
    print(fname + " Poudel")


ap("Aashish")
ap()

#recursion function
def fact(n):
    if n==0 or n==1:
        return 1
    else: 
        return n*fact(n-1)

f = fact(5)
print(f)