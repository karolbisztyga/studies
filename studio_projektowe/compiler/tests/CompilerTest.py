'''
    @file       CompilerTest.py
    @author     Karol Bisztyga (karolbisztyga@gmail.com)
    @date       2018/10/21
    @version    1.0

    @brief
        unit tests for Compiler
'''

from studio_projektowe.compiler.src.Compiler import Compiler, IOMethod
from studio_projektowe.compiler.src.Exceptions import CompilerException
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

    def test_compile(self):
        compiler = Compiler()
        # data to be tested
        code_samples = [
            '[sec]hello123[sec]add([con]20;[reg]r3;[reg]r1);[sec]',
            '[sec]abcdefghijklmnoprstuwvxyz1234567890[sec][sec]',
            '''[sec]884567733575[sec]
                psh([mem] dwd, 3);
                pop([reg] r3);
                cmp([mem] byt, 5; [reg] r7; [reg] r0);
            [sec]''',
            '[sec][sec]add([reg]r0; [reg]r1; [reg]r2);[sec]'
        ]
        # expected data
        expected_results = [
            b'\x4B\x00\x42\x00\x56\x00\x4D\x00\x08\x00\x00\x00\x00\x00\x00\x00\x2E\x00\x00\x00\x00\x00\x00\x00\x68\x65\x6C\x6C\x6F\x31\x32\x33\x02\x00\x26\x00\x28\x00\x1A\x00\x29\x00\x2C\x00\x2A\x00\x14\x00\x00\x00\x00\x00\x00\x00\x24\x00\x28\x00\x19\x00\x29\x00\x1F\x00\x24\x00\x28\x00\x19\x00\x29\x00\x1D\x00\x27\x00\x24\x00',
            b'\x4B\x00\x42\x00\x56\x00\x4D\x00\x23\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6A\x6B\x6C\x6D\x6E\x6F\x70\x72\x73\x74\x75\x77\x76\x78\x79\x7A\x31\x32\x33\x34\x35\x36\x37\x38\x39\x30',
            b'\x4B\x00\x42\x00\x56\x00\x4D\x00\x0C\x00\x00\x00\x00\x00\x00\x00\x5C\x00\x00\x00\x00\x00\x00\x00\x38\x38\x34\x35\x36\x37\x37\x33\x33\x35\x37\x35\x0A\x00\x26\x00\x28\x00\x1B\x00\x29\x00\x17\x00\x25\x00\x2D\x00\x03\x00\x00\x00\x00\x00\x00\x00\x27\x00\x24\x00\x00\x00\x26\x00\x28\x00\x19\x00\x29\x00\x1F\x00\x27\x00\x24\x00\x0C\x00\x26\x00\x28\x00\x1B\x00\x29\x00\x15\x00\x25\x00\x2F\x00\x05\x00\x00\x00\x00\x00\x00\x00\x24\x00\x28\x00\x19\x00\x29\x00\x23\x00\x24\x00\x28\x00\x19\x00\x29\x00\x1C\x00\x27\x00\x24\x00',
            b'\x4B\x00\x42\x00\x56\x00\x4D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x24\x00\x00\x00\x00\x00\x00\x00\x02\x00\x26\x00\x28\x00\x19\x00\x29\x00\x1C\x00\x24\x00\x28\x00\x19\x00\x29\x00\x1D\x00\x24\x00\x28\x00\x19\x00\x29\x00\x1E\x00\x27\x00\x24\x00',
        ]
        # perform tests
        results = []
        for sample in code_samples:
            results.append(compiler.compile(IOMethod.STRING, sample))
        self.assertRaises(CompilerException, compiler.compile, None, '[sec]asd[sec]add([reg]r0; [reg]r1; [reg]r2);[sec]')
        self.assertRaises(CompilerException, compiler.compile, IOMethod.STRING, ' [sec]asd[sec]add([reg]r0; [reg]r1; [reg]r2);[sec]')
        self.assertRaises(CompilerException, compiler.compile, IOMethod.STRING, ' [sec]asd[sec]add([reg]r0; [reg]r1; [reg]r2);[sec] ')
        self.assertRaises(CompilerException, compiler.compile, IOMethod.STRING, '[sec]asd[sec]add([reg]r0; [reg]r1; [reg]2);[sec]')
        self.assertRaises(CompilerException, compiler.compile, IOMethod.STRING, '[sec]asd[sec]add([reg]r0; [reg]r1; [reg]r2;[sec]')
        # compare results
        self.assertEqual(len(results), len(code_samples))
        self.assertEqual(len(expected_results), len(results))
        for i in range(len(results)):
            self.assertEqual(results[i], expected_results[i])
