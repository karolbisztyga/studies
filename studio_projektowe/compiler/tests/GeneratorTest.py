'''
    @file       GeneratorTest.py
    @author     Karol Bisztyga (karolbisztyga@gmail.com)
    @date       2018/10/21
    @version    1.0

    @brief
        unit tests for Generator
'''

from studio_projektowe.compiler.src.Generator import Generator
from studio_projektowe.compiler.src.Scanner import Scanner
from studio_projektowe.compiler.src.Parser import Parser
import unittest


class GeneratorTest(unittest.TestCase):

    def test_generate(self):
        generator = Generator()
        # data to be tested
        code_samples = [
            'add([con]20;[reg]r3;[reg]r1);',
            '''
                psh([mem] dwd, 34634);
                pop([reg] r3);
                cmp([mem] byt, 456452; [reg] r7; [reg] r0);
            ''',
            '# i wanna copy memory value into register;  cpy([mem]dwd, 14234; [reg]r7); # and then add it to current value;  add([reg]r0;[reg] r7; [reg ]r0) ;',

        ]
        # expected data
        expected_results = [
            b'\x02\x00&\x00(\x00\x1a\x00)\x00,\x00*\x00\x14\x00\x00\x00\x00\x00\x00\x00$\x00(\x00\x19\x00)\x00\x1f\x00$\x00(\x00\x19\x00)\x00\x1d\x00\x27\x00$\x00',
            b'\n\x00&\x00(\x00\x1b\x00)\x00\x17\x00%\x00-\x00.\x000\x00-\x00.\x00J\x87\x00\x00\x00\x00\x00\x00\x27\x00$\x00\x00\x00&\x00(\x00\x19\x00)\x00\x1f\x00\x27\x00$\x00\x0c\x00&\x00(\x00\x1b\x00)\x00\x15\x00%\x00.\x00/\x000\x00.\x00/\x00,\x00\x04\xf7\x06\x00\x00\x00\x00\x00$\x00(\x00\x19\x00)\x00#\x00$\x00(\x00\x19\x00)\x00\x1c\x00\x27\x00$\x00',
            b'\x01\x00&\x00(\x00\x1b\x00)\x00\x17\x00%\x00+\x00.\x00,\x00-\x00.\x00\x9a7\x00\x00\x00\x00\x00\x00$\x00(\x00\x19\x00)\x00#\x00\x27\x00$\x00\x02\x00&\x00(\x00\x19\x00)\x00\x1c\x00$\x00(\x00\x19\x00)\x00#\x00$\x00(\x00\x19\x00)\x00\x1c\x00\x27\x00$\x00',
        ]
        # perform tests
        results = []
        for sample in code_samples:
            scanner = Scanner(sample)
            scanner.scan()
            if(not Parser().parse(scanner.tokens)[0]):
                print('parser failed!')
            else:
                binary = generator.generate(scanner.tokens)
                results.append(binary)

        # compare results
        self.assertEqual(len(results), len(code_samples))
        self.assertEqual(len(expected_results), len(results))
        for i in range(len(results)):
            self.assertEqual(results[i], expected_results[i])