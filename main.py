from art import logo
from os import system
print(logo)
def add(n1, n2):
    return n1 + n2
def substract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operations = {
    "+":add,
    "-":substract,
    "*":multiply,
    "/":divide,
}
running = True
while running == True:
    num1 = float(input("Podaj 1 liczbe: "))
    for o in operations:
        print(o)
    znak = input("Wybierz znak: ")
    num2 = float(input("Podaj 2 liczbe: "))

    def calc(num1,znak,num2):
        calc = operations[znak]
        wynik = calc(num1, num2)
        return wynik
    wynik = calc(num1,znak,num2)
    print(f"Wynik: {wynik}")


    cont_calc = input(f"Napisz 't', jeśli chcesz coś zrobić z wynikiem {wynik}, napisz 'n', jeśli chcesz zacząć od nowa: ")
    if cont_calc == 't':
        petla = True
    elif cont_calc == 'n':
        petla = False
        system('cls')


    while petla == True:

        znak2 = input("Podaj znak: ")
        num3 = float(input("Podaj kolejną liczbe: "))
        wynik = calc(wynik,znak2,num3)
        print(f"Wynik: {wynik}")
        cont_calc = input(f"Napisz 't', jeśli chcesz coś zrobić z wynikiem {wynik}, napisz 'n', jeśli chcesz zacząć od nowa: ")
        if cont_calc == 't':
            petla = True
        elif cont_calc == 'n':
            petla = False
            system('cls')