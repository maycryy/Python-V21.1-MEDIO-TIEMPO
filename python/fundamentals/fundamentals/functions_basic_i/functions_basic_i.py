#se imprimirá la declaracián de námeros alimentarios 
def number_of_food_groups():
    return 5
print(number_of_food_groups())


#dará error ya que hay una declaracion que no esta definida aún                                                      
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())


#imprimira la declaración 5 veces
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())


#se va a aimprimir un print(10) para despues la declaracion 5 veces
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())


#se imprimira un numero 5 y abajo
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)


#establece la funcion contatenante de dos parametros by c
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))


#establece la funcion contatenante con dos parametros b y c
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))


#toma el parametro de la funcion y despues se devuelve el valor 5 despues imprime el valor 100 y 10
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())


#se imprimira el numero 7, el numero 14 y la suma de las 2 anteriores resultando en 21
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))


#10 se va a imprimir la suma de b + c que es igual a  8
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))


#11 se imprimira 500, luego 500, despues 300 porque llama a la foobar y por ultimo 500
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)


#12 se va a imprimir 500, despues 500, despues 300 porque el return lo retorna a 300 y al final 500
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)


#13 se va imprimir 500, despues 500, despues 300 porque el return hace que el valor sea 300 y por ultimo 300 ya que se llama a la foobar para que se imprima.
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)


#14 se imprime 1, despues 3 y luego 2
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()


#15 se va a imprimir 1, despues se va a imprimir 3, luego 5 y despues 10 ya que se llama a la declaracion "y"
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)