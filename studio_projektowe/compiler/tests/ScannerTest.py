'''
    @file       ScannerTest.py
    @author     Karol Bisztyga (karolbisztyga@gmail.com)
    @date       2018/10/21
    @version    1.0

    @brief
        unit tests for Scanner
'''

from studio_projektowe.compiler.src.Scanner import Scanner
import unittest


class ScannerTest(unittest.TestCase):
    def test_scan(self):
        pass

    def test_clear_code(self):
        scanner = Scanner()
        # data to be tested
        test_data = [
            '''
                Maecenas augue magna,
                \tmollis ac magna sit amet,
                suscipit posuere neque.
                \t\tEtiam malesuada leo eu
                lorem pellentesque porttitor.
                \tVivamus diam urna,
                  condimentum   eu volutpat
                a, luctus ultrices
                justo.
            ''',
            '''
                Maecenas augue magna, #mollis 
                ac magna sit amet;, suscipit 
                posuere neque. #Etiam malesuada 
                leo eu lorem; pellentesque; porttitor
                . #Vivamus #diam ##urna, ###condimentum
                 #eu ;volutpat ;a, ;luctus #ultrices ;
                 justo.# Etiam ac massa
            ''',
        ]
        # expected data
        expected_data = [
            'Maecenasauguemagna,mollisacmagnasitamet,suscipitposuereneque.Etiammalesuadaleoeulorempellentesqueporttitor.Vivamusdiamurna,condimentumeuvolutpata,luctusultricesjusto.',
            'Maecenasauguemagna,,suscipitposuereneque.pellentesque;porttitor.volutpat;a,;luctusjusto.',
        ]
        # perform tests
        results = []
        for test in test_data:
            result = scanner.clear_code(test)
            results.append(result)
        # compare results
        self.assertEqual(len(results), len(test_data))
        self.assertEqual(len(expected_data), len(test_data))
        for i in range(0, len(results)):
            self.assertEqual(results[i], expected_data[i])
