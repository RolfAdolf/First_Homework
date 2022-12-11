from second_task import sleight_of_hand
import sys

# Чтение из файлов
if (len(sys.argv) > 1):
    for file in sys.argv[1:]:
        with open(file) as f:
            # Число клавиш
            k = int( f.readline() )

            # Поле 
            field = f.readlines()
            if len(field) < 4:
                raise EOFError("Empty input!")
            else:
                field = ''.join( field[:4] )
        
        print(sleight_of_hand(k, field))

# Ручной ввод
else:
    inp = []
    for i in range(5):
        try:
            line = input()
            if not line:
                raise EOFError("Empty input!")
        finally:
            inp.append(line)
    
    # Парсинг
    k = int(inp[0])
    field = ''.join( inp[1:] )



    print(sleight_of_hand(k, field))