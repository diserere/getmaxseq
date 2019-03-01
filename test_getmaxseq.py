#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_maxss.py
#  
#  Copyright 2019 Diserere <diserere@cooler>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

"""
Test suite for function returning longest substring containing not more
than N different symbols found in given string.
Assumed that:
- the tested function is placed in module module_name,
- it's called as 
fn_name(str string, int charset_len),
- it's returning value of type str
- if several substring of equal length is found, the last one 
is returned
- the sequence consisting of 0 symbols is null-length
"""

__version__ = '1.1.3'

import sys
import unittest
import time


module_name = 'max_seq'
fn_name = 'get_max_seq'

TIME_TRESHOLD = 0.01

related_test_version = '1.0.8'


class BaseTestClass(unittest.TestCase):

    """
    Base class for all tests with prepared conditions (tested fn is imported)
    """
    
    def setUp(self):
        self.m = __import__(module_name)
        self.fn = self.m.__getattribute__(fn_name)
        self.longMessage = True
        self._started_at = time.time()
        
    def tearDown(self):
        elapsed = time.time() - self._started_at
        if elapsed > TIME_TRESHOLD:
            print('{} ({}s)'.format(self.id(), round(elapsed, 3)))
            #~ print('Run time: ({}s)'.format(round(elapsed, 3)))
    

#~ @unittest.skip('Skipped test suite')    
class Test01Integration(unittest.TestCase):
    """ 
    Test that module and function are loadable 
    """

    def test_import_module(self):
        """ 
        Test if module is importable
        """
        try:
            self.m = __import__(module_name)
        except:
            self.fail('Cannot import %s: %s' % (module_name, str(sys.exc_info())))
        
    def test_import_fn(self):
        """ 
        Test if function in imported module is callable
        """
        try:
            self.m = __import__(module_name)
            self.fn = self.m.__getattribute__(fn_name)
        except:
            self.fail('Cannot import %s from %s: %s' % (fn_name, module_name, str(sys.exc_info())))


#~ @unittest.skip('Skipped test suite')
class Test02Positive(BaseTestClass):

    """
    Functional tests: test should return right value from different 
    types of incoming data
    """
    
    def test_ss_is_at_start(self):
        """
        Should find substring at start of string
        """
        self.assertEqual(self.fn('aabbc', 2), 'aabb')
    
    def test_ss_is_at_middle(self):
        """
        Should find substring at the middle of string
        """
        self.assertEqual(self.fn('abbcce', 2), 'bbcc')
    
    def test_ss_is_at_end(self):
        """
        Should find substring at the end of string
        """
        self.assertEqual(self.fn('abbcc', 2), 'bbcc')
    
    def test_max_ss_is_last(self):
        """
        Should return last max substring if more than one is found 
        """
        self.assertEqual(self.fn('abbccddeef', 3), 'ccddee')
    
    def test_ss_is_whole_string(self):
        """
        Test if found substring is whole string
        Should return whole string
        """
        self.assertEqual(self.fn('abbccdde', 5), 'abbccdde', 'Should return whole string')
        
    def test_seq_len_is_more_than_string_len(self):
        """
        Should return whole string when symbols number is more than string length
        """
        self.assertEqual(self.fn('abbccdde', 125), 'abbccdde')
        
    def test_register_matters(self):
        """
        Should distinct upper- and lower-case
        """
        self.assertEqual(self.fn('baaaAc', 1), 'aaa')
        
    def test_string_is_null(self):
        """
        Test if string is null
        Should return null string
        """
        self.assertEqual(self.fn('', 5), '')
        
    def test_ss_len_is_null(self):
        """ 
        Test if sequence length is null
        Should return null string
        """
        self.assertEqual(self.fn('abbccdde', 0), '')
        
    def test_all_chars(self):
        """ 
        Test all chars in string are acceptable for input and output
        """
        self.string = ''
        
        for c in range(0,256):
            self.string += chr(c)
            
        #~ self.assertEqual(self.fn(string, charset_len = 3), string[-3:])
        self.assertEqual(self.fn(self.string, 256), self.string)
        

#~ @unittest.skip('Skipped test suite')
class Test03Positive(BaseTestClass):

    """
    Functional tests: test that function could be called by
    different ways
    """
    
    def test_kw_arg(self):
        """ 
        Test if one param is keyword
        """
        self.assertEqual(self.fn('abbccdde', charset_len = 3), 'bbccdd')
        

    def test_kw_args(self):
        """ 
        Test if all params are keywords
        """
        self.assertEqual(self.fn(string = 'abbccdde', charset_len = 3), 'bbccdd')
        

#~ @unittest.skip('Skipped test suite')
class Test04Negative(BaseTestClass):

    """
    Test suite with negative cases: test behevior when incoming data is
    out of boundary conditions 
    """

    def test_param1_type(self):
        """
        Test if param1 is not string
        """
        with self.assertRaises(TypeError):
            self.fn(100, 2)
  
    def test_param2_type(self):
        """
        Test if param2 is not int
        """
        with self.assertRaises(TypeError):
            self.fn('aabbcc', '2')
  
    def test_param_missing_1(self):
        """
        Test if param missing - various param addressing type
        """
        with self.assertRaises(TypeError):
            self.fn('aabbcc')

    def test_param_missing_2(self):
        """
        Test if param missing - various param addressing type
        """
        with self.assertRaises(TypeError):
            self.fn(2)

    def test_param_missing_3(self):
        """
        Test if param missing - various param addressing type
        """
        with self.assertRaises(TypeError):
            self.fn(string = 'aabbcc')

    def test_param_missing_4(self):
        """
        Test if param missing - various param addressing type
        """
        with self.assertRaises(TypeError):
            self.fn(charset_len = 2)
        
    def test_param_exceeded(self):
        """
        Test if parameters exceeded
        """
        with self.assertRaises(TypeError):
            self.fn('aabbcc',2,3)
        
    #~ @unittest.expectedFailure
    def test_param2_negative(self):
        """
        Test if parameters 2 is negative
        """
        #~ with self.assertRaises(Exception):
        with self.assertRaises(TypeError):
            self.fn('aabbcc',-2)
        

#~ @unittest.skip('Skipped test suite')
class Test05Load(BaseTestClass):

    """
    Test suite for load tests
    """

    @unittest.skip("should not run until fixed: exceeded runtime (approx. 2.8s on tested version 1.0.7)")
    def test_load_01_256k(self):
        """
        Test if big (256Kb) string is in and out
        """
        self.string = ''.join( [ chr(c)*2**10 for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,256), self.string)
  
    @unittest.skip("should not run until fixed: exceeded runtime (approx. 12s on tested version 1.0.7)")
    def test_load_02_512k(self):
        """
        Test if big (512Kb) string is in and out
        """
        self.string = ''.join( [ chr(c)*2**11 for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,256), self.string)
  
    @unittest.skip("should not run until fixed: exceeded runtime (approx. 56s on tested version 1.0.7)")
    def test_load_03_1m(self):
        """
        Test if big (1Mb) string is in and out
        """
        self.string = ''.join( [ chr(c)*2**12 for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,256), self.string)
  
    #~ @unittest.skip("should not run until fixed: exceeded runtime (approx. 303s on tested version 1.0.7)")
    def test_load_04_2m(self):
        """
        Test if big (2Mb) string is in and out
        """
        self.string = ''.join( [ chr(c)*2**13 for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,256), self.string)
  
    #~ @unittest.skip("should not run until fixed: exceeded runtime (approx. 1.74s on tested version 1.0.8)")
    def test_load_05_4m(self):
        """
        Test if big (4Mb) string is in and out
        """
        self.string = ''.join( [ chr(c)*2**14 for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,256), self.string)
  
    #~ @unittest.skip("should not run until fixed: exceeded runtime (approx. 3.4s on tested version 1.0.8)")
    def test_load_06_8m(self):
        """
        Test if big (8Mb) string is in and out
        """
        self.string = ''.join( [ chr(c)*2**15 for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,256), self.string)
  
    @unittest.skip("should not run until fixed: exceeded runtime (approx. 6.8s on tested version 1.0.8)")
    def test_load_07_16m(self):
        """
        Test if big (16Mb) string is in and out
        """
        self.string = ''.join( [ chr(c)*2**16 for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,256), self.string)
  
    @unittest.skip("should not run until fixed: exceeded runtime (approx. 14.14s on tested version 1.0.8)")
    def test_load_08_32m(self):
        """
        Test if big (32Mb) string is in and out
        """
        self.string = ''.join( [ chr(c)*2**17 for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,256), self.string)
  
    @unittest.skip("should not run until fixed: exceeded runtime (approx. 28.46s on tested version 1.0.8)")
    def test_load_09_64m(self):
        """
        Test if big (64Mb) string is in and out
        """
        self.string = ''.join( [ chr(c)*2**18 for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,256), self.string)
  
    @unittest.skip("should not run until fixed: exceeded runtime (approx. 58.0s on tested version 1.0.8)")
    def test_load_10_128m(self):
        """
        Test if big (128Mb) string is in and out
        """
        self.string = ''.join( [ chr(c)*2**19 for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,256), self.string)
  

    @unittest.skip("should not run until fixed: exceeded runtime (approx. 124.77s on tested version 1.0.8)")
    def test_load_99_256m(self):
        """
        Test if big (256Mb) string is in and out
        """
        self.string = ''.join( [ chr(c)*2**20 for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,256), self.string)

multi = 2**12 # 1Mb
#~ multi = 2**11 # 512Kb
#~ multi = 2**10 # 256Kb
#~ multi = 2**9 # 128Kb


#~ @unittest.skip('Skipped test suite')
class Test06Perf(BaseTestClass):

    """
    Performance test suite 
    """

    @unittest.skip("should not run until fixed: exceeded runtime (approx. 0.22s on tested version 1.0.8)")
    def test_perf_01_00_s16m_n1_8(self):
        """
        Test if big (1Mb) string is in, seq len is 1 (near linear reading)
        """
        for self.n in range(1,9):
            self.string = ''.join( [ chr(c)*multi for c in range(256) ] )   
            self.assertEqual(self.fn(self.string,self.n), self.string[-multi*self.n:])
  
    #~ @unittest.skip("should not run until fixed: exceeded runtime (approx. 0.37s on tested version 1.0.8)")
    def test_perf_01_01_s16m_n1(self):
        """
        Test if big (1Mb) string is in, seq len is 1 (near linear reading)
        """
        self.n = 1
        self.string = ''.join( [ chr(c)*multi for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,self.n), self.string[-multi*self.n:])
  
    #~ @unittest.skip("should not run until fixed: exceeded runtime (approx. 0.97s on tested version 1.0.8)")
    def test_perf_01_01_s16m_n2(self):
        """
        Test if big (1Mb) string is in, seq len is 1 (near linear reading)
        """
        self.n = 2
        self.string = ''.join( [ chr(c)*multi for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,self.n), self.string[-multi*self.n:])
  
    #~ @unittest.skip("should not run until fixed: exceeded runtime (approx. 1.55s on tested version 1.0.8)")
    def test_perf_01_01_s16m_n3(self):
        """
        Test if big (1Mb) string is in, seq len is 1 (near linear reading)
        """
        self.n = 3
        self.string = ''.join( [ chr(c)*multi for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,self.n), self.string[-multi*self.n:])
  
    #~ @unittest.skip("should not run until fixed: exceeded runtime (approx. 2.04s on tested version 1.0.8)")
    def test_perf_01_01_s16m_n4(self):
        """
        Test if big (1Mb) string is in, seq len is 1 (near linear reading)
        """
        self.n = 4
        self.string = ''.join( [ chr(c)*multi for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,self.n), self.string[-multi*self.n:])
  
    #~ @unittest.skip("should not run until fixed: exceeded runtime (approx. 4.22s on tested version 1.0.8)")
    def test_perf_01_01_s16m_n8(self):
        """
        Test if big (1Mb) string is in, seq len is 1 (near linear reading)
        """
        self.n = 8
        self.string = ''.join( [ chr(c)*multi for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,self.n), self.string[-multi*self.n:])
  
    @unittest.skip("should not run until fixed: exceeded runtime (approx. 8.3s on tested version 1.0.8)")
    def test_perf_01_02_s16m_n16(self):
        """
        Test if big (1Mb) string is in, seq len is 1 (near linear reading)
        """
        self.n = 16
        self.string = ''.join( [ chr(c)*multi for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,self.n), self.string[-multi*self.n:])
  
    @unittest.skip("should not run until fixed: exceeded runtime (approx. 42.9s on tested version 1.0.8)")
    def test_perf_01_01_s16m_n128(self):
        """
        Test if big (1Mb) string is in, seq len is 1 (near linear reading)
        """
        self.n = 128
        self.string = ''.join( [ chr(c)*multi for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,self.n), self.string[-multi*self.n:])
  
    @unittest.skip("should not run until fixed: exceeded runtime (approx. 8.41s on tested version 1.0.8)")
    def test_perf_02_s16m_n32(self):
        """
        Test if big (1Mb) string is in, seq len is 32 (less seq length, more passes)
        """
        self.n = 32
        self.string = ''.join( [ chr(c)*multi for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,self.n), self.string[-multi*self.n:])
  
    @unittest.skip("should not run until fixed: exceeded runtime (approx. 14.4s on tested version 1.0.8)")
    def test_perf_03_s16m_n64(self):
        """
        Test if big (1Mb) string is in, seq len is 1 (near linear reading)
        """
        self.n = 64
        self.string = ''.join( [ chr(c)*multi for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,self.n), self.string[-multi*self.n:])
  
    @unittest.skip("should not run until fixed: exceeded runtime (approx. 18.8s on tested version 1.0.8)")
    def test_perf_04_s16m_n96(self):
        """
        Test if big (1Mb) string is in, seq len is 1 (near linear reading)
        """
        self.n = 96
        self.string = ''.join( [ chr(c)*multi for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,self.n), self.string[-multi*self.n:])
  
    @unittest.skip("should not run until fixed: exceeded runtime (approx. 20.9s on tested version 1.0.8)")
    def test_perf_05_s16m_n128(self):
        """
        Test if big (1Mb) string is in, seq len is 128 (half-string seq length, half passes)
        """
        self.n = 128
        self.string = ''.join( [ chr(c)*multi for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,self.n), self.string[-multi*self.n:])
  
    @unittest.skip("should not run until fixed: exceeded runtime (approx. 20.2s on tested version 1.0.8)")
    def test_perf_06_s16m_n160(self):
        """
        Test if big (1Mb) string is in, seq len is 160 (more seq length, less passes)
        """
        self.n = 160
        self.string = ''.join( [ chr(c)*multi for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,self.n), self.string[-multi*self.n:])
  
    @unittest.skip("should not run until fixed: exceeded runtime (approx. 16.77s on tested version 1.0.8)")
    def test_perf_07_s16m_n192(self):
        """
        Test if big (1Mb) string is in, seq len is 160 (more seq length, less passes)
        """
        self.n = 192
        self.string = ''.join( [ chr(c)*multi for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,self.n), self.string[-multi*self.n:])
  
    @unittest.skip("should not run until fixed: exceeded runtime (approx. 10.23s on tested version 1.0.8)")
    def test_perf_08_0_s16m_n224(self):
        """
        Test if big (1Mb) string is in, seq len is 224 (more seq length, less passes)
        """
        self.n = 224
        self.string = ''.join( [ chr(c)*multi for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,self.n), self.string[-multi*self.n:])
  
    @unittest.skip("should not run until fixed: exceeded runtime (approx. 5.7s on tested version 1.0.8)")
    def test_perf_08_1_s16m_n240(self):
        """
        Test if big (1Mb) string is in, seq len is 224 (more seq length, less passes)
        """
        self.n = 240
        self.string = ''.join( [ chr(c)*multi for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,self.n), self.string[-multi*self.n:])
  
    @unittest.skip("should not run until fixed: exceeded runtime (approx. 3.0s on tested version 1.0.8)")
    def test_perf_08_2_s16m_n248(self):
        """
        Test if big (1Mb) string is in, seq len is 224 (more seq length, less passes)
        """
        self.n = 248
        self.string = ''.join( [ chr(c)*multi for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,self.n), self.string[-multi*self.n:])
  
    @unittest.skip("should not run until fixed: exceeded runtime (approx. 1.69s on tested version 1.0.8)")
    def test_perf_08_3_s16m_n252(self):
        """
        Test if big (1Mb) string is in, seq len is 224 (more seq length, less passes)
        """
        self.n = 252
        self.string = ''.join( [ chr(c)*multi for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,self.n), self.string[-multi*self.n:])
  
    @unittest.skip("should not run until fixed: exceeded runtime (approx. 0.24s on tested version 1.0.8)")
    def test_perf_09_s16m_n256(self):
        """
        Test if big (1Mb) string is in, seq len is 256 (more seq length, less passes)
        """
        self.n = 256
        self.string = ''.join( [ chr(c)*multi for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,self.n), self.string[-multi*self.n:])
  

def main(args):
    #~ unittest.main(verbosity=2)
    unittest.main(verbosity=0)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
