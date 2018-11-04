'''
    @file       CompilerTest.py
    @author     Karol Bisztyga (karolbisztyga@gmail.com)
    @date       2018/10/21
    @version    1.0

    @brief
        unit tests for Compiler
'''

from studio_projektowe.compiler.src.Compiler import Compiler
import unittest


class CompilerTest(unittest.TestCase):

    def test_sections(self):
        compiler = Compiler()
        # data to be tested
        code_samples = [
            '[sec]sf3nroehey!1234567890very important stuff:)[sec]add([reg] r1; [mem] byt, 2; [reg] r0); out([reg] r0); out([mem] qwd, 7);[sec]',
            '[sec]swewfewf44r23rwef[sec]qd32e3232234455[sec]',
            '[sec][sec][sec]',
            '[sec]add([con]20;[reg]r3;[reg]r1);[sec]',
            '[sec]hello123[ sec]add([con]20;[reg]r3;[reg]r1);[sec]',
            '        sadasdsadasd[sec]hello123 [sec] add([con]20;[reg]r3;[reg]r1);   [sec]   ',
            '[sec]hello123[sec]hello123[sec]add([con]20;[reg]r3;[reg]r1);[sec]',
        ]
        # expected data
        expected_results = [
            True,
            True,
            True,
            False,
            False,
            False,
            False,

        ]
        # perform tests
        results = []
        for sample in code_samples:
            result = compiler.check_sections(sample)
            results.append(result)
        # compare results
        self.assertEqual(len(results), len(code_samples))
        self.assertEqual(len(expected_results), len(results))
        for i in range(len(results)):
            self.assertEqual(results[i], expected_results[i])