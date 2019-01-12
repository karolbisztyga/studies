'''
    @file       DataHandler.py
    @author     Karol Bisztyga (karolbisztyga@gmail.com)
    @date       2018/11/04
    @version    1.0

    @input - ASCII signs
    @output - binary codes for given signs
    @brief
        handles data section during compilation, responsible for input validation and conversion into binary code
'''


class DataHandler:

    def validate_data(self, input_data):
        try:
            input_data.encode('ascii')
        except UnicodeDecodeError:
            return False
        return True

    def generate_binary(self, input_data):
        return input_data.encode()
