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
from studio_projektowe.compiler.src.DataHandler import DataHandler
from studio_projektowe.compiler.src.BinaryTools import BinaryTools, Endianess
from studio_projektowe.compiler.src.Exceptions import *
from binascii import unhexlify
import os

class Compiler:

    def __init__(self, endianess = None):
        self.SECTION_DELIMITER = '[sec]'
        self.NUMBER_OF_SECTIONS = 2
        self.endianess = Endianess.LITTLE
        if endianess in [Endianess.LITTLE, Endianess.BIG]:
            self.endianess = endianess

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
            raise CompilerException('code validation failed')

        # writing to output
        result = b''
        result += self.generate_header(data, code)

        result += self.generator.generate(self.scanner.tokens)

        # this code will be moved to another handler
        with open('out.bin', 'wb') as file:
            file.write(result)

        return result

    def validate_code(self, code):
        try:
            self.scanner.scan()
            if not self.parser.parse(self.scanner.tokens)[0]:
                return False
        except:
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