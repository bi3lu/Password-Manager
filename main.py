import random
from random_word import RandomWords


class Generator:

    @staticmethod
    def generate_word_password(k=3):
        '''
        Method generates a random k-words "word password" using random_word lib
        k parameter is default set on int value 3
        output_password is str var in which our password is creating
        i int var is counter in while loop
        '''

        output_password = ""
        i = 0
        r = RandomWords()

        while True:
            random_word = r.get_random_word()
            temp_word = str(random_word).capitalize()
            m = random.randint(0, 2)

            if m == 1:
                temp_word += str(random.randint(0, 9))

            output_password += temp_word
            i += 1

            if i == k:
                break

            output_password += "-"

        return output_password


class Encrypter:

    @staticmethod
    def encrypt(list_of_passwords):
        '''
        The method is responsible for simple encryption of the password list
        list_of_passwords parameter is an array of passwords ready to be encrypted
        '''

    @classmethod
    def caesar(phrase):
        '''
        The method is responsible for calling the Caesar cipher on the given phrase parameter
        '''
