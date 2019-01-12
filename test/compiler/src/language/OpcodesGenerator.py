'''
    @file       OpcodesGenerator.py
    @author     Karol Bisztyga (karolbisztyga@gmail.com)
    @date       2018/10/20
    @version    1.0

    @input - list of Token class objects
    @output - bytecode
    @brief
        it holds the logic responsible for generating opcodes for the tokens of given grammar
'''
from compiler.src.language.Grammar import Grammar
from compiler.src.BinaryTools import BinaryTools


class OpcodesGenerator:
    def __init__(self, grammar=None):
        self.grammar = grammar
        if self.grammar is None:
            self.grammar = Grammar()

    def generate(self):
        result = {}
        index = 1
        for terminal_length, terminal_arr in self.grammar.TERMINALS.items():
            for terminal in terminal_arr:
                binary = BinaryTools.fill_with_zeros(str.encode(bin(index).replace('0b', '')))
                index += 1
                if len(binary) > BinaryTools.OPCODE_BYTE_LENGTH * 8:
                    raise Exception('opcodes have to be longer, otherwise there could occur repetitions')
                result[terminal[0]] = binary
        return result
