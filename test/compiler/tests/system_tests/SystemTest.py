'''
    @file       SystemTest.py
    @author     Karol Bisztyga (karolbisztyga@gmail.com)
    @date       2019/01/10
    @version    1.0

    @brief
        system test which runs App.py with all the possible options
'''
import unittest
import glob
import os
import subprocess


class IntegrationException(Exception):
    pass


class SystemTest(unittest.TestCase):
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
        super(SystemTest, self).__init__(*args, **kwargs)
        # check for tmp folder existence and access
        if not os.path.isdir(SystemTest.TMP_PATH):
            os.mkdir(SystemTest.TMP_PATH)
        self.clear_tmp()

    # --------------------------------------------------------------------
    #           HELPER FUNCTIONS
    # --------------------------------------------------------------------

    # clear the tmp folder considering file naming convention
    def clear_tmp(self):
        files = glob.glob(SystemTest.TMP_PATH + '\\*')
        for file in files:
            if SystemTest.FILE_PREFIX in file:
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
            current_name = SystemTest.TMP_PATH + '\\' + SystemTest.FILE_PREFIX + n_str + '.bin'
            if not os.path.isfile(current_name):
                valid_name = True
            n += 1
        with open(current_name, 'wb') as file:
            file.write(code.encode())
        return os.path.abspath(current_name)

    def read_sample(self, sample_name):
        if SystemTest.TMP_PATH not in sample_name:
            sample_name = SystemTest.TMP_PATH + '\\' + sample_name
        if not os.path.isfile(sample_name):
            raise IntegrationException('unrecognized sample ' + str(sample_name))
        with open(sample_name, 'rb') as file:
            return file.read()

    def chech_sample_existence(self, sample_name):
        try:
            self.read_sample(sample_name)
            return True
        except:
            return False
        return False

    # --------------------------------------------------------------------
    #           TESTS
    # --------------------------------------------------------------------

    def test_user_interface(self):
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
            1,
            1,
            1,
            0,
            1,
            0,
            0,
            0,
            1,
            1,
            1,
        ]
        # perform tests
        results = []
        for sample in args_samples:
            result = os.system(SystemTest.PYTHON_PATH + ' ' + SystemTest.APP_PATH + ' ' + sample)
            results.append(result)
        # compare results
        self.assertEqual(len(results), len(args_samples))
        self.assertEqual(len(expected_results), len(results))
        for i in range(len(results)):
            self.assertEqual(results[i], expected_results[i])
        self.clear_tmp()

    def test_minify_code(self):
        # data to be tested
        code_samples = [
            # empty
            '',
            # single line without comments
            'sub([reg] r0; [mem] dwd, 3; [reg] r0);',
            # single line with comments
            'sub([reg] r0; [mem] dwd, 3; [reg] r0);     # write out the output;    out([reg] r3) ;    ',
            # multi line with comments
            '''
                # load initial values;
                cpy([con]120; [reg]r0);
                cpy([con]11; [reg]r1);
                # multiply them;
                mul([reg]r1; [reg]r2; [reg] r3);
                # write out the output;
                out([reg] r3) ;
            ''',
            # multi line with no comments
            '''
                cpy([con]120; [reg]r0);
                cpy([con]11; [reg]r1);
                mul([reg]r1; [reg]r2; [reg] r3);
                out([reg] r3) ;
            ''',
        ]
        # expected data
        expected_results = [
            0,
            0,
            0,
            0,
            0,
        ]
        # perform tests
        results = []
        for sample in code_samples:
            full_sample = '[sec][sec]' + sample + '[sec]'
            sample_file_in = self.prepare_sample(full_sample)
            sample_file_out = self.prepare_sample('')
            result = os.system(SystemTest.PYTHON_PATH + ' ' + SystemTest.APP_PATH + ' ' + sample_file_in + ' minify_code ' + sample_file_out)
            # output_code = self.read_sample(sample_file_out).decode()
            # output_code = output_code.split(SystemTest.SECTION_DELIMITER)[2]
            results.append(result)
        # compare results
        self.assertEqual(len(results), len(code_samples))
        self.assertEqual(len(expected_results), len(results))
        for i in range(len(results)):
            self.assertEqual(results[i], expected_results[i])
        self.clear_tmp()

    def test_check_code(self):
        # data to be tested
        code_samples = [
            # empty
            '',
            # correct single line
            'sub([reg] r0; [mem] dwd, 3; [reg] r0);',
            # correct multi line
            '''
                # load initial values;
                cpy([con]120; [reg]r0);
                cpy([con]11; [reg]r1);
                # multiply them;
                mul([reg]r1; [reg]r2; [reg] r3);
                # write out the output;
                out([reg] r3) ;
            ''',
            # incorrect one line - missing reg number like r0, r1 etc.
            'sub([reg] r; [mem] dwd, 3; [reg] r0);',
            # incorrect one line - missing ; after mem arg
            'sub([reg] r5; [mem] dwd, 3 [reg] r0);',
            # incorrect multi line - invalid number
            '''
                # load initial values - invalid number
                cpy([con]1a20; [reg]r0);
            ''',
            # incorrect multi line - passing reg 0 as const
            '''
                # load initial values;
                cpy([con]120; [con]r0);
            ''',
            # incorrect multi line - 2 args expected, 3 passed
            '''
                # load initial values;
                not([con]120; [reg]r0; [reg] r3);
            ''',
        ]
        # expected data
        expected_results = [
            0,
            0,
            0,
            1,
            1,
            1,
            1,
            1,
        ]
        # perform tests
        results = []
        for sample in code_samples:
            full_sample = '[sec][sec]' + sample + '[sec]'
            sample_file_in = self.prepare_sample(full_sample)
            result = os.system(SystemTest.PYTHON_PATH + ' ' + SystemTest.APP_PATH + ' ' + sample_file_in + ' check_code')
            results.append(result)
        # compare results
        self.assertEqual(len(results), len(code_samples))
        self.assertEqual(len(expected_results), len(results))
        for i in range(len(results)):
            self.assertEqual(results[i], expected_results[i])
        self.clear_tmp()

    def test_compile(self):
        # data to be tested
        code_samples = [
            # empty
            '',
            # correct signle line
            'sub([reg] r0; [mem] dwd, 3; [reg] r0);',
            # correct multi line
            '''
                # load initial values;
                cpy([con]120; [reg]r0);
                cpy([con]11; [reg]r1);
                # multiply them;
                mul([reg]r1; [reg]r2; [reg] r3);
                # write out the output;
                out([reg] r3) ;
            ''',
            # incorrect one line - missing reg number like r0, r1 etc.
            'sub([reg] r; [mem] dwd, 3; [reg] r0);',
            # incorrect one line - missing ;
            'sub([reg] r5; [mem] dwd, 3 [reg] r0);',
            # incorrect multi line - invalid number
            '''
                # load initial values
                cpy([con]12a0; [reg]r0);
            ''',
            # incorrect multi line - invalid arg 2
            '''
                # load initial values;
                cpy([con]120; [con]r0);
            ''',
            # incorrect multi line - wrong number of args
            '''
                # load initial values;
                not([con]120; [reg]r0; [reg] r3);
            ''',
        ]
        # expected data
        expected_results = [
            0,
            0,
            0,
            1,
            1,
            1,
            1,
            1,
        ]
        # perform tests
        results = []
        for sample in code_samples:
            full_sample = '[sec][sec]' + sample + '[sec]'
            sample_file_in = self.prepare_sample(full_sample)
            sample_file_out = self.prepare_sample('')
            result = os.system(SystemTest.PYTHON_PATH + ' ' + SystemTest.APP_PATH + ' ' + sample_file_in + ' compile ' + sample_file_out)
            results.append(result)
        # compare results
        self.assertEqual(len(results), len(code_samples))
        self.assertEqual(len(expected_results), len(results))
        for i in range(len(results)):
            self.assertEqual(results[i], expected_results[i])
        self.clear_tmp()

    def test_std_out(self):
        # data to be tested
        code_samples = [
            # user interface invalid args
            ('ui', 'a minify_code b a'),
            # minify code
            ('minify', 'sub([reg] r0; [mem] dwd, 3; [reg] r0);'),
            # check code - valid
            ('check', 'sub([reg] r0; [mem] dwd, 3; [reg] r0);'),
            # check code - invalid
            ('check', 'sub([reg] r5; [mem] dwd, 3 [reg] r0);'),
            # compile - valid sample 1
            ('compile', 'sub([reg] r0; [mem] dwd, 3; [reg] r0);'),
            # compile - valid sample 2
            ('compile', '''
                # load initial values;
                cpy([con]120; [reg]r0);
                cpy([con]11; [reg]r1);
                # multiply them;
                mul([reg]r1; [reg]r2; [reg] r3);
                # write out the output;
                out([reg] r3) ;
            '''),
            # compile - syntax error
            ('compile', '''
                # load initial values
                cpy([con]12a0; [reg]r0);
            '''),
        ]
        # expected data
        expected_results = [
            ['an error occured', 'HELP', 'invalid arguments'],
            ['minification successful, output file: '],
            ['1 the code is valid', ],
            ['0 the code is not valid', ],
            ['compilation successful, output file: ', ],
            ['compilation successful, output file: ', ],
            ['an error occured'],
        ]
        # perform tests
        results = []
        for tested_feature, sample in code_samples:
            full_sample = '[sec][sec]' + sample + '[sec]'
            sample_file_in = self.prepare_sample(full_sample)
            sample_file_out = self.prepare_sample('')
            cmd = SystemTest.PYTHON_PATH + ' ' + SystemTest.APP_PATH + ' '# + sample_file_in + ' compile ' + sample_file_out
            if tested_feature == 'ui':
                cmd += sample
            elif tested_feature == 'minify':
                cmd += sample_file_in + ' minify_code ' + sample_file_out
            elif tested_feature == 'check':
                cmd += sample_file_in + ' check_code'
            elif tested_feature == 'compile':
                cmd += sample_file_in + ' compile ' + sample_file_out
            else:
                # invalid tested_feature value
                self.assertTrue(False)
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            result = result.stdout
            results.append(result)
        # compare results
        self.assertEqual(len(results), len(code_samples))
        self.assertEqual(len(expected_results), len(results))
        for i in range(len(results)):
            for expected_res in expected_results[i]:
                self.assertTrue(expected_res in results[i])
        self.clear_tmp()

    def test_files_creation(self):
        # data to be tested
        code_samples = [
            # minify code
            ('minify', '''sub(
                                [reg] r0; 
                                [mem] dwd, 3; 
                                [reg] r0);'''),
            # compile - valid sample 1
            ('compile', 'sub([reg] r0; [mem] dwd, 3; [reg] r0);'),
            # compile - valid sample 2
            ('compile', '''
                        # load initial values;
                        cpy([con]120; [reg]r0);
                        cpy([con]11; [reg]r1);
                        # multiply them;
                        mul([reg]r1; [reg]r2; [reg] r3);
                        # write out the output;
                        out([reg] r3) ;
                    '''),
            # compile - syntax error
            ('compile', '''
                        # load initial values
                        cpy([con]12a0; [reg]r0);
                    '''),
        ]
        # expected data
        expected_results = [
            b'[sec][sec]sub([reg]r0;[mem]dwd,3;[reg]r0);[sec]',
            b'K\x00B\x00V\x00M\x00\x00\x00\x00\x00\x00\x00\x00\x000\x00\x00\x00\x00\x00\x00\x00\x03\x00&\x00(\x00\x19\x00)\x00\x1c\x00$\x00(\x00\x1b\x00)\x00\x17\x00%\x00-\x00\x03\x00\x00\x00\x00\x00\x00\x00$\x00(\x00\x19\x00)\x00\x1c\x00\x27\x00$\x00',
            b'K\x00B\x00V\x00M\x00\x00\x00\x00\x00\x00\x00\x00\x00~\x00\x00\x00\x00\x00\x00\x00\x01\x00&\x00(\x00\x1a\x00)\x00+\x00,\x00*\x00x\x00\x00\x00\x00\x00\x00\x00$\x00(\x00\x19\x00)\x00\x1c\x00\x27\x00$\x00\x01\x00&\x00(\x00\x1a\x00)\x00+\x00+\x00\x00\x00\x00\x00\x00\x00\x00\x00$\x00(\x00\x19\x00)\x00\x1d\x00\x27\x00$\x00\x04\x00&\x00(\x00\x19\x00)\x00\x1d\x00$\x00(\x00\x19\x00)\x00\x1e\x00$\x00(\x00\x19\x00)\x00\x1f\x00\x27\x00$\x00\x10\x00&\x00(\x00\x19\x00)\x00\x1f\x00\x27\x00$\x00',
            b'',
        ]
        # perform tests
        results = []
        for tested_feature, sample in code_samples:
            full_sample = '[sec][sec]' + sample + '[sec]'
            sample_file_in = self.prepare_sample(full_sample)
            sample_file_out = self.prepare_sample('')
            cmd = SystemTest.PYTHON_PATH + ' ' + SystemTest.APP_PATH + ' '  # + sample_file_in + ' compile ' + sample_file_out
            if tested_feature == 'minify':
                cmd += sample_file_in + ' minify_code ' + sample_file_out
            elif tested_feature == 'compile':
                cmd += sample_file_in + ' compile ' + sample_file_out
            else:
                # invalid tested_feature value
                self.assertTrue(False)
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            result = result.stdout
            results.append(sample_file_out)
        # compare results
        self.assertEqual(len(results), len(code_samples))
        self.assertEqual(len(expected_results), len(results))
        for i in range(len(results)):
            expected = self.read_sample(results[i])
            self.assertEqual(expected, expected_results[i])
        self.clear_tmp()
