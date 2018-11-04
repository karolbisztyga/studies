'''
    @file       Generator.py
    @author     Karol Bisztyga (karolbisztyga@gmail.com)
    @date       2018/10/20
    @version    1.0

    @input - list of Token class objects
    @output - bytecode
    @brief
        converts given list of Tokens into binary code
        it assumes that the syntax has already been checked by the Parser and is correct
'''
from studio_projektowe.compiler.src.Grammar import Grammar
from studio_projektowe.compiler.src.Token import *
from studio_projektowe.compiler.src.Exceptions import *

class Generator:
    def __init__(self):
        self.grammar = Grammar()
        self.BYTE_LENGTH = 8
        self.opcodes = self.generate_opcodes(self.BYTE_LENGTH)

    def generate(self, tokens):
        result = ''
        for token in tokens:
            if token.value not in self.opcodes:
                raise GeneratorException('unrecognized token in generator: '+  str(token))
            result += self.opcodes[token.value]
        return result

    def generate_opcodes(self, length):
        result = {}
        index = 1
        for terminal_length, terminal_arr in self.grammar.TERMINALS.items():
            for terminal in terminal_arr:
                binary = bin(index).replace('0b', '')
                index += 1
                for i in range(0, length - len(binary)):
                    binary = '0' + binary
                if len(binary) > length:
                    raise Exception('opcodes have to be longer, otherwise there could occur repetitions')
                result[terminal[0]] =  binary
        return result

    def print_bytes(self, bits):
        result = ''
        index = 1
        for c in bits:
            result += c
            if index > 0 and index % self.BYTE_LENGTH == 0:
                result += ' '
            index += 1
        return result
