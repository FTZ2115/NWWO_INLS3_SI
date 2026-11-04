def add_task(lista_zadan):
    zadanie = input("Podaj treść zadania: ").strip().lower()

    if zadanie:
        lista_zadan.append(zadanie)
        print("Zadanie dodano!")

    print("Zadanie nie może być pusta")