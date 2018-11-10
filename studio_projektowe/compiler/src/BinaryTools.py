'''
    @file       BinaryTools.py
    @author     Karol Bisztyga (karolbisztyga@gmail.com)
    @date       2018/11/10
    @version    1.0

    @brief this class provides a set of independent methods which help in binary data handling
'''

class BinaryTools:
    BYTE_LENGTH = 8

    def print_bytes(bits):
        result = ''
        index = 1
        for c in bits:
            result += c
            if index > 0 and index % BinaryTools.BYTE_LENGTH == 0:
                result += ' '
            index += 1
        return result

    # fills given bytes with zeros to make their length % BYTE_LENGTH = 0 without changing value
    def fill_with_zeros(binary):
        for i in range(0, BinaryTools.BYTE_LENGTH - len(binary)):
            binary = b'0' + binary
        return binary