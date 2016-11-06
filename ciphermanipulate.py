# ciphermanipulate.py
# Created by Freegle Yuan on 2016-11-06

# Encodes or decodes a text using a given cipher

import re

class CipherProcessorError(Exception):
    pass

# class CipherFileProcessorError(CipherProcessorError):
#     pass


def text_to_nums(text):
    """Converts the input text into an numeric list
    from 1-26 corresponding to a-z"""
    pattern = re.compile('[^A-Za-z]+')
    """ord()returns the numeric value in Unicode of a charactor, minus ord('a')
    so that the numbers of a text accordingly will be returned"""
    return [ord(ch) + 1 - ord('a') for ch in pattern.sub('',text).lower()]

def num_to_num(nums):
    """Converts the numeric list to alphabetic list
    likewise, chr()reutrns the charactor from a number based on Unicode"""
    num_list = [chr(i -1 + ord('a')) for i in nums]
    return ''.join(num_list)


class CipherProcessor(object):
    """Accept a alphabetic string and returns an encoded/decoded string"""
    def __init__(self, key=''):
        """Initializes the string object with a key with blank default"""
        super(CipherProcessor, self).__init__()
        self.key = key

    def text_key_to_nums(self, text):
        """Converts the text and key to numeric list"""
        return text_to_nums(text),text_to_nums(self.key)

    def encode(self, text):
        """Encodes the given text with the key"""
        text_nums, key_nums = self.text_key_to_nums(text)
        encoded_nums = []
        key_len = len(self.key)
        for i, tx in enumerate(text_nums):
            encoded_nums.append((tx + key_nums[i % key_len]) % 26)
        return num_to_num(encoded_nums)

    def decode(self, text):
        """Decodes the given text with the key"""
        text_nums, key_nums = self.text_key_to_nums(text)
        decoded_nums = []
        key_len = len(self.key)
        for i, tx in enumerate(text_nums):
            decoded_nums.append((tx + key_nums[i % key_len]) % 26)
        return num_to_num(decoded_nums)
