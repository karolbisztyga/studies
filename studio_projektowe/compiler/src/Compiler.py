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
from studio_projektowe.compiler.src.Exceptions import *

class Compiler:

    def __init__(self):
        self.SECTION_DELIMITER = '[sec]'
        self.NUMBER_OF_SECTIONS = 2

    # input is just an asm code or path to file
    def compile(self, input_method, input_data):
        if input_method not in IOMethod.IO_METHODS:
            raise Exception('invalid IO method')
        contents = ''
        if input_method == IOMethod.STRING:
            contents = input_data
        elif input_method == IOMethod.FILE:
            with open(input_data, 'r') as input_file:
                for line in input_file.readlines():
                    contents += str(line)
        if not self.check_sections(contents):
            raise CompilerException('invalid sections, the file has to have ' + self.SECTION_DELIMITER +
                                    ' on the beginning and on the end and has no contain ' +
                                    str(self.NUMBER_OF_SECTIONS) + ' sections')
        contents = contents.split(self.SECTION_DELIMITER)
        data = contents[1]
        code = contents[2]
        # call parser, scanner and generator on given code
        #self.__scanner = Scanner()
        #self.__parser = Parser()
        #self.__generator = Generator()
        # TODO call scanner parser and generator
        # TODO handle data and code separately, the best option is to validate them both
        # TODO and after validation save them to a file, fisrt saving a properly preparated header

    def check_sections(self, input_data):
        if input_data[0:len(self.SECTION_DELIMITER)] != self.SECTION_DELIMITER:
            return False
        if input_data[-len(self.SECTION_DELIMITER):] != self.SECTION_DELIMITER:
            return False
        if len(input_data.split(self.SECTION_DELIMITER)) != self.NUMBER_OF_SECTIONS + 2:
            return False
        return True

class IOMethod:
    STRING = 'string'
    FILE = 'file'
    IO_METHODS = [STRING, FILE]