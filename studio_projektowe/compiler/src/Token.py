'''
    @file       Token.py
    @author     Karol Bisztyga (karolbisztyga@gmail.com)
    @date       2018/10/20
    @version    1.0

    @brief
        container for tokens obtained from code
'''

class Token:
    def __init__(self, value, type, length, position):
        self.value = value
        self.type = type
        self.position = position
        self.length = length


class TokenType:
    INSTRUCTION_LABEL = 'INSTRUCTION_LABEL'
    DELIMITER = 'DELIMITER'
    NUMBER = 'NUMBER'
    REGISTER_LABEL = 'REGISTER_LABEL'
    ACCESS_TYPE = 'ACCESS_TYPE'
    ARGUMENT_TYPE = 'ARGUMENT_TYPE'

    TYPES = [INSTRUCTION_LABEL, DELIMITER, NUMBER, REGISTER_LABEL, ACCESS_TYPE, ARGUMENT_TYPE]