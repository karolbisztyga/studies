'''
    @file       CustomGrammar.py
    @author     Karol Bisztyga (karolbisztyga@gmail.com)
    @date       2018/10/21
    @version    1.0

    @brief
        stores information about grammar needed to check syntax validity
'''


class TokenType:
    LABEL = 'LABEL'


class CustomGrammar:
    def __init__(self):
        self.TERMINALS = {
            1: [
                ('a', TokenType.LABEL),
                ('b', TokenType.LABEL),
            ],
        }
        self.NONTERMINALS = [
            'A',
            'B',
        ]
        self.START_SYMBOL = self.NONTERMINALS[0]
        self.TRANSITIONS = {
            'A': [
                ('a', 'A'),
                ('B',),
                (None,),
            ],
            'B': [
                ('b', 'B'),
                (None,),
            ],
        }
        self.COMMENT_START = '#'
        self.COMMENT_END = ';'
        self.MAX_TERMINAL_LENGTH = 1

    def get_number_of_terminals(self):
        result = 0
        for k, v in self.TERMINALS.items():
            result += len(v)
        return result
