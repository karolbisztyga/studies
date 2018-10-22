'''
    @file       Scanner.py
    @author     Karol Bisztyga (karolbisztyga@gmail.com)
    @date       2018/10/20
    @version    1.0

    @input - code as string
    @output - list of Token class objects
    @brief
        removing redundant elements of the code(spaces, comments etc)
        generating a list of tokens from given code
'''
from studio_projektowe.compiler.src.Grammar import Grammar

class Scanner:
    def __init__(self):
        self.grammar = Grammar()

    def scan(self, code):
        self.__clear_code()
        self.__generate_tokens()

    def clear_code(self, code):
        # remove spaces, tabs, newlines etc.
        content_to_remove = ['\t', '\r', '\n', ' ']
        for i in content_to_remove:
            code = code.replace(i, '')
        # remove comments
        while True:
            comment_start_index = code.find(self.grammar.COMMENT_START)
            if comment_start_index == -1:
                break
            comment_end_index = code.find(self.grammar.COMMENT_END, comment_start_index)
            if comment_end_index == -1:
                comment_end_index = len(code)
            else:
                comment_end_index += 1
            code = code[0:comment_start_index] + code[comment_end_index:len(code)]
        return code

    def generate_tokens(self, code):
        pass
