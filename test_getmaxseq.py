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

__version__ = '1.1.2'

import sys
import unittest


related_test_version = '1.0.7'
#~ global related_test_version
#~ related_test_version = ''
module_name = 'max_seq'
fn_name = 'get_max_seq'

class BaseTestClass(unittest.TestCase):

    """
    Base class for all tests with prepared conditions (tested fn is imported)
    """
    
    def setUp(self):
        self.m = __import__(module_name)
        self.fn = self.m.__getattribute__(fn_name)
        self.longMessage = True
    
    
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
            related_test_version = self.m.__version__
            self.fn = self.m.__getattribute__(fn_name)
        except:
            self.fail('Cannot import %s from %s: %s' % (fn_name, module_name, str(sys.exc_info())))


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
        
    @unittest.skipIf(related_test_version <= '1.0.7', 'Not fixed until version 1.0.7: current %s' % related_test_version)
    def test_param_exceeded(self):
        """
        Test if parameters exceeded
        """
        with self.assertRaises(TypeError):
            self.fn('aabbcc',2,3)
        
    @unittest.expectedFailure
    def test_param2_negative(self):
        """
        Test if parameters 2 is negative
        """
        with self.assertRaises(Exception):
        #~ with self.assertRaises(TypeError):
            self.fn('aabbcc',-2)
        

#~ @unittest.skip('Skipped test suite')
class Test05Load(BaseTestClass):

    """
    Test suite for load tests
    """

    #~ @unittest.skip("should not run until fixed: exceeded runtime (approx. 2.8s)")
    def test_load_01_256k(self):
        """
        Test if big (256Kb) string is in and out
        """
        self.string = ''.join( [ chr(c)*2**10 for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,256), self.string)
  
    @unittest.skip("should not run until fixed: exceeded runtime (approx. 12s)")
    def test_load_02_512k(self):
        """
        Test if big (512Kb) string is in and out
        """
        self.string = ''.join( [ chr(c)*2**11 for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,256), self.string)
  
    @unittest.skip("should not run until fixed: exceeded runtime (approx. 56s)")
    def test_load_03_1m(self):
        """
        Test if big (1Mb) string is in and out
        """
        self.string = ''.join( [ chr(c)*2**12 for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,256), self.string)
  
    @unittest.skip("should not run until fixed: exceeded runtime (approx. 303s)")
    def test_load_04_2m(self):
        """
        Test if big (2Mb) string is in and out
        """
        self.string = ''.join( [ chr(c)*2**13 for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,256), self.string)
  
    @unittest.skip("should not run until fixed: exceeded runtime")
    def test_load_05_4m(self):
        """
        Test if big (4Mb) string is in and out
        """
        self.string = ''.join( [ chr(c)*2**14 for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,256), self.string)
  
    @unittest.skip("should not run until fixed: exceeded runtime")
    def test_load_06_8m(self):
        """
        Test if big (8Mb) string is in and out
        """
        self.string = ''.join( [ chr(c)*2**15 for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,256), self.string)
  
    @unittest.skip("should not run until fixed: exceeded runtime")
    def test_load_07_16m(self):
        """
        Test if big (16Mb) string is in and out
        """
        self.string = ''.join( [ chr(c)*2**16 for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,256), self.string)
  
    @unittest.skip("should not run until fixed: exceeded runtime")
    def test_load_08_32m(self):
        """
        Test if big (32Mb) string is in and out
        """
        self.string = ''.join( [ chr(c)*2**17 for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,256), self.string)
  
    @unittest.skip("should not run until fixed: exceeded runtime")
    def test_load_09_64m(self):
        """
        Test if big (64Mb) string is in and out
        """
        self.string = ''.join( [ chr(c)*2**18 for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,256), self.string)
  
    @unittest.skip("should not run until fixed: exceeded runtime")
    def test_load_10_128m(self):
        """
        Test if big (128Mb) string is in and out
        """
        self.string = ''.join( [ chr(c)*2**19 for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,256), self.string)
  

    @unittest.skip("should not run until fixed: exceeded runtime")
    def test_load_99_256m(self):
        """
        Test if big (256Mb) string is in and out
        """
        self.string = ''.join( [ chr(c)*2**20 for c in range(256) ] )   
        self.assertEqual(self.fn(self.string,256), self.string)
  

def main(args):
    unittest.main(verbosity=2)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
