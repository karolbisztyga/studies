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
from studio_projektowe.compiler.src.Token import *
from studio_projektowe.compiler.src.Exceptions import *

class Parser:
    def __init__(self):
        self.grammar = Grammar()

    '''
        powinno sciagac kazdy resullt z kazdej galezi drzewa skladniowego(to co wylazi z rekurencji)
        i jezeli jest jakis pozytywny wynik to znacy, ze skladnia jest poprawna a jak nie to nie
        jeszcze nie ma waruunku stopu algorytmu
    '''
    def parse(self, tokens):
        self.tokens = tokens
        return self.__parse(self.grammar.START_SYMBOL, 0)

    # zacina sie na numerach... jakos zle wraca
    def __parse(self, expression, token_index):
        result = False
        token_index_cache = token_index
        for transition in self.grammar.TRANSITIONS[expression]:
            transition_completed = False
            if token_index != token_index_cache:
                token_index = token_index_cache
            for transition_element in transition:
                # if token is nonterminal - go deeper into recursion
                if transition_element in self.grammar.NONTERMINALS:
                    parse_result = self.__parse(transition_element, token_index)
                    result = result or parse_result[0]
                    if result:
                        token_index = parse_result[1]
                        transition_completed = True
                # if token is a terminal, check if it occurs in self.tokens where self.tokens_index points
                # if so, then increase self.tokens_index and proceed, otherwise there's a parsing exception
                elif transition_element != None:
                    if self.tokens[token_index].value == transition_element:
                        token_index += 1
                        if transition_element == transition[-1]:
                            transition_completed = True
                            result = True
                    else:
                        break
                    if token_index >= len(self.tokens) - 1:
                        return (True, token_index)
                else:
                    return (True, token_index)
            if transition_completed:
                break
        return (result, token_index)

'''
            
           
            else:
                for terminal in
                    pass
            for token in transition:
                # if token is non terminal - go deeper into recursion
                if token.value in self.grammar.NONTERMINALS:
                    result = self.find_productions()
                # if token is terminal, check if it can be popped from self.tokens
                # if so, then pop it, otherwise there's a parsing exception
                else:
                    
            if self.tokens[self.tokens_index] != token:
                raise ParserException('')'''