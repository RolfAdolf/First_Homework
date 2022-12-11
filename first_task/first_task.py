def nearest_zero(array: str) -> str:

    # Разбиение строки на список чисел.
    array = [ int(s) for s in array.split(' ') ]
    n = len(array)


    # Обход слева направо (ближайший ноль слева).
    # Счётчик расстояния слева до нуля.
    zero_dist = int(1e9)

    for i in range(n):
        
        if array[i]:
            zero_dist += 1
            array[i] = zero_dist
        else:
            zero_dist = 0

    
    # Обход справа налево (ближайший справа или слева ноль).
    # Счётчик расстояния справа до нуля.
    zero_dist = int(1e9)

    for i in range(n-1, -1, -1):
        
        if array[i]:
            zero_dist += 1
            array[i]= min( array[i], zero_dist )
        else:
            zero_dist = 0

    return " ".join(str(i) for i in array)