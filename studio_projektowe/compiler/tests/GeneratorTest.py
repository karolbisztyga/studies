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
            b'00000010001001100010100000011010001010010010110000101010001001000010100000011001001010010001111100100100001010000001100100101001000111010010011100100100',
            b'0000101000100110001010000001101100101001000101110010010100101101001011100011000000101101001011100010011100100100000010110010011000101000000110010010100100011111001001110010010000001100001001100010100000011011001010010001010100100101001011100010111100110000001011100010111100101100001001000010100000011001001010010010001100100100001010000001100100101001000111000010011100100100',
            b'00000001001001100010100000011011001010010001011100100101001010110010111000101100001011010010111000100100001010000001100100101001001000110010011100100100000000100010011000101000000110010010100100011100001001000010100000011001001010010010001100100100001010000001100100101001000111000010011100100100',
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