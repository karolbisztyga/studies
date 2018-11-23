'''
    @file       App.py
    @author     Karol Bisztyga (karolbisztyga@gmail.com)
    @date       2018/11/19
    @version    1.0

    @brief
        here goes the logic of interaction with user
'''
import os, glob
from studio_projektowe.compiler.src.Compiler import Compiler, IOMethod
from studio_projektowe.compiler.src.Exceptions import AppException, ParserException, ScannerException, CompilerException
from studio_projektowe.compiler.src.Scanner import Scanner
from studio_projektowe.compiler.src.Parser import Parser

class App:

    def help(self):
        print('HELP')
        print('calling the compiler: python3 studio_projektowe [path_to_input_file] [action] [path_to_output_file(optional)]')
        print('  arguments:')
        print('    [path_to_input_file]')
        print('    [action] you can choose one of the following options:')
        print('      minify_code')
        print('      check_code - does not produce any output file(the output_file_path is not used), just prints a message if the code is syntax valid')
        print('      compile - default')
        print('    [path_to_output_file(optional)]')


    def run(self, args):
        show_help_on_exception = True
        try:
            print('KBVM compiler version 1.0')
            if len(args) not in [3, 4]:
                raise AppException('invalid arguments ' + str(args))
            input_file_path = args[1]
            action = args[2]
            output_file_path = None
            if action not in [Actions.MINIFY, Actions.CHECK, Actions.COMPILE]:
                raise AppException('invalid action: ' + str(action))
            if action != Actions.CHECK:
                if len(args) != 4:
                    raise AppException('no output file provided')
                output_file_path = args[3]
            # check the input file path
            if not os.path.isfile(input_file_path):
                show_help_on_exception = False
                raise AppException('the file ' + str(input_file_path) + ' does not exist')
            # get the absolute path of input file
            input_file_path = os.path.abspath(input_file_path)
            input_file_data = ''
            with open (input_file_path, 'r') as file:
                input_file_data = file.read()
            # perform desired action
            show_help_on_exception = False
            if action == Actions.CHECK:
                compiler = Compiler()
                valid = False
                try:
                    valid = self.check(input_file_data)
                except Exception as e:
                    raise AppException(str(e))
                if valid:
                    print('1 the code is valid')
                else:
                    print('0 the code is not valid')
            else:
                # the output file is needed so check for existence
                if output_file_path == None:
                    raise AppException('output file error')
                result = None
                opening_options = 'w'
                if action == Actions.MINIFY:
                    result = self.minify(input_file_data)
                elif action == Actions.COMPILE:
                    opening_options += 'b'
                    result = self.compile(input_file_data)
                if result == None:
                    raise AppException('broken output')
                with open(output_file_path, opening_options) as file:
                    file.write(result)
                print('compilation successful, output file: ' + str(output_file_path))
        except AppException as e:
            print('an error occured: ' + str(e))
            if show_help_on_exception:
                print('see help')
                self.help()
            return False
        return True

    def compile(self, file_data):
        compiled = b''
        try:
            compiler = Compiler()
            compiled = compiler.compile(IOMethod.STRING, file_data)
        except Exception as e:
            raise AppException(str(e))
        return compiled

    def minify(self, file_data):
        try:
            scanner = Scanner(file_data)
            scanner.scan()
            parser = Parser()
            parse_result = parser.parse(scanner.tokens)
            # only if the code is valid return the minified code
            if not parse_result[0]:
                msg = 'code validation failed\n'
                msg += 'near token ' + str(scanner.tokens[parser.furthest_token].value)
                raise ParserException(msg)
            return scanner.code
        except Exception as e:
            raise AppException(str(e))

    def check(self, file_data):
        scanner = Scanner(file_data)
        try:
            scanner.scan()
        except ScannerException as e:
            raise CompilerException(str(e))
        parser = Parser()
        if not parser.parse(scanner.tokens)[0]:
            return False
        return True

class Actions:
    MINIFY = 'minify_code'
    CHECK = 'check_code'
    COMPILE = 'compile'