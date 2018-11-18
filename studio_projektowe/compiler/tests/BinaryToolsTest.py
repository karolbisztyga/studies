'''
    @file       BinaryToolsTest.py
    @author     Karol Bisztyga (karolbisztyga@gmail.com)
    @date       2018/11/18
    @version    1.0

    @brief
        unit tests for Binary Tools
'''

from studio_projektowe.compiler.src.BinaryTools import BinaryTools, Endianess
from studio_projektowe.compiler.src.Exceptions import BinaryToolsException
import unittest

class BinaryToolsTest(unittest.TestCase):

    def test_fill_with_zeros(self):
        # data to be tested
        samples = [
            ('1', None),
            ('100', None),
            ('00', None),
            ('0110100110', 16), # len 10
            ('10101101010101001010', 24), # len 20
            ('', None),
            ('', 2),
            ('1', 2),
            ('11', 2),
        ]
        # expected data
        expected_results = [
            b'00000001',
            b'00000100',
            b'00000000',
            b'0000000110100110',
            b'000010101101010101001010',
            b'00000000',
            b'00',
            b'01',
            b'11',
        ]
        # perform tests
        results = []
        for sample in samples:
            results.append(BinaryTools.fill_with_zeros(sample[0], sample[1]))
        self.assertRaises(BinaryToolsException, BinaryTools.fill_with_zeros, '0110110', 4)
        # compare results
        self.assertEqual(len(results), len(samples))
        self.assertEqual(len(expected_results), len(results))
        for i in range(len(results)):
            self.assertEqual(results[i], expected_results[i])

    def test_number_to_hex(self):
        # data to be tested
        samples = [
            (0, Endianess.LITTLE, 4),
            (1, Endianess.LITTLE, 4),
            (1, Endianess.BIG, 4),
            (4294967295, Endianess.BIG, 4),
            (2359445, Endianess.BIG, 4),
            (2359445, Endianess.LITTLE, 4),
            (113539, Endianess.BIG, 4),
            (113539, Endianess.LITTLE, 4),
            (3498562852345435, Endianess.BIG, 8)
        ]
        # expected data
        expected_results = [
            b'\x00\x00\x00\x00',
            b'\x01\x00\x00\x00',
            b'\x00\x00\x00\x01',
            b'\xff\xff\xff\xff',
            b'\x00\x24\x00\x95',
            b'\x95\x00\x24\x00',
            b'\x00\x01\xbb\x83',
            b'\x83\xbb\x01\x00',
            b'\x00\x0c\x6d\xec\xa4\x09\xd6\x5b',
        ]
        # perform tests
        results = []
        for sample in samples:
            results.append(BinaryTools.number_to_hex(sample[0], sample[1], sample[2]))
        self.assertRaises(BinaryToolsException, BinaryTools.number_to_hex, 352, None)
        self.assertRaises(BinaryToolsException, BinaryTools.number_to_hex, 5678242893, Endianess.LITTLE)
        self.assertRaises(BinaryToolsException, BinaryTools.number_to_hex, 61345867829464766555, Endianess.LITTLE)
        # compare results
        self.assertEqual(len(results), len(samples))
        self.assertEqual(len(expected_results), len(results))
        for i in range(len(results)):
            self.assertEqual(results[i], expected_results[i])