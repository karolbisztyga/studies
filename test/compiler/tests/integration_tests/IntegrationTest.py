'''
    @file       IntegrationTest.py
    @author     Karol Bisztyga (karolbisztyga@gmail.com)
    @date       2019/01/10
    @version    1.0

    @brief
        integration tests which verifies whether communication between Scanner Parser and Generator works ok in the
        Compilator's scope
'''
import unittest
from compiler.tests.TestTools import TestsTools
from compiler.src.Compiler import Compiler, IOMethod
from compiler.src.Scanner import Scanner
from compiler.src.Parser import Parser
from compiler.src.Generator import Generator
from compiler.src.App import App
from compiler.src.language.Grammar import Grammar
from compiler.tests.integration_tests.CustomGrammar import CustomGrammar


class IntegrationTestException(Exception):
    pass


class IntegrationTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(IntegrationTest, self).__init__(*args, **kwargs)
        self.test_tools = TestsTools()
        self.test_data = [
            {
                'code': 'add('
                        '   [con] 20;'
                        '   [reg] r3;'
                        '   [reg] r1);',
                'valid': True,
                'grammar': Grammar(),
            },
            {
                'code': 'add('
                        '   [con] 2a0;'
                        '   [reg] r3;'
                        '   [reg] r1);',
                'valid': False,
                'grammar': Grammar(),
            },
            {
                'code': 'aabb',
                'valid': True,
                'grammar': CustomGrammar(),
            },
            {
                'code': 'aabbbcc',
                'valid': False,
                'grammar': CustomGrammar(),
            },
        ]

    def test_compiler_scanner_parser(self):
        # iterate over test data
        for data in self.test_data:
            # prepare variables
            code = data['code']
            valid = data['valid']
            compiler = Compiler(grammar=data['grammar'])
            scanner = Scanner(code, grammar=data['grammar'])
            # perform actions
            try:
                compiler.compile(IOMethod.STRING, '[sec][sec]' + code + '[sec]')
            except:
                pass
            try:
                scanner.scan()
            except:
                pass
            # test results
            if valid:
                self.assertEqual(len(compiler.parser.tokens), len(scanner.tokens))
                for i in range(len(scanner.tokens)):
                    self.assertEqual(compiler.parser.tokens[i].value, scanner.tokens[i].value)
                    self.assertEqual(compiler.parser.tokens[i].type, scanner.tokens[i].type)
                    self.assertEqual(compiler.parser.tokens[i].position, scanner.tokens[i].position)
                    self.assertEqual(compiler.parser.tokens[i].length, scanner.tokens[i].length)
            else:
                self.assertEqual(len(compiler.parser.tokens), 0)

    def test_compiler_parser_generator(self):
        # iterate over test data
        for data in self.test_data:
            # prepare variables
            code = data['code']
            valid = data['valid']
            compiler = Compiler(grammar=data['grammar'])
            scanner = Scanner(code, grammar=data['grammar'])
            parser = Parser(grammar=data['grammar'])
            # perform actions
            try:
                compiler.compile(IOMethod.STRING, '[sec][sec]' + code + '[sec]')
            except:
                pass
            try:
                scanner.scan()
                parser.parse(scanner.tokens)
            except:
                pass
            # test results
            if valid:
                self.assertEqual(len(compiler.generator.tokens), len(parser.tokens))
                for i in range(len(parser.tokens)):
                    self.assertEqual(compiler.generator.tokens[i].value, parser.tokens[i].value)
                    self.assertEqual(compiler.generator.tokens[i].type, parser.tokens[i].type)
                    self.assertEqual(compiler.generator.tokens[i].position, parser.tokens[i].position)
                    self.assertEqual(compiler.generator.tokens[i].length, parser.tokens[i].length)
            else:
                self.assertEqual(len(compiler.generator.tokens), 0)

    def test_compiler_scanner_generator(self):
        # iterate over test data
        for data in self.test_data:
            # prepare variables
            code = data['code']
            valid = data['valid']
            compiler = Compiler(grammar=data['grammar'])
            scanner = Scanner(code, grammar=data['grammar'])
            # perform actions
            try:
                compiler.compile(IOMethod.STRING, '[sec][sec]' + code + '[sec]')
            except:
                pass
            try:
                scanner.scan()
            except:
                pass
            # test results
            if valid:
                self.assertEqual(len(compiler.generator.tokens), len(scanner.tokens))
                for i in range(len(scanner.tokens)):
                    self.assertEqual(compiler.generator.tokens[i].value, scanner.tokens[i].value)
                    self.assertEqual(compiler.generator.tokens[i].type, scanner.tokens[i].type)
                    self.assertEqual(compiler.generator.tokens[i].position, scanner.tokens[i].position)
                    self.assertEqual(compiler.generator.tokens[i].length, scanner.tokens[i].length)
            else:
                self.assertEqual(len(compiler.generator.tokens), 0)

    def test_ui_scanner_parser(self):
        # iterate over test data
        for data in self.test_data:
            # prepare variables
            code = data['code']
            valid = data['valid']
            app = App()
            scanner = Scanner(code, grammar=data['grammar'])
            sample_in = self.test_tools.prepare_sample(code)
            # perform actions
            try:
                cmd = 'app ' + sample_in + ' check_code'
                app.run(cmd.split(' '))
            except:
                pass
            try:
                scanner.scan()
            except:
                pass
            # test results
            if valid:
                self.assertEqual(len(app.parser.tokens), len(scanner.tokens))
                for i in range(len(scanner.tokens)):
                    self.assertEqual(app.parser.tokens[i].value, scanner.tokens[i].value)
                    self.assertEqual(app.parser.tokens[i].type, scanner.tokens[i].type)
                    self.assertEqual(app.parser.tokens[i].position, scanner.tokens[i].position)
                    self.assertEqual(app.parser.tokens[i].length, scanner.tokens[i].length)
            else:
                self.assertIsNone(app.parser)
        self.test_tools.clear_tmp()

    def test_ui_parser_generator(self):
        # iterate over test data
        for data in self.test_data:
            # prepare variables
            app = App()
            code = data['code']
            valid = data['valid']
            compiler = Compiler(grammar=data['grammar'])
            scanner = Scanner(code, grammar=data['grammar'])
            parser = Parser(grammar=data['grammar'])
            sample_in = self.test_tools.prepare_sample('[sec][sec]' + code + '[sec]')
            sample_out = self.test_tools.prepare_sample('')
            # perform actions
            try:
                cmd = 'app ' + sample_in + ' compile ' + sample_out
                app.run(cmd.split(' '))
            except:
                pass
            try:
                scanner.scan()
                parser.parse(scanner.tokens)
            except:
                pass
            # test results
            if valid:
                self.assertEqual(len(app.compiler.generator.tokens), len(parser.tokens))
                for i in range(len(parser.tokens)):
                    self.assertEqual(app.compiler.generator.tokens[i].value, parser.tokens[i].value)
                    self.assertEqual(app.compiler.generator.tokens[i].type, parser.tokens[i].type)
                    self.assertEqual(app.compiler.generator.tokens[i].position, parser.tokens[i].position)
                    self.assertEqual(app.compiler.generator.tokens[i].length, parser.tokens[i].length)
            else:
                self.assertEqual(len(app.compiler.generator.tokens), 0)

    def test_ui_scanner_generator(self):
        # iterate over test data
        for data in self.test_data:
            # prepare variables
            app = App()
            code = data['code']
            valid = data['valid']
            compiler = Compiler(grammar=data['grammar'])
            scanner = Scanner(code, grammar=data['grammar'])
            sample_in = self.test_tools.prepare_sample('[sec][sec]' + code + '[sec]')
            sample_out = self.test_tools.prepare_sample('')
            # perform actions
            try:
                cmd = 'app ' + sample_in + ' compile ' + sample_out
                app.run(cmd.split(' '))
            except:
                pass
            try:
                scanner.scan()
            except:
                pass
            # test results
            if valid:
                self.assertEqual(len(app.compiler.generator.tokens), len(scanner.tokens))
                for i in range(len(scanner.tokens)):
                    self.assertEqual(app.compiler.generator.tokens[i].value, scanner.tokens[i].value)
                    self.assertEqual(app.compiler.generator.tokens[i].type, scanner.tokens[i].type)
                    self.assertEqual(app.compiler.generator.tokens[i].position, scanner.tokens[i].position)
                    self.assertEqual(app.compiler.generator.tokens[i].length, scanner.tokens[i].length)
            else:
                self.assertEqual(len(app.compiler.generator.tokens), 0)
