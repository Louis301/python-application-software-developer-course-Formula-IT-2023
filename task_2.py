volume_floppy_disk = 1.44  # mb
number_of_pages = 100
number_of_lines = 50
number_of_characters = 25
single_character_store = 4

volume_book = single_character_store * \
              number_of_characters * \
              number_of_lines * \
              number_of_pages  # bytes

volume_book /= (1024 ** 2)  # mb

max_books_quantity = int(volume_floppy_disk // volume_book)

print("Количество книг, помещающихся на дискету:", max_books_quantity)
