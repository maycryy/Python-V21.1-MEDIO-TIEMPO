x = [5,4,3,2,1,0]
print(x)

def print_and_return(lista):
    print(lista[0])
    return lista[1]
print(print_and_return([7,14]))

def first_plus_length(lista):
    return list[0] + len(lista)
print(first_plus_length([1,2,3,4,5]))

def values_greater_than_second(lista):
    if len(lista) < 2:
        return False
    output =[]
    for i in range(0,len(lista)):
        if lista[i] < lista[1]:
            output.append(lista[i])
        print(len(output))
        return output
    print(values_greater_than_second([5,2,3,2,1,4]))
    print(values_greater_than_second([3]))
    def length_and_value(size,value):
        output = []
        for i in range(0, size):
            output.append(value)
            return output
        print(length_and_value(4,7))
        print(length_and_value(6,2))
