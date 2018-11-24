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

from compiler.src.Scanner import Scanner
from compiler.src.Parser import Parser
from compiler.src.Generator import Generator
from compiler.src.DataHandler import DataHandler
from compiler.src.BinaryTools import BinaryTools, Endianess
from compiler.src.Exceptions import *

class Compiler:
    SECTION_DELIMITER = '[sec]'
    NUMBER_OF_SECTIONS = 2

    def __init__(self, endianess = None):
        self.endianess = Endianess.LITTLE
        if endianess in [Endianess.LITTLE, Endianess.BIG]:
            self.endianess = endianess

    # input is just an asm code or path to file
    def compile(self, input_method, input_data):
        if input_method not in IOMethod.IO_METHODS:
            raise CompilerException('invalid IO method')
        contents = ''
        if input_method == IOMethod.STRING:
            contents = input_data
        elif input_method == IOMethod.FILE:
            with open(input_data, 'r') as input_file:
                for line in input_file.readlines():
                    contents += str(line)
        if not self.check_sections(contents):
            raise CompilerException('invalid sections, the file has to have ' + Compiler.SECTION_DELIMITER +
                                    ' on the beginning and on the end and has to contain ' +
                                    str(Compiler.NUMBER_OF_SECTIONS) + ' sections')
        contents = contents.split(Compiler.SECTION_DELIMITER)
        data = contents[1]
        code = contents[2]
        # initialize necessary objects
        self.scanner = Scanner(code)
        self.parser = Parser()
        self.generator = Generator()
        self.data_handler = DataHandler()

        #validating data
        if not self.data_handler.validate_data(data):
            raise CompilerException('data validation failed')
        #validating code
        if not self.validate_code(code):
            msg = 'code validation failed\n'
            msg += 'near token ' + str(self.scanner.tokens[self.parser.furthest_token].value)
            raise CompilerException(msg)

        # generating hex codes
        code = self.generator.generate(self.scanner.tokens)
        data = self.data_handler.generate_binary(data)
        # writing to output
        result = b''
        result += self.generate_header(data, code)
        result += data
        result += code

        return result

    def validate_code(self, code):
        try:
            self.scanner.scan()
        except ScannerException as e:
            raise CompilerException(str(e))
        if not self.parser.parse(self.scanner.tokens)[0]:
            return False
        return True

    def generate_header(self, data, code):
        header = b''
        # K0B0V0M0
        MAGIC = 'K\x00B\x00V\x00M\x00'
        header += str.encode(MAGIC)
        header += BinaryTools.number_to_hex(len(data), self.endianess, 8)
        header += BinaryTools.number_to_hex(len(code), self.endianess, 8)
        return header

    def check_sections(self, input_data):
        if input_data[0:len(Compiler.SECTION_DELIMITER)] != Compiler.SECTION_DELIMITER:
            return False
        if input_data[-len(Compiler.SECTION_DELIMITER):] != Compiler.SECTION_DELIMITER:
            return False
        if len(input_data.split(Compiler.SECTION_DELIMITER)) != Compiler.NUMBER_OF_SECTIONS + 2:
            return False
        return True

class IOMethod:
    STRING = 'string'
    FILE = 'file'
    IO_METHODS = [STRING, FILE]