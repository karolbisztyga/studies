import os, sys

'''
    @file       IntegrationTest.py
    @author     Karol Bisztyga (karolbisztyga@gmail.com)
    @date       2018/11/23
    @version    1.0

    @brief
        integration test which runs App.py with all the possible options
'''
import unittest, glob
from studio_projektowe.compiler.src.Exceptions import IntegrationException
from studio_projektowe.compiler.src.App import App


class IntegrationTest(unittest.TestCase):

    # tmp path which will be used to store files and check for their validity
    # all the tested files should be removed after each test
    TMP_PATH = 'D:\\pytmp'
    # used for file naming
    FILE_PREFIX = 'kbvm_test_'

    def __init__(self, *args, **kwargs):
        super(IntegrationTest, self).__init__(*args, **kwargs)
        # check for tmp folder existence and access
        if not os.path.isdir(IntegrationTest.TMP_PATH):
            os.mkdir(IntegrationTest.TMP_PATH)
        self.clear_tmp()

    # clear the tmp folder considering file naming convention
    def clear_tmp(self):
        files = glob.glob(IntegrationTest.TMP_PATH + '\\*')
        for file in files:
            if IntegrationTest.FILE_PREFIX in file:
                os.remove(file)

    def prepare_sample(self, code):
        valid_name = False
        n = 0
        current_name = ''
        while not valid_name:
            #compose string from number
            n_str = str(n)
            for i in range(len(n_str), 3):
                n_str = '0' + n_str
            current_name = IntegrationTest.TMP_PATH + '\\' + IntegrationTest.FILE_PREFIX + n_str + '.bin'
            if not os.path.isfile(current_name):
                valid_name = True
            n += 1
        with open(current_name, 'w') as file:
            file.write(code)
        return os.path.abspath(current_name)

    def test_ui(self):
        app = App()
        insample = self.prepare_sample('[sec]qwerty1234567[sec]sub([reg] r0; [mem] dwd, 3; [reg] r0);[sec]')
        outsample = self.prepare_sample('')
        # data to be tested
        args_samples = [
            #'',
            #insample,
            #insample + ' minify_code',
            #insample + ' check_code',
            #insample + ' compile',
            #insample + ' minify_code ' + outsample,
            insample + ' compile ' + outsample,
        ]
        # expected data
        expected_results = [
            #False,
            #False,
            #False,
            #True,
            #False,
            #True,
            True,
        ]
        # perform tests
        results = []
        for sample in args_samples:
            sample = 'studio_projektowe ' + sample
            sample = sample.split(' ')
            result = app.run(sample)
            results.append(result)
        # compare results
        self.assertEqual(len(results), len(args_samples))
        self.assertEqual(len(expected_results), len(results))
        for i in range(len(results)):
            self.assertEqual(results[i], expected_results[i])


        result = app.run('')
        print('--------' + str(result))
        self.clear_tmp()

    def test_minify_code(self):
        # TODO
        self.clear_tmp()

    def test_check_code(self):
        # TODO
        self.clear_tmp()

    def test_compile(self):
        # TODO
        self.clear_tmp()