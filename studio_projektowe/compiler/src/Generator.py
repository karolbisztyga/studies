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
from studio_projektowe.compiler.src.BinaryTools import BinaryTools
from studio_projektowe.compiler.src.Token import *
from studio_projektowe.compiler.src.Exceptions import *

class Generator:
    def __init__(self):
        self.grammar = Grammar()
        self.opcodes = self.generate_opcodes(BinaryTools.BYTE_LENGTH)

    def generate(self, tokens):
        result = b''
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
                binary = BinaryTools.fill_with_zeros(str.encode(bin(index).replace('0b', '')))
                index += 1
                if len(binary) > length:
                    raise Exception('opcodes have to be longer, otherwise there could occur repetitions')
                result[terminal[0]] =  binary
        return result
