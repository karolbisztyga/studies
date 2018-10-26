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
from studio_projektowe.compiler.src.Token import Token, TokenType
from studio_projektowe.compiler.src.Exceptions import *

class Scanner:
    def __init__(self, code):
        self.grammar = Grammar()
        self.code = code
        self.code_clean = False
        self.tokens = []

    def scan(self):
        self.clear_code()
        self.generate_tokens()

    def clear_code(self):
        # remove spaces, tabs, newlines etc.
        content_to_remove = ['\t', '\r', '\n', ' ']
        for i in content_to_remove:
            self.code = self.code.replace(i, '')
        # remove comments
        while True:
            comment_start_index = self.code.find(self.grammar.COMMENT_START)
            if comment_start_index == -1:
                break
            comment_end_index = self.code.find(self.grammar.COMMENT_END, comment_start_index)
            if comment_end_index == -1:
                comment_end_index = len(self.code)
            else:
                comment_end_index += 1
            self.code = self.code[0:comment_start_index] + self.code[comment_end_index:len(self.code)]
        self.code_clean = True

    def generate_tokens(self):
        if not self.code_clean:
            raise ScannerException('cannot generate tokens without clean code')
        pos = 0
        while pos < len(self.code):
            current_terminal = None
            token_start_pos = pos
            token_end_pos = min(pos+self.grammar.MAX_TERMINAL_LENGTH, len(self.code))
            token_candidate = self.code[token_start_pos:token_end_pos]
            token_found = self.__find_token(token_candidate, pos)
            if token_found is None:
                self.tokens.clear()
                raise ScannerException('failed to fetch token: ' + str(token_candidate))
            pos += token_found.length
            # concatenate numbers with multiple digits
            if token_found.type == TokenType.NUMBER:
                if self.tokens[-1].type == TokenType.NUMBER:
                    self.tokens[-1].value += token_found.value
                    continue
            self.tokens.append(token_found)



    # passed value must be as long as MAX_TERMINAL_LENGTH
    def __find_token(self, value, position):
        try:
            if len(value) > self.grammar.MAX_TERMINAL_LENGTH:
                raise GrammarException('find token: value of length 3 expected, got ' + str(value) + ' of length ' + str(len(value)))
            for terminal_length in range(self.grammar.MAX_TERMINAL_LENGTH):
                terminal_length += 1
                value_edited = value[0:terminal_length]
                for terminal, type in self.grammar.TERMINALS[terminal_length]:
                    if terminal[0:terminal_length] == value_edited:
                        return Token(terminal, type, terminal_length, position)
        except:
            return None
        return None
