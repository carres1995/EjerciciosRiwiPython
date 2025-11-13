
def filter_even(list_filter): #creacion de listas filtrando datos y entendiendo el proceso inmutable de listas en funciones.
    return [i for i in list_filter if i > 5]

list_numbers=[1,4,7,2,5,9,1,3,5,6,7,8,2,3,1]
list_filter= filter_even(list_numbers)
print(list_filter)


def double_numbers(numbers):
    
    pass

print(double_numbers([1, 2, 3]))