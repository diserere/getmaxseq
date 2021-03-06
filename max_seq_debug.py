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
DOCSTRING
"""

__version__ = '1.0.5'

#~ import argparse

def is_in_seq(charset, char, charset_len):
    if char in charset:
        print("seq: found")
        found = True
    elif len(charset) < charset_len:
        charset += char
        print("seq: added")
        found = True
    else:
        print("seq: not found")
        found = False
    return charset, found
    
def save_max_substr(cur_substr, max_substr):
    if len(cur_substr) >= len(max_substr): # Use ">" here to save first max substr of the same length instead of last one
        print("-- Replace max [" + max_substr + "] to new [" + cur_substr + "]")
        max_substr = cur_substr
    return max_substr

def get_max_seq(string, charset_len):
    
    import time
    
    """ 
    Function to find max substring containing not more than 'charset_len' 
    symbols in 'string' string. 
    Returns last found substring of max length
    """

    # if string is zero-length
    if not len(string):
        return ""
    
    # start from beginning of string
    p = 0
    max_substr = ""
    cur_substr = ""
    charset = ""
    
    while p <= len(string)-1 :
        
        time.sleep(0.1)
        print("...sleep ...")

        while True:
            print("  ...")
            print("Curr p is: " + str(p))
            cur_char = string[p]
            print("Curr char is: " + cur_char)
            print("Curr seq is: " + charset)
            print("Curr substr is: " + cur_substr)
            print("Max substr is: " + max_substr)

            charset, found = is_in_seq(charset, cur_char, charset_len)

            if found:
                cur_substr += cur_char
                print("Extend substr: " + cur_substr)
                p += 1
                break

            else:
                max_substr = save_max_substr(cur_substr, max_substr)

                # flush charset 
                charset = ""
                # flush current substr
                cur_substr = ""
                # rewind ptr to start of new sequence
                while True:
                    cur_char = string[p]
                    print("Rewind: p is: %s; char is: %s; charset is: %s" % (str(p), cur_char, charset))
                    charset, found = is_in_seq(charset, cur_char, charset_len)
                    if not found:
                        # shift ptr fwd, clear registers, exit
                        p += 1 
                        charset = ""
                        break
                    else:
                        p -= 1
                        
                break
                
        max_substr = save_max_substr(cur_substr, max_substr)

    print ("Ptr is in %s" % (str(p)))
    
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
