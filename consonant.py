my_string = input("Enter a string to count number of consonants: ")
string_check = [
    "a",
    "e",
    "i",
    "o",
    "u",
    "A",
    "E",
    "I",
    "O",
    "U",
]  # list for checking vowels


def count_con(string):
    return sum(
        1 for i in range(len(string)) if (string[i] not in string_check)
    )


counter = count_con(my_string)
print(f"Number of consonants in {my_string} is {counter}.")
