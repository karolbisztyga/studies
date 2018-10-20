'''
    @file       Token.py
    @author     Karol Bisztyga (karolbisztyga@gmail.com)
    @date       2018/10/20
    @version    1.0

    @brief
        container for tokens obtained from code
'''

class Token:
    def __init__(self, type, value, position):
        self.__type = type
        self.__value = value
        self.__position = position