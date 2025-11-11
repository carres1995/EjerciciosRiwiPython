
#Lazy evaluation
def numeros_infinitos():
    n = 0
    while True:
        yield n
        n += 1

nums = numeros_infinitos()

print(next(nums))  
