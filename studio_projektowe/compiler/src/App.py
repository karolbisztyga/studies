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
from studio_projektowe.compiler.src.Exceptions import AppException

class App:

    def __init__(self):
        self.compiler = Compiler()

    def help(self):
        print('HELP')
        print('calling the compiler: python3 studio_projektowe [path_to_input_file] [action] [path_to_output_file(optional)]')
        print('  arguments:')
        print('    [path_to_input_file]')
        print('    [path_to_input_file(optional)]')
        print('    [action] you can choose one of the following options:')
        print('      minify_code')
        print('      check_code - does not produce any output file(the output_file_path is not used), just prints a message if the code is syntax valid')
        print('      compile - default')


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
                valid = self.check(input_file_data)
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
                    raise AppException('an error occured, broken output')
                with open(output_file_path, opening_options) as file:
                    file.write(result)
                print('compilation successful, output file: ' + str(output_file_path))
        except AppException as e:
            print('an error occured: ' + str(e))
            if show_help_on_exception:
                print('see help')
                self.help()

    def compile(self, file_path):
        compiled = b''
        try:
            compiled = self.compiler.compile(IOMethod.STRING, file_path)
        except Exception as e:
            raise AppException(str(e))
        return compiled

    def check(self, file_path):
        # TODO
        pass

    def minify(self, file_path):
        # TODO
        pass

class Actions:
    MINIFY = 'minify_code'
    CHECK = 'check_code'
    COMPILE = 'compile'