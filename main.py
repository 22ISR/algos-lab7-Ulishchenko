# """
# Задание №1

# Задание: Написать программу, которая принимает на вход слово и проверяет, является ли оно палиндромом.
# Условия:

#     Программа должна быть нечувствительна к регистру.
#     Игнорировать пробелы и знаки пунктуации.

def isPalindrom(word):
     word = word.replace(" ", "").lower()
     return word == word[::-1]
user_imput = input("Ввод:")
if isPalindrome(user_input):
    print("Палиндром")
else:
    print("Не палиндром")
    

# Задание №2
def isPalindrom(word):
     return word == word[::-1]
     user_imput = input("Ввод слов:")
     words user_input.split(',')
     for word in ["".join(filter(str.isalpha, w)) for w in text.split(" ")]:
          print("palidrome") if word.lover()[::-1] else print("not palidrome")
          print("Палидром: ")
# Задание: Написать программу, которая принимает список слов и проверяет, какие из них являются палиндромами.
# Условия:

#     Слова передаются в виде списка через ввод пользователя.
#     Программа должна вывести все палиндромы из списка.

#  def isPalindrom(Word):
#          word= word.lower
#     return word_lower 
#     word_lower =  word_lower[::-1]

# Пример использования:
#     isPalindromList(["hello", "list", "level"]) # ["level"]

# Задание №3

# Задание: Написать программу, которая ищет все палиндромы в строке текста.
# Условия:

#     Программа должна игнорировать регистр и знаки пунктуации.
#     Если палиндромы повторяются, выводить их только один раз.

# Пример использования isPalindromString("Madam, Anna went to the civic center") # ["madam", "anna", "civic"]
# """
