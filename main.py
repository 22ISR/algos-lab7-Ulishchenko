# """
# Задание №1

# Задание: Написать программу, которая принимает на вход слово и проверяет, является ли оно палиндромом.
# Условия:

#     Программа должна быть нечувствительна к регистру.
#     Игнорировать пробелы и знаки пунктуации.


def isPalindrom(word):
    word = word.replace(" ", "").lower()
user_imput = input("Введите:")
if user_imput == user_imput[::-1]:
    print("Полиндром")   
else:    
    print("Не полиндром")
 Правильное(вроде):
def isPalindrom(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]:

user_imput = input("Ввод: ")
print(isPalindrom(user_imput))
    

# Задание №2

# Задание: Написать программу, которая принимает список слов и проверяет, какие из них являются палиндромами.
# Условия:
#     Слова передаются в виде списка через ввод пользователя.
#     Программа должна вывести все палиндромы из списка.
# def isPalindromlist(word)
#     word = word.lower()replace(" ", "")
#     return word == word[::-1]

# def check_isPalindrom(wordi):
#     Palindrom = []
#     for word in word:
#         if isPalindromlist(word):
#             Palindrom.append(word.lower())
#     peturn Palindrom

# user_imput = input("Ввод: ")
# word_list = [word.strip() for word in user_imput.split(",")]
# print(check_isPalindrom(wordi_list))


# abuyz:
# n = int(input("Enter the number of elements: "))
# for i in range(n):
#     element = input(f"Enter element {i+1}: ")
#     a.append(element)
# print("List:", a)


   


# Задание №3

# Задание: Написать программу, которая ищет все палиндромы в строке текста.
# Условия:

#     Программа должна игнорировать регистр и знаки пунктуации.
#     Если палиндромы повторяются, выводить их только один раз.

# Пример использования isPalindromString("Madam, Anna went to the civic center") # ["madam", "anna", "civic"]
# """
def isPalindromlist(word)
    word = word.lower()replace(" ", "")
    return word == word[::-1]

def check_isPalindrom(wordi):
    Palindrom = []
    for word in word:
        if isPalindromlist(word):
            Palindrom.append(word.lower())
    peturn Palindrom

user_imput = input("Ввод: ")
word_list = [word.strip() for word in user_imput.split(",")]
print(check_isPalindrom(wordi_list))
def isPalindrom(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]:
def find_palindromStringe(word):
    word = text.split()
    palindromes = set()
    for word in word:
        word= ".join(char for char in word if char.isalnum())"
        if isPalindromeString(word) and word:
            palindrome.add(word.lower())
    return list(palindromes)
    user_input = input("Ввод: ")
    print(find_palindromes(user_input))
