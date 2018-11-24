'''
    @file       IntegrationTest.py
    @author     Karol Bisztyga (karolbisztyga@gmail.com)
    @date       2018/11/23
    @version    1.0

    @brief
        integration test which runs App.py with all the possible options
'''
import unittest, glob, os, sys
from studio_projektowe.compiler.src.Exceptions import IntegrationException
from studio_projektowe.compiler.src.App import App
from studio_projektowe.compiler.src.Compiler import Compiler


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
        with open(current_name, 'wb') as file:
            file.write(code.encode())
        return os.path.abspath(current_name)

    def read_sample(self, sample_path):
        if not os.path.isfile(sample_path):
            raise IntegrationException('unrecognized sample ' + str(sample_path))
        with open(sample_path, 'rb') as file:
            return file.read()

    def test_ui(self):
        app = App()
        insample = self.prepare_sample('[sec]qwerty1234567[sec]sub([reg] r0; [mem] dwd, 3; [reg] r0);[sec]')
        outsample = self.prepare_sample('')
        # data to be tested
        args_samples = [
            # nothing
            '',
            # too less args
            insample,
            insample + ' minify_code',
            insample + ' check_code',
            insample + ' compile',
            # valid number of args
            insample + ' minify_code ' + outsample,
            insample + ' compile ' + outsample,
            # too many args but it does not result in error
            insample + ' check_code ' + outsample,
            # too many args
            insample + ' minify_code a b',
            insample + ' check_code a b',
            insample + ' compile a b',
        ]
        # expected data
        expected_results = [
            False,
            False,
            False,
            True,
            False,
            True,
            True,
            True,
            False,
            False,
            False,
        ]
        # perform tests
        results = []
        for sample in args_samples:
            sample = 'studio_projektowe ' + sample
            sample = sample.split(' ')
            result = app.run(sample)
            results.append(result[0])
        # compare results
        self.assertEqual(len(results), len(args_samples))
        self.assertEqual(len(expected_results), len(results))
        for i in range(len(results)):
            self.assertEqual(results[i], expected_results[i])
        self.clear_tmp()

    def test_minify_code(self):
        app = App()
        # data to be tested
        code_samples = [
            'sub([reg] r0; [mem] dwd, 3; [reg] r0);',
            '''
                # load initial values;
                cpy([con]120; [reg]r0);
                cpy([con]11; [reg]r1);
                # multiply them;
                mul([reg]r1; [reg]r2; [reg] r3);
                # write out the output;
                out([reg] r3) ;
            ''',
        ]
        # expected data
        expected_results = [
            'sub([reg]r0;[mem]dwd,3;[reg]r0);',
            'cpy([con]120;[reg]r0);cpy([con]11;[reg]r1);mul([reg]r1;[reg]r2;[reg]r3);out([reg]r3);'
        ]
        # perform tests
        results = []
        for sample in code_samples:
            full_sample = '[sec][sec]' + sample + '[sec]'
            sample_file_in = self.prepare_sample(full_sample)
            sample_file_out = self.prepare_sample('')
            args = 'studio_projektowe ' +  sample_file_in + ' minify_code ' + sample_file_out
            run_result = app.run(args.split(' '))
            self.assertTrue(run_result)
            output_code = self.read_sample(sample_file_out).decode()
            output_code = output_code.split(Compiler.SECTION_DELIMITER)[2]
            results.append(output_code)
        # compare results
        self.assertEqual(len(results), len(code_samples))
        self.assertEqual(len(expected_results), len(results))
        for i in range(len(results)):
            self.assertEqual(results[i], expected_results[i])
        self.clear_tmp()

    def test_check_code(self):
        app = App()
        # data to be tested
        code_samples = [
            'sub([reg] r0; [mem] dwd, 3; [reg] r0);',
            '''
                # load initial values;
                cpy([con]120; [reg]r0);
                cpy([con]11; [reg]r1);
                # multiply them;
                mul([reg]r1; [reg]r2; [reg] r3);
                # write out the output;
                out([reg] r3) ;
            ''',
            'sub([reg] r; [mem] dwd, 3; [reg] r0);',
            'sub([reg] r5; [mem] dwd, 3 [reg] r0);',
            '''
                # load initial values
                cpy([con]120; [reg]r0);
            ''',
            '''
                # load initial values;
                cpy([con]120; [con]r0);
            ''',
            '''
                # load initial values;
                not([con]120; [reg]r0; [reg] r3);
            ''',
        ]
        # expected data
        expected_results = [
            True,
            True,
            False,
            False,
            False,
            False,
            False,
        ]
        # perform tests
        results = []
        for sample in code_samples:
            full_sample = '[sec][sec]' + sample + '[sec]'
            sample_file_in = self.prepare_sample(full_sample)
            args = 'studio_projektowe ' + sample_file_in + ' check_code'
            result = app.run(args.split(' '))[1]
            if result is None:
                result = False
            results.append(result)
        # compare results
        self.assertEqual(len(results), len(code_samples))
        self.assertEqual(len(expected_results), len(results))
        for i in range(len(results)):
            self.assertEqual(results[i], expected_results[i])
        self.clear_tmp()

    def test_compile(self):

        app = App()
        # data to be tested
        code_samples = [
            'sub([reg] r0; [mem] dwd, 3; [reg] r0);',
            '''
                # load initial values;
                cpy([con]120; [reg]r0);
                cpy([con]11; [reg]r1);
                # multiply them;
                mul([reg]r1; [reg]r2; [reg] r3);
                # write out the output;
                out([reg] r3) ;
            ''',
            'sub([reg] r; [mem] dwd, 3; [reg] r0);',
            'sub([reg] r5; [mem] dwd, 3 [reg] r0);',
            '''
                # load initial values
                cpy([con]120; [reg]r0);
            ''',
            '''
                # load initial values;
                cpy([con]120; [con]r0);
            ''',
            '''
                # load initial values;
                not([con]120; [reg]r0; [reg] r3);
            ''',
        ]
        # expected data
        expected_results = [
            b'K\x00B\x00V\x00M\x00\x00\x00\x00\x00\x00\x00\x00\x000\x00\x00\x00\x00\x00\x00\x00\x03\x00&\x00(\x00\x19\x00)\x00\x1c\x00$\x00(\x00\x1b\x00)\x00\x17\x00%\x00-\x00\x03\x00\x00\x00\x00\x00\x00\x00$\x00(\x00\x19\x00)\x00\x1c\x00\x27\x00$\x00',
            b'K\x00B\x00V\x00M\x00\x00\x00\x00\x00\x00\x00\x00\x00~\x00\x00\x00\x00\x00\x00\x00\x01\x00&\x00(\x00\x1a\x00)\x00+\x00,\x00*\x00x\x00\x00\x00\x00\x00\x00\x00$\x00(\x00\x19\x00)\x00\x1c\x00\x27\x00$\x00\x01\x00&\x00(\x00\x1a\x00)\x00+\x00+\x00\x00\x00\x00\x00\x00\x00\x00\x00$\x00(\x00\x19\x00)\x00\x1d\x00\x27\x00$\x00\x04\x00&\x00(\x00\x19\x00)\x00\x1d\x00$\x00(\x00\x19\x00)\x00\x1e\x00$\x00(\x00\x19\x00)\x00\x1f\x00\x27\x00$\x00\x10\x00&\x00(\x00\x19\x00)\x00\x1f\x00\x27\x00$\x00',
            b'',
            b'',
            b'',
            b'',
            b'',
        ]
        # perform tests
        results = []
        for sample in code_samples:
            full_sample = '[sec][sec]' + sample + '[sec]'
            sample_file_in = self.prepare_sample(full_sample)
            sample_file_out = self.prepare_sample('')
            args = 'studio_projektowe ' + sample_file_in + ' compile ' + sample_file_out
            run_result = app.run(args.split(' '))[0]
            result = b''
            if run_result:
                result = self.read_sample(sample_file_out)
            results.append(result)
        # compare results
        self.assertEqual(len(results), len(code_samples))
        self.assertEqual(len(expected_results), len(results))
        for i in range(len(results)):
            self.assertEqual(results[i], expected_results[i])
        self.clear_tmp()