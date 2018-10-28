'''
    @file       Grammar.py
    @author     Karol Bisztyga (karolbisztyga@gmail.com)
    @date       2018/10/21
    @version    1.0

    @brief
        stores information about grammar needed to check syntax validity
'''
from studio_projektowe.compiler.src.Token import Token, TokenType
from studio_projektowe.compiler.src.Exceptions import *

class Grammar:
    def __init__(self):
        self.TERMINALS = {
            3: [
                ('cpy', TokenType.INSTRUCTION_LABEL),
                ('add', TokenType.INSTRUCTION_LABEL),
                ('sub', TokenType.INSTRUCTION_LABEL),
                ('mul', TokenType.INSTRUCTION_LABEL),
                ('div', TokenType.INSTRUCTION_LABEL),
                ('and', TokenType.INSTRUCTION_LABEL),
                ('lor', TokenType.INSTRUCTION_LABEL),
                ('not', TokenType.INSTRUCTION_LABEL),
                ('xor', TokenType.INSTRUCTION_LABEL),
                ('psh', TokenType.INSTRUCTION_LABEL),
                ('pop', TokenType.INSTRUCTION_LABEL),
                ('cmp', TokenType.INSTRUCTION_LABEL),
                ('jmp', TokenType.INSTRUCTION_LABEL),
                ('jeq', TokenType.INSTRUCTION_LABEL),
                ('jne', TokenType.INSTRUCTION_LABEL),
                ('out', TokenType.INSTRUCTION_LABEL),
                ('cal', TokenType.INSTRUCTION_LABEL),
                ('ret', TokenType.INSTRUCTION_LABEL),
                ('rgd', TokenType.INSTRUCTION_LABEL),
                ('exe', TokenType.INSTRUCTION_LABEL),
                ('byt', TokenType.ACCESS_TYPE),
                ('wrd', TokenType.ACCESS_TYPE),
                ('dwd', TokenType.ACCESS_TYPE),
                ('qwd', TokenType.ACCESS_TYPE),
                ('reg', TokenType.ARGUMENT_TYPE),
                ('con', TokenType.ARGUMENT_TYPE),
                ('mem', TokenType.ARGUMENT_TYPE),
            ],
            2: [
                ('r0', TokenType.REGISTER_LABEL),
                ('r1', TokenType.REGISTER_LABEL),
                ('r2', TokenType.REGISTER_LABEL),
                ('r3', TokenType.REGISTER_LABEL),
                ('r4', TokenType.REGISTER_LABEL),
                ('r5', TokenType.REGISTER_LABEL),
                ('r6', TokenType.REGISTER_LABEL),
                ('r7', TokenType.REGISTER_LABEL),
            ],
            1: [
                (';', TokenType.DELIMITER),
                (',', TokenType.DELIMITER),
                ('(', TokenType.DELIMITER),
                (')', TokenType.DELIMITER),
                ('[', TokenType.DELIMITER),
                (']', TokenType.DELIMITER),
                ('0', TokenType.NUMBER),
                ('1', TokenType.NUMBER),
                ('2', TokenType.NUMBER),
                ('3', TokenType.NUMBER),
                ('4', TokenType.NUMBER),
                ('5', TokenType.NUMBER),
                ('6', TokenType.NUMBER),
                ('7', TokenType.NUMBER),
                ('8', TokenType.NUMBER),
                ('9', TokenType.NUMBER),
            ],
        }
        self.NONTERMINALS = [
            'S', # start symbol
            'I', # instruction
            'A', # argument
            'R', # register label
            'N', # number
            'M', # memory access type
        ]
        self.START_SYMBOL = self.NONTERMINALS[0]
        self.TRANSITIONS = {
            'S': [
                ('I','S'),
                ('I',),
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
                ('r0',),
                ('r1',),
                ('r2',),
                ('r3',),
                ('r4',),
                ('r5',),
                ('r6',),
                ('r7',),
            ],
            'N': [
                ('0','N'),
                ('1','N'),
                ('2','N'),
                ('3','N'),
                ('4','N'),
                ('5','N'),
                ('6','N'),
                ('7','N'),
                ('8','N'),
                ('9','N'),
                (None,),
            ],
            'M': [
                ('byt',),
                ('wrd',),
                ('dwd',),
                ('qwd',),
            ],
        }
        self.COMMENT_START = '#'
        self.COMMENT_END = ';'
        self.MAX_TERMINAL_LENGTH = 3