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
from compiler.src.language.Grammar import Grammar
from compiler.src.BinaryTools import BinaryTools, Endianess
from compiler.src.Token import *
from compiler.src.Exceptions import *
from compiler.src.language.OpcodesGenerator import OpcodesGenerator


class Generator:
    def __init__(self, endianess = None, grammar=Grammar(), opcodes_generator=OpcodesGenerator()):
        self.grammar = grammar
        self.opcodes_generator = opcodes_generator
        self.opcodes = self.opcodes_generator.generate()
        self.endianess = Endianess.LITTLE
        if endianess in [Endianess.LITTLE, Endianess.BIG]:
            self.endianess = endianess

    def generate(self, tokens):
        result = b''
        curr_num = None
        for token in tokens:
            if token.value not in self.opcodes:
                raise GeneratorException('unrecognized token in generator: ' + str(token))
            if token.type == TokenType.NUMBER:
                if curr_num is None:
                    curr_num = token.value
                else:
                    curr_num += token.value
            else:
                # this happens when we finished collecting current number so it is ready to get it's representation
                if curr_num != None:
                    he = BinaryTools.number_to_hex(int(curr_num), self.endianess, BinaryTools.NUMBER_BYTE_LENGTH)
                    result += he
                    curr_num = None
            bin = self.opcodes[token.value]
            dec = int(bin, 2)
            he = BinaryTools.number_to_hex(dec, self.endianess, BinaryTools.OPCODE_BYTE_LENGTH)
            result += he
        return result

