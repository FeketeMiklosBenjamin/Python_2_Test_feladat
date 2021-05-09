def main() -> None:
    print('A hasáb térfogatát kiszámoló függvény!')
    a : float = float(input('a (él) = '))
    b : float = float(input('b (él) = '))
    c : float = float(input('c (él) = '))
    if a < 1 or b < 1 or c < 1:
        print('A megadott adatokkal nem lehet számolni!')
    else:
        hasáb_terfogata: float = a * b * c
        print(f'A hasáb térfogata: {hasáb_terfogata}')

    print('A hasáb felszínét kiszámoló függvény!')
    a : float = float(input('a (él) = '))
    b : float = float(input('b (él) = '))
    c : float = float(input('c (él) = '))
    if a < 1 or b < 1 or c < 1: 
        print('A megadott adatokkal nem lehet számolni!')
    else:
        hasáb_felszine: float = (2 * a * b) + (2 * a * c) + (2 * b * c)
        print(f'A hasáb felszíne: {hasáb_felszine}')

if __name__ == "__main__":
    main()