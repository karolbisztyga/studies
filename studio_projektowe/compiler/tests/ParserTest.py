'''
    @file       ParserTest.py
    @author     Karol Bisztyga (karolbisztyga@gmail.com)
    @date       2018/10/21
    @version    1.0

    @brief
        unit tests for Parser
'''

from compiler.src.Parser import Parser
from compiler.src.Scanner import Scanner
import unittest


class ParserTest(unittest.TestCase):
    def test_parse(self):
        # data to be tested
        code_samples = [
            'add([con]20;[reg]r3;[reg]r1);',
            'cpy([mem]byt, 454353452;[reg]r3); #comment; xor ([mem]qwd , 4534;[con]3424233234;[reg]r7); #print it out; out([reg]r7);',
            'add([reg]r0;[con]1;[reg]r1);sub([con]400;[reg]r1;[reg]r0);cmp([reg]r0;[con]123;[reg]r7);',
            '# i wanna copy memory value into register;  cpy([mem]dwd, 14234; [reg]r7); # and then add it to current value;  add([reg]r0;[reg] r7; [reg ]r0) ;',
            '''
            psh([mem] dwd, 34634);
            pop([reg] r3);
            cmp([mem] byt, 456452; [reg] r7; [reg] r0);
            ''',
            '''
                psh([mem] dwd, 34634);
                pop([mem] r3);
                cmp([mem] byt, 456452; [reg] r7; [reg] r0);
            ''',
            'add([con]r6;[reg]r3;[reg]r1);',
            'add([reg]433542;[reg]r3;[reg]r1);',
            'add([mem]433542, byt;[reg]r3;[reg]r1);',
            'add([mem]byt, 433542;[reg]r3;[reg]2);',
            'ret([mem] qwd, 67567567);',
            'exe([reg] r3);',
            'exe([con] 567567);',
            'exe([mem] dwd, 567567);',
            'exe([con] 567567)',
        ]

        for i in ['add', 'sub', 'mul', 'div', 'and', 'lor', 'xor', 'cmp']:
            code_samples += [
                i + '([mem]byt, 123129; [con] 454575; [reg]r2);',
                i + '([mem]byt, 123129; [con] 454575 ;[mem]qwd, 34646445);',
                i + '([mem]byt, 123129; [con] 454575; [con] 3454352);',
            ]
        code_samples += [
            'not([reg] r1; [reg] r4);',
            'not([reg] r1; [mem] byt, 36456);',
            'not([reg] r1; [con] 44444);',
        ]
        code_samples += [
            'pop([reg] r7);',
            'pop([mem] qwd, 45457567);',
            'pop([con] 948561);',
        ]
        # expected data
        expected_results = [
            (True, 19),
            (True, 63),
            (True, 58),
            (True, 37),
            (True, 47),
            (False, 0),
            (False, 0),
            (False, 0),
            (False, 0),
            (False, 0),
            (False, 0),
            (True, 8),
            (True, 13),
            (False, 0),
            (False, 0),
        ]

        for arithmetical_logical_method in ['add', 'sub', 'mul', 'div', 'and', 'lor', 'xor', 'cmp']:
            expected_results += [
                (True, 30),
                (False, 0),
                (False, 0),
            ]
        expected_results += [
                (True, 13),
                (False, 0),
                (False, 0),
        ]
        expected_results += [
                (True, 8),
                (False, 0),
                (False, 0),
        ]

        # perform tests
        self.assertEqual(len(code_samples), len(expected_results))
        results = []
        for sample in code_samples:
            scanner = Scanner(sample)
            scanner.scan()
            results.append(Parser().parse(scanner.tokens))

        self.assertEqual(len(results), len(expected_results))
        # compare results
        for i in range(len(results)):
            self.assertEqual(results[i], expected_results[i])
