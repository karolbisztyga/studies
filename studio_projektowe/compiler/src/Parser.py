'''
    @file       Parser.py
    @author     Karol Bisztyga (karolbisztyga@gmail.com)
    @date       2018/10/20
    @version    1.0

    @input - list of Token class objects
    @output - result of the syntax validation
    @brief
        performs the syntax validation of given list of Tokens
'''

from studio_projektowe.compiler.src.Grammar import Grammar
from studio_projektowe.compiler.src.Token import Token, TokenType
from studio_projektowe.compiler.src.Exceptions import *

class Parser:
    def __init__(self):
        self.grammar = Grammar()

    def parse(self, tokens):
        current_expression = self.grammar.START_SYMBOL
        while len(tokens):
            pass