#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  max_seq.py
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
Returns max substring containing not more than N different symbols
"""

__version__ = '1.1.3'


def is_matching(char, n, charmap, charmap_len):
    """
    TODO: DOCSTRING
    args:
        char: str
        1-length str to operate
        n: int
        current pos in str to save as last occurence
        charmap: dict
        dict with char as key and n as value, 
         like {char: n[, char: n]...}
        charmap_len: int
    """
    # try to match with stack
    if char in charmap or len(charmap) < charmap_len:
        charmap[char] = n
        match = True
    else: # nor found neither added: not match
        match = False

    return match


def save_max_substr(cur_substr, max_substr):
    if len(cur_substr) >= len(max_substr): # Use ">" here to save first max substr of the same length instead of last one
        max_substr = cur_substr
    return max_substr


def get_max_seq(string, charset_len):
    """ 
    Return longest substring consisting of not more than given number of
    different chars found in input string. If more than one string of
    equal length is found then the last one is returned.
    Args:
        str string: input string
        int charset_len: max number of different chars in sequence
    """
    
    # charset_len should be int and positive
    if type(charset_len) is not int:
        raise TypeError('arg charset_len: should be int but unexpected type: %s' % type(charset_len) )
    elif charset_len < 0:
        raise TypeError('arg charset_len: should not be negative but is: %s' % str(charset_len) )
    
    # Null charset_len cause exception while pop from null list, see below
    if len(string) == 0 or charset_len == 0:
        return ""
    
    # start from beginning of string
    p = 0
    max_substr = ''
    cur_substr = ''
    charset = dict()
    
    while p <= len(string)-1:
        cur_char = string[p]
        if not is_matching(cur_char, p, charset, charset_len): # end of sequence is found
            # compare and save result 
            max_substr = save_max_substr(cur_substr, max_substr) 
            # exclude first element from charmap, 
            #  get abs new start address (+1) from its address
            min_key = min(charset, key=charset.get)
            new_start_addr = charset[min_key] - p + len(cur_substr) + 1
            charset.pop(min_key)
            # add new char to charmap
            charset[cur_char] = p
            # trunk current ss for new sequence
            cur_substr = cur_substr[new_start_addr:]
            
        # add last char to ss, fwd ptr
        cur_substr += cur_char
        p += 1
    # here the ptr is at the end of string, compare results again
    max_substr = save_max_substr(cur_substr, max_substr) 

    return max_substr
    

def main(args):

    import argparse
    
    d_MAX_SEQ_LEN = 2
    
    parser = argparse.ArgumentParser(
        description='Python script for print max substring from given string containing not more than '+ str(d_MAX_SEQ_LEN) + ' symbols',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('str', type=str, metavar='STRING', default="", help='String to find a sequence')
    parser.add_argument('-n', '--num', type=int, metavar='NUM', default=d_MAX_SEQ_LEN, help='Max. number of different symbols in substring')

    aargs = parser.parse_args()
    string = aargs.str
    max_charset = aargs.num

    max_substr = get_max_seq(string, max_charset)
    
    print ("Last substring of max length of " + str(len(max_substr)) + " is:")
    print ("[" + max_substr + "]")


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
