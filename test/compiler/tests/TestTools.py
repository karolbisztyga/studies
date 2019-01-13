'''
    @file       TestTools.py
    @author     Karol Bisztyga (karolbisztyga@gmail.com)
    @date       2019/01/10
    @version    1.0

    @brief
        toolset for tests which helps in file handling process
'''
import os
import glob


class TestException(Exception):
    pass


class TestsTools:
    SECTION_DELIMITER = '[sec]'

    # tmp path which will be used to store files and check for their validity
    # all the tested files should be removed after each test
    TMP_PATH = 'D:\\pytmp'
    # python interpreter path
    PYTHON_PATH = 'D:\\Programs\\Python3\\python.exe'
    # path to the App to be tested
    APP_PATH = 'D:\\Workspace\\studies\\test\\compiler'
    # used for file naming
    FILE_PREFIX = 'kbvm_test_'

    def __init__(self, *args, **kwargs):
        # check for tmp folder existence and access
        if not os.path.isdir(TestsTools.TMP_PATH):
            os.mkdir(TestsTools.TMP_PATH)
        self.clear_tmp()

    # clear the tmp folder considering file naming convention
    def clear_tmp(self):
        files = glob.glob(TestsTools.TMP_PATH + '\\*')
        for file in files:
            if TestsTools.FILE_PREFIX in file:
                os.remove(file)

    def prepare_sample(self, code):
        valid_name = False
        n = 0
        current_name = ''
        while not valid_name:
            # compose string from number
            n_str = str(n)
            for i in range(len(n_str), 3):
                n_str = '0' + n_str
            current_name = TestsTools.TMP_PATH + '\\' + TestsTools.FILE_PREFIX + n_str + '.bin'
            if not os.path.isfile(current_name):
                valid_name = True
            n += 1
        with open(current_name, 'wb') as file:
            file.write(code.encode())
        return os.path.abspath(current_name)

    def read_sample(self, sample_name):
        if TestsTools.TMP_PATH not in sample_name:
            sample_name = TestsTools.TMP_PATH + '\\' + sample_name
        if not os.path.isfile(sample_name):
            raise TestException('unrecognized sample ' + str(sample_name))
        with open(sample_name, 'rb') as file:
            return file.read()

    def chech_sample_existence(self, sample_name):
        try:
            self.read_sample(sample_name)
            return True
        except:
            return False
        return False
