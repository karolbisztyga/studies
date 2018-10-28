'''
    @file       ParserTest.py
    @author     Karol Bisztyga (karolbisztyga@gmail.com)
    @date       2018/10/21
    @version    1.0

    @brief
        unit tests for Parser
'''

from studio_projektowe.compiler.src.Parser import Parser
from studio_projektowe.compiler.src.Scanner import Scanner
import unittest


class ParserTest(unittest.TestCase):
    def test_parse(self):
        scanner = Scanner('add([con]20;[reg]r3;[reg]r1);')
        scanner.scan()
        self.assertTrue(Parser().parse(scanner.tokens))