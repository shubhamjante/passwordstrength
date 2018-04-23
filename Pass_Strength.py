import string
import re

__author__ = "Shubham Jante"
__credits__ = "Passwordmeter"
__version__ = "1.0"
__maintainer__ = "Shubham Jante"
__email__ = "shubhamjante1995@gmail.com"
__status__ = "In Development"
__date__ = "2018/01/27"


class Password_Strength:
    """
    :parameter word: takes a string known as password
    :parameter size: size is a keyword argument the default value is 8 but this can be modified
    :type str() : word
    :type int() : size
    :returns: this class returns a string of percentage stating how strong the password is!

    :var self.password: self.word
    :var self.score: stores the calculated password strength result
    :var self.length: defines the default length of the password to check default value is 8
    :dict requirements: stores number of requirements passed for further calculation

    :Example
        strength = Password_Strength(YOUR_PASSWORD)
        print(strength)

        or
        print(Password_Strength(YOUR_PASSWORD))

    Methods defined here:
        __init__(self, word, size=8)
            The class constructor takes two arguments. The constructor will call all the methods used in the class.
            :argument word : :type str : Represents the password string
            :argument size : :type int : Keyword argument represents the required length of the password.
            Default value is 8

        num_of_chars(self)
            This function calculates the score on the number of characters in the given password

        ucase_letters(self)
            This method calculate the number of UPPERCASE LETTERS in the password and update the score

        lcase_letters(self)
            This method calculate the number of lowercase letters in the password and update the score

        numbers(self)
            This method calculate the number of digits present in the password and update the score

        symbols(self)
            This method calculate the number of symbols in the password and update the score

        middle_num_symbol(self)
            Working on it

        min_requirements(self)
            This method use the dict to identity how many requirements are passed by the password and update the score
            :var self.requirements: defined in :func __init__(self, word, size=8) : Class Constructor

            Minimum Requirements are:
            1. Minimum 8 characters in length
            2. Contains 3/4 of the following items:
                - Uppercase Letters
                - Lowercase Letters
                - Numbers
                - Symbols

        letters_only(self)
            If the given password contain only letters then this method will update the score
            :Example
                password = aeplSdniEe

        numbers_only(self)
            If the given password contain only numbers/digits then this method will update the score
            :Example
                password = 465930463

        consecutive_uppercase(self)
            If the consecutive uppercase letters present in the password then it's easy to brute force. This method
            will check the the consecutive uppercase and updates the score.
            :Example
                password = FHALHE4658#kjhf

        consecutive_lowercase(self)
            If the consecutive lowercase letters present in the password then this method will update the score
            :Example
                password = heipx254@3H

        consecutive_numbers(self)
            If the consecutive digits present in the password then this method will update the score
            :Example
                password = 34839@kdfGHr

        sequential_letters(self)
            IF the sequential letters present in the password then this method will update the score.
            The counter will start counting if there are 3+ sequential letters present
            :Example
                if password = abcdef
                then total_sequential_letters = 4

                if password = abc
                then total_sequential_letters = 1

        sequential_numbers(self)
            IF the sequential digits present in the password then this method will update the score.
            The counter will start counting if there are 3+ sequential digits present
            :Example
                if password = 12345
                then total_sequential_letters = 3

                if password = 012
                then total_sequential_letters = 1

        sequential_symbols(self)
            This method uses symbol dict in which keys represent the integer values obtained from function
            ord(sym) and values represent sym {ord(sym):sym}

        printscore(self)
            :returns score: :type class object : Returns the final score which will represent the total percentage out of 100
            :Example
                74% means the password is 74% strong out of 100
                100% is assumed as the strongest password
                0% is assumed as the weakest password

        @override method
        __str__(self)
            This method will be used to convert the class object returned by :func printscore(self)
            :returns score: :type str : Returns a score + %
    """
    def __init__(self, word, size=8):
        self.password = word
        self.score = 0
        self.length = size
        self.requirements = {'length': len(self.password), 'uppercase': 0, 'lowercase': 0, 'number': 0, 'symbol': 0}
        self.num_of_chars()
        self.ucase_letters()
        self.lcase_letters()
        self.numbers()
        self.symbols()
        self.middle_num_symbol()
        self.min_requirements()
        self.letters_only()
        self.numbers_only()
        self.consecutive_uppercase()
        self.consecutive_lowercase()
        self.consecutive_numbers()
        self.sequential_letters()
        self.sequential_numbers()
        self.sequential_symbols()
        self.printscore()

    def num_of_chars(self):
        self.score += len(self.password) * 4

    def ucase_letters(self):
        ucase_count = 0
        if self.password.isupper():
            ucase_count += 0
        else:
            for x in self.password:
                if x.isupper():
                    ucase_count += 1

        self.requirements['uppercase'] = ucase_count
        if ucase_count > 0:
            self.score += (self.requirements['length']-ucase_count)*2

    def lcase_letters(self):
        lcase_count = 0
        if self.password.islower():
            lcase_count += 0
        else:
            for x in self.password:
                if x.islower():
                    lcase_count += 1

        self.requirements['lowercase'] = lcase_count
        if lcase_count > 0:
            self.score += (self.requirements['length']-lcase_count)*2

    def numbers(self):
        number_count = 0
        if self.password.isalpha():
            number_count += 0
        elif self.password.isdigit():
            number_count += 0
        else:
            for x in self.password:
                if x in string.digits:
                    number_count += 1

        self.requirements['number'] = number_count
        self.score += number_count * 4

    def symbols(self):
        sym_count = 0
        for x in self.password:
            if x in string.punctuation:
                sym_count += 1

        self.requirements['symbol'] = sym_count
        self.score += sym_count * 6

    def middle_num_symbol(self):
        pass

    def min_requirements(self):
        requirement_count = 0
        if self.requirements['length'] < self.length:
            requirement_count += 0
        else:
            for x in self.requirements.values():
                if x > 0:
                    requirement_count += 1

        if requirement_count >= 4:
            self.score += requirement_count * 2

    def letters_only(self):
        if self.password.isalpha():
            self.score -= self.requirements['length']

    def numbers_only(self):
        if self.password.isdigit():
            self.score -= self.requirements['length']

    def repeat_characters(self):
        char_count = dict()
        repeat_char_count = 0
        for x in self.password:
            if x not in char_count:
                char_count[x] = 1
            else:
                char_count[x] += 1
        for y in char_count.keys():
            if char_count[x] >= 2:
                repeat_char_count += char_count[x]

        self.score -= repeat_char_count

    def consecutive_uppercase(self):
        uppercase_error_count = 0
        for i in range(self.requirements['length']-1):
            if self.password[i] in string.ascii_uppercase:
                if self.password[i+1] in string.ascii_uppercase:
                    uppercase_error_count += 1

        self.score -= uppercase_error_count * 2

    def consecutive_lowercase(self):
        # lowercase_error_count = 0
        l = re.findall('[a-z](?=[a-z])', self.password)
        lowercase_error_count = len(l)

        self.score -= lowercase_error_count * 2

    def consecutive_numbers(self):
        # number_error_count = 0
        n = re.findall('[0-9](?=[0-9])', self.password)
        number_error_count = len(n)

        self.score -= number_error_count * 2

    def sequential_letters(self):
        seq_letter_error = 0
        for i in range(self.requirements['length']-2):
            letter = ord(self.password[i])
            if letter + 1 == ord(self.password[i+1]):
                if letter + 2 == ord(self.password[i+2]):
                    seq_letter_error += 1

        self.score -= seq_letter_error * 3

    def sequential_numbers(self):
        seq_number_error = 0
        for i in range(self.requirements['length']-2):
            if self.password[i].isdigit():
                number = ord(self.password[i])
                if number + 1 == ord(self.password[i+1]):
                    if number + 2 == ord(self.password[i+2]):
                        seq_number_error += 1

        self.score -= seq_number_error * 3

    def sequential_symbols(self):
        seq_sym_error = 0
        symbol_dict = {33: '!', 34: '"', 35: '#', 36: '$', 37: '%', 38: '&', 39: "'",
                       40: '(', 41: ')', 42: '*', 43: '+', 44: ',', 45: '-', 46: '.',
                       47: '/', 48: '@', 49: '@', 50: '@', 51: '@', 52: '@', 53: '@',
                       54: '@'}
        for i in range(self.requirements['length']-1):
            symbol = ord(self.password[i])
            try:
                if chr(symbol + 1) == symbol_dict[symbol + 1]:
                        seq_sym_error += 1
            except KeyError:
                pass

        self.score -= seq_sym_error * 3

    def printscore(self):
        return self.score

    def __str__(self):
        if self.score > 100:
            self.score = 100

        return "".join(str(self.score) + "%")

        