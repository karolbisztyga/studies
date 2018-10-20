from studio_projektowe.compiler.src.Compiler import Compiler
import unittest

class DummyTest(unittest.TestCase):
    def test(self):
        compiler = Compiler()
        compiler.compile(
            'string',
            'add([R]r0,[C]1,[R]r2); sub([C]400,[R]r2,[R]r0);#cmnt; cmp([R] r0, [C] 123, [R] r2)')