import string

input_string = input("Введи дві літери через дефіс: ")
# шукаємо першу та останню літеру
first_letter = input_string[0]
# print(first_letter)
last_letters = input_string[-1]
# print(last_letters)
# знаходимо індекси букв у string.ascii_letters
start_index = string.ascii_letters.index(first_letter)
last_index = string.ascii_letters.index(last_letters)
# за допомогою зрізів прописуємо умову
if start_index <= last_index:
    result = string.ascii_letters[start_index:last_index + 1]
else:
    result = string.ascii_letters[last_index:start_index + 1]
print(result)
