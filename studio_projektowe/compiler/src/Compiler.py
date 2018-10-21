'''
    @file       Compiler.py
    @author     Karol Bisztyga (karolbisztyga@gmail.com)
    @date       2018/10/20
    @version    1.0

    @input - asm code(string or file)
    @output - binary code(string or file)
    @brief
        - receives asm code as string or file
        - passes the code to the scanner to obtain tokens
        - passes the tokens to the parser to validate the syntax
        - passes the tokens to the generator to obtain byte code
        - returns bytecode as string or writes it to file
'''

from studio_projektowe.compiler.src.Scanner import Scanner
from studio_projektowe.compiler.src.Parser import Parser
from studio_projektowe.compiler.src.Generator import Generator

class Compiler:

    def __init__(self):
        self.__scanner = Scanner()
        self.__parser = Parser()
        self.__generator = Generator()

    # input is just an asm code or path to file
    def compile(self, input_method, input_data):
        if input_method not in IOMethod.IO_METHODS:
            raise Exception('invalid IO method')
        code = ''
        if input_method == IOMethod.STRING:
            code = input_data
        elif input_method == IOMethod.FILE:
            with open(input_data, 'r') as input_file:
                for line in input_file.readlines():
                    code += str(line)
        # todo call scanner parser and generator

class IOMethod:
    STRING = 'string'
    FILE = 'file'
    IO_METHODS = [STRING, FILE]