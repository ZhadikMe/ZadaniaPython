# TODO Найдите количество книг, которое можно разместить на дискете

capacity = 1.44 * 1024 * 1024;

capacity_bits = 1,44;

count_pages = 100;

count_str = 50;

count_symbols = 25;

simbol_weight = 4;

book = 4 * 25 * 50 * 100;

count_of_book = int(capacity/ book);

print("Количество книг, помещающихся на дискету:", count_of_book)
