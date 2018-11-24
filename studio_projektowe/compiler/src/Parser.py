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

from compiler.src.Grammar import Grammar
from compiler.src.Token import *
from compiler.src.Exceptions import *

class Parser:
    def __init__(self):
        self.grammar = Grammar()
        self.furthest_token = 0

    def parse(self, tokens):
        self.tokens = tokens
        result = self.__parse(self.grammar.START_SYMBOL, 0)
        if result[1] != len(self.tokens):
            return (False, 0)
        if result[0]:
            return (True, result[1])
        return (False, 0)

    def __parse(self, expression, token_index):
        result = False
        token_index_cache = token_index
        for transition in self.grammar.TRANSITIONS[expression]:
            transition_completed = False
            if token_index != token_index_cache:
                token_index = token_index_cache
            for transition_element in transition:
                # check if there are any tokens let, if so go on, otherwise continue loop
                if token_index >= len(self.tokens):
                    if transition_element == None:
                        self.furthest_token = max(self.furthest_token, token_index)
                        return (True, token_index)
                # if token is nonterminal - go deeper into recursion
                if transition_element in self.grammar.NONTERMINALS:
                    parse_result = self.__parse(transition_element, token_index)
                    result = parse_result[0]
                    if result:
                        token_index = parse_result[1]
                        transition_completed = True
                    else:
                        result = False
                        break
                # if token is a terminal, check if it occurs in self.tokens where self.tokens_index points
                # if so, then increase self.tokens_index and proceed, otherwise there's a parsing exception
                elif transition_element != None:
                    try:
                        self.tokens[token_index]
                    except IndexError:
                        self.furthest_token = max(self.furthest_token, token_index)
                        return (False, 0)
                    if self.tokens[token_index].value == transition_element:
                        token_index += 1
                        if transition_element == transition[-1]:
                            transition_completed = True
                            result = True
                        else:
                            result = False
                    else:
                        result = False
                        break
                    if token_index > len(self.tokens):
                        self.furthest_token = max(self.furthest_token, token_index)
                        return (True, token_index)
                else:
                    self.furthest_token = max(self.furthest_token, token_index)
                    return (True, token_index)
            if transition_completed:
                break
        self.furthest_token = max(self.furthest_token, token_index)
        return (result, token_index)

