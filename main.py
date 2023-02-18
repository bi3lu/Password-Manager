import random
import datetime
import time
import json
from random_word import RandomWords


class Generator:

    def _read_config_nums():
        '''
        '''

    def _read_config_kwords():
        '''
        The method is responsible for reading the kwords value from the json configuration file used to set the default k value in the generate_word_pssaword method
        '''
        f = open("config.json")
        data = json.load(f)
        output = data["generator"]["kwords"]

        return output

    @staticmethod
    def generate_word_password(k=_read_config_kwords()):
        '''
        Method generates a random k-words "word password" using random_word lib
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

        encrypted_passwords = []

        for p in list_of_passwords:
            c_p = Encrypter.caesar(p)
            ab_p = Encrypter.at_bash(c_p)
            encrypted_passwords.append(ab_p)

        return encrypted_passwords

    @classmethod
    def caesar(cls, phrase):
        '''
        The method is responsible for calling the Caesar Cipher on the given phrase parameter
        '''

    @classmethod
    def at_bash(cls, phrase):
        '''
        The method is responsible for invoking the AtBash cipher for the given phrase parameter
        '''


class Decrypter:

    @staticmethod
    def decrypt(list_of_passwords):
        '''
        '''

    @classmethod
    def reverse_caesar(phrase):
        '''
        '''


class StreamReader:

    def __init__(self):
        _passwords_readed = []
        _passwords_ready_to_save = []

    def save_passwords(list_of_passwords):
        '''
        '''

    def read_passwords(list_of_passwords):
        '''
        '''
