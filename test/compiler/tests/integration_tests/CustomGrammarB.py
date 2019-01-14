'''
    @file       CustomGrammarB.py
    @author     Karol Bisztyga (karolbisztyga@gmail.com)
    @date       2018/10/21
    @version    1.0

    @brief
        stores information about grammar needed to check syntax validity
'''


class TokenType:
    LABEL = 'LABEL'


class CustomGrammarB    :
    def __init__(self):
        self.TERMINALS = {
            1: [
                ('y', TokenType.LABEL),
                ('a', TokenType.LABEL),
                ('b', TokenType.LABEL),
            ],
        }
        self.NONTERMINALS = [
            'S',
            'A',
        ]
        self.START_SYMBOL = self.NONTERMINALS[0]
        self.TRANSITIONS = {
            'S': [
                ('x', 'A'),
                ('y', 'A'),
                (None,),
            ],
            'A': [
                ('a', 'A'),
                ('a', ),
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
