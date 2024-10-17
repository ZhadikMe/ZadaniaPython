numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

summa = sum(numbers[0:4] + numbers[5:]);

dlina = len(numbers);

numbers[4] = summa / dlina;

print("Измененный список:", numbers)


