from first_task import nearest_zero
import sys

# Чтение из файлов
if (len(sys.argv) > 1):
    for file in sys.argv[1:]:
        with open(file) as f:
            line = f.readline()
        
        print(nearest_zero(line))

# Ручной ввод
else:
    line = input()
    if not line:
        raise EOFError("Empty input!")



    print(nearest_zero(line))