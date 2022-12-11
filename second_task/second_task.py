def sleight_of_hand(k: int, field: str) -> int:

    field = field if ('\n' not in field) else field.replace("\n", '')
    
    # Словарь различных чисел, больших 2k
    field_dict = {key: field.count(key) for key in field if key!='.' and field.count(key) <= 2*k}

    # Длина словаря - количество очков
    return len(field_dict)



