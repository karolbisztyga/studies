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
from studio_projektowe.compiler.src.BinaryTools import BinaryTools
from studio_projektowe.compiler.src.Exceptions import *
import os

class Compiler:

    def __init__(self):
        self.SECTION_DELIMITER = '[sec]'
        self.NUMBER_OF_SECTIONS = 2
        self.endianess = Endianess.LITTLE

    # input is just an asm code or path to file
    # output should be file name or if it is None then it will be written to std out
    def compile(self, input_method, input_data, output_path = None):
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

        # prepare output if necessary
        output = None
        if output_path is not None:
            try:
                with open(output_path, 'wb') as file:
                    pass
                if not os.path.isfile(output_path):
                    raise CompilerException('could not create such file: ' + str(output_path))
            except:
                raise CompilerException('error while handling given path: ' + str(output_path))
            output = open(output_path, 'wb')

        # writing to output
        self.write_header(output)
        self.write_data(output, data)
        self.write_code(output, code)

    def validate_code(self, code):
        try:
            self.scanner.scan()
            if not self.parser.parse(self.scanner.tokens)[0]:
                return False
        except:
            return False
        return True

    def write_header(self, output, data, code):
        header = b''
        MAGIC = 'K0B0V0M0'
        #data_size = BinaryTools.fill_with_zeros(bin(len(data)))
        #code_size = len(code)
        # TODO finish
        if output is None:
            print(header)
        else:
            output.write(header)

    def write_data(self, output, data):
        # TODO
        pass

    def write_code(self, output, code):
        # TODO
        pass

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

class Endianess:
    LITTLE = 'little_endian'
    BIG = 'big_endian'