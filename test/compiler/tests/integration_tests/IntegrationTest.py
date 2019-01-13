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


class IntegrationTestException(Exception):
    pass


class IntegrationTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(IntegrationTest, self).__init__(*args, **kwargs)
        self.test_tools = TestsTools()
