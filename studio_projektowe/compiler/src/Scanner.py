'''
    @file       Scanner.py
    @author     Karol Bisztyga (karolbisztyga@gmail.com)
    @date       2018/10/20
    @version    1.0

    @input - code as string
    @output - list of Token class objects
    @brief
        removing redundant elements of the code(spaces, comments etc)
        generating a list of tokens from given code
'''
from studio_projektowe.compiler.src.Grammar import Grammar

class Scanner:
    def __init__(self, code):
        self.grammar = Grammar()
        self.__code = code

    def scan(self):
        self.__clear_code()
        self.__generate_tokens()

    def clear_code(self):
        # remove spaces, tabs, newlines etc.
        # remove comments
        pass

    def generate_tokens(self):
        pass
