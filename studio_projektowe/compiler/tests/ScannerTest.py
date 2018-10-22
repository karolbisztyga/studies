'''
    @file       ScannerTest.py
    @author     Karol Bisztyga (karolbisztyga@gmail.com)
    @date       2018/10/21
    @version    1.0

    @brief
        unit tests for Scanner
'''

from studio_projektowe.compiler.src.Scanner import Scanner
from studio_projektowe.compiler.src.Exceptions import *
import unittest


class ScannerTest(unittest.TestCase):
    def test_clear_code(self):
        # data to be tested
        test_data = [
            '''
                Maecenas augue magna,
                \tmollis ac magna sit amet,
                suscipit posuere neque.
                \t\tEtiam malesuada leo eu
                lorem pellentesque porttitor.
                \tVivamus diam urna,
                  condimentum   eu volutpat
                a, luctus ultrices
                justo.
            ''',
            '''
                Maecenas augue magna, #mollis 
                ac magna sit amet;, suscipit 
                posuere neque. #Etiam malesuada 
                leo eu lorem; pellentesque; porttitor
                . #Vivamus #diam ##urna, ###condimentum
                 #eu ;volutpat ;a, ;luctus #ultrices ;
                 justo.# Etiam ac massa
            ''',
        ]
        # expected data
        expected_data = [
            'Maecenasauguemagna,mollisacmagnasitamet,suscipitposuereneque.Etiammalesuadaleoeulorempellentesqueporttitor.Vivamusdiamurna,condimentumeuvolutpata,luctusultricesjusto.',
            'Maecenasauguemagna,,suscipitposuereneque.pellentesque;porttitor.volutpat;a,;luctusjusto.',
        ]
        # perform tests
        results = []
        for test in test_data:
            scanner = Scanner(test)
            scanner.clear_code()
            results.append(scanner.code)
        # compare results
        self.assertEqual(len(results), len(test_data))
        self.assertEqual(len(expected_data), len(test_data))
        for i in range(0, len(results)):
            self.assertEqual(results[i], expected_data[i])

    def test_generate_tokens(self):
        test_data = [
            'add([reg]r0;[con]1;[reg]r1);sub([con]400;[reg]r1;[reg]r0);cmp([reg]r0;[con]123;[reg]r7)'
        ]
        scanner = Scanner(test_data)
        self.assertRaises(ScannerException, scanner.generate_tokens)

    def test_scan(self):
        # data to be tested
        test_data = [
            'add([reg]r0;[con]1;[reg]r1);sub([con]400;[reg]r1;[reg]r0);cmp([reg]r0;[con]123;[reg]r7)',
            '# i wanna copy memory value into register;  cpy([mem]14234; [reg]r7); # and then add it to current value;  add([reg]r0;[reg] r7; [reg ]r0) ;',
            'not([reg]r5; [reg]r1); pop # test endless comment', # this contains syntax error but it is not checked in scanner
            'jeq([con]14324112; [reg] r4; [reg] r2); copy([reg]r2;reg[r6]);', # 'copy' should fire an exception
        ]
        # expected data - number of tokens
        expected_data = [
            53,
            31,
            14,
            0,
        ]
        # perform tests
        results = []
        for test in test_data:
            scanner = Scanner(test)
            try:
                scanner.scan()
            except ScannerException:
                pass
            results.append((len(scanner.tokens)))
        # compare results
        self.assertEqual(len(results), len(test_data))
        self.assertEqual(len(expected_data), len(test_data))
        for i in range(0, len(results)):
            self.assertEqual(results[i], expected_data[i])