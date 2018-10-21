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
        self.terminals = 'cpy', 'add', 'sub', 'mul', 'div', 'and', 'lor', 'not', 'xor', 'psh', 'pop', 'cmp', 'jmp', 'jeq', 'jne', 'out', 'cal', 'ret', 'reg', 'exe', '#', ';', ',', '(', ')', '[', ']', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'byt', 'wrd', 'dwd', 'qwd', 'reg', 'con', 'mem'
        self.nonterminals = [
            'S', # start symbol
            'I', # instruction
            'K', # comment
            'A', # argument
            'R', # register label
            'N', # number
            'M', # memory access type
            'X', # any sign
        ]
        start_symbol = self.nonterminals[0]
        self.transitions = {
            'S': ['IS', 'KS', 'I', 'K'],
            'I': [],
            'K': ['#X;'],
            'A': [],
            'R': [],
            'N': [],
            'M': [],
            'X': [],
        }