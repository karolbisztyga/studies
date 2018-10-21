'''
    @file       Grammar.py
    @author     Karol Bisztyga (karolbisztyga@gmail.com)
    @date       2018/10/21
    @version    1.0

    @brief
        stores information about grammar needed to check syntax validity
'''

class Grammar:
    def __init__(self):
        self.terminals = [
            'cpy',      # instructions labels
            'add',
            'sub',
            'mul',
            'div',
            'and',
            'lor',
            'not',
            'xor',
            'psh',
            'pop',
            'cmp',
            'jmp',
            'jeq',
            'jne',
            'out',
            'cal',
            'ret',
            'reg',
            'exe',
            ';',        # delimiters
            ',',
            '(',
            ')',
            '[',
            ']',
            '0',        # digits
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            'a',        # registers labels
            'b',
            'c',
            'd',
            'e',
            'f',
            'g',
            'h',
            'byt',      # access types
            'wrd',
            'dwd',
            'qwd',
            'reg',      # argument types
            'con',
            'mem',
        ]
        self.nonterminals = [
            'S', # start symbol
            'I', # instruction
            'A', # argument
            'R', # register label
            'N', # number
            'M', # memory access type
        ]
        start_symbol = self.nonterminals[0]
        self.transitions = {
            'S': [
                ('I','S'),
                ('I',)
            ],
            'I': [
                ('cpy','(','A',';','A',')',';'),
                ('add','(','A',';','A',';','A',')',';'),
                ('sub','(','A',';','A',';','A',')',';'),
                ('mul','(','A',';','A',';','A',')',';'),
                ('div','(','A',';','A',';','A',')',';'),
                ('and','(','A',';','A',';','A',')',';'),
                ('lor','(','A',';','A',';','A',')',';'),
                ('not','(','A',';','A',')',';'),
                ('xor','(','A',';','A',';','A',')',';'),
                ('psh','(','A',')',';'),
                ('pop','(','A',')',';'),
                ('cmp','(','A',';','A',';','A',')',';'),
                ('jmp','(','A',')',';'),
                ('jeq','(','A',';','A',';','A',')',';'),
                ('jne','(','A',';','A',';','A',')',';'),
                ('out','(','A',')',';'),
                ('cal','(','A',')',';'),
                ('ret','(',')',';'),
                ('reg','(','A',')',';'),
                ('exe','(','A',')',';'),
            ],
            'A': [
                ('[','reg',']','R'),
                ('[','con',']','N'),
                ('[','mem',']','M','N'),
            ],
            'R': [
                ('a',),
                ('b',),
                ('c',),
                ('d',),
                ('e',),
                ('f',),
                ('g',),
                ('h',),
            ],
            'N': [
                ('0',),
                ('1',),
                ('2',),
                ('3',),
                ('4',),
                ('5',),
                ('6',),
                ('7',),
                ('8',),
                ('9',),
                ('NN',),
            ],
            'M': [
                ('byt',),
                ('wrd',),
                ('dwd',),
                ('qwd',),
            ],
        }