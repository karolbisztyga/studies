'''
    @file       BinaryTools.py
    @author     Karol Bisztyga (karolbisztyga@gmail.com)
    @date       2018/11/10
    @version    1.0

    @brief this class provides a set of independent methods which help in binary data handling
'''
from studio_projektowe.compiler.src.Exceptions import BinaryToolsException
from binascii import unhexlify

class Endianess:
    LITTLE = 'little_endian'
    BIG = 'big_endian'

class BinaryTools:
    BYTE_LENGTH = 8
    NUMBER_BYTE_LENGTH = 8
    OPCODE_BYTE_LENGTH = 2

    def print_binary(bits):
        result = ''
        index = 1
        for c in bits:
            result += c
            if index > 0 and index % BinaryTools.BYTE_LENGTH == 0:
                result += ' '
            index += 1
        return result

    # fills given bytes with zeros to make their length % BYTE_LENGTH = 0 without changing value
    def fill_with_zeros(binary, byte_length = None):
        if byte_length is None:
            byte_length = BinaryTools.BYTE_LENGTH
        if isinstance(binary, str):
            binary = binary.replace('0b', '').encode()
        else:
            binary = binary.decode().replace('0b', '').encode()
        if len(binary) > byte_length:
            raise BinaryToolsException('too big value')
        for i in range(0, byte_length - len(binary)):
            binary = b'0' + binary
        return binary

    def number_to_hex(number, endianess = Endianess.LITTLE, nbytes = 4):
        if nbytes < 1 or nbytes > 8:
            raise BinaryToolsException('number of bytes has to be between 1 and 8')
        result = b''
        if endianess not in [Endianess.LITTLE, Endianess.BIG]:
            raise BinaryToolsException('invalid endianess value passed')
        h_number = hex(number)[2:]
        if len(h_number) > nbytes * 2:
            raise BinaryToolsException('given number ' + str(number) + ' is bigger than bytes limit')
        h_number = BinaryTools.fill_with_zeros(h_number, nbytes*2)
        byte_arr = []
        for i in range(nbytes):
            value = h_number[i*2:i*2+2]
            value = BinaryTools.fill_with_zeros(value, 2)
            byte_arr.append(value)
        if endianess == Endianess.LITTLE:
            byte_arr = byte_arr[::-1]
        for byte in byte_arr:
            result += byte
        result = BinaryTools.fill_with_zeros(result, nbytes * 2)
        result = unhexlify(result)
        return result