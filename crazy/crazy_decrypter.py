#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, string, sys
import itertools, hashlib

NAME        = 'Python Crazy Decrypter'
VERSION     = '0.0.3'
AUTHOR      = 'Summon Agus'
DESCRIPTION = NAME + ''' is real crazy tool
to decrypt md5, sha1, sha224, sha256, sha384, and sha512 with Brute Force method.'''

CHRS = string.printable.replace(' \t\n\r\x0b\x0c', '')
LIST_MODULES_TYPE = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']

def print_help():
    print '\n'+NAME
    print 'Author  : {}'.format(AUTHOR)
    print 'Version : {}\n'.format(VERSION)
    print DESCRIPTION
    print '''\nPARAMETERS:
    -m  \t To try with specific module choice.
    -a  \t To try with all modules.
    -c  \t To try with specific charachters.
    -ac \t To try with all charachters. \n\nUSAGE:
    SPECIFIC MODULE
     $ crazy_decrypter -m <module_type> <hashed> -c <chars> <min_length> <max_length>
     $ crazy_decrypter -m md5 d73d1e93a306b8230410cbe496ec84bf -c ABC 1 2

     $ crazy_decrypter -m <module_type> <hashed> -ac <min_length> <max_length>
     $ crazy_decrypter -m md5 d73d1e93a306b8230410cbe496ec84bf -ac 1 2

    ALL MODULES
     $ crazy_decrypter -a <hashed> -c <chars> <min_length> <max_length>
     $ crazy_decrypter -a d73d1e93a306b8230410cbe496ec84bf -c ABC 1 2

     $ crazy_decrypter -a <hashed> -ac <min_length> <max_length>
     $ crazy_decrypter -a d73d1e93a306b8230410cbe496ec84bf -ac 1 2
    '''

def decrypter(choice, module_type, hashed, chrs, min_length, max_length):

    if module_type in LIST_MODULES_TYPE:
        improt_module = getattr(hashlib, '{}'.format(module_type))
    else:
        print 'The `{}` does not exist in the list module!\nPlease try this:'.format(module_type)
        print LIST_MODULES_TYPE
        sys.exit()

    end_result_chip = ''

    try:
        for n in range(min_length, max_length+1):
            for xs in itertools.product(chrs, repeat=n):
                result_chip = ''.join(xs)
                hash_chip = improt_module(result_chip).hexdigest()
                if hashed == hash_chip:
                    end_result_chip += result_chip
                    print 'Decrypt found : {}'.format(end_result_chip)
                    print 'Type Decrypt  : {}'.format(module_type)
                    print 'End time      : {}\n'.format(time.strftime('%H:%M:%S'))
                    sys.exit()
                else:
                    print '   *** Please drink your coffee first! ***'
                    print '\t{} {}\n'.format(NAME, VERSION)
                    print 'CTRL+C to Exit!'
                    if choice == '-a' and module_type not in LIST_MODULES_TYPE[0]:
                        print 'Type Decrypt has been tried: {}'.format(LIST_MODULES_TYPE[:LIST_MODULES_TYPE.index(module_type)])
                    print 'Charachters to try : {}'.format(chrs)
                    print 'Type Decrypt now   : {}'.format(module_type)
                    print 'Trying with        : {} - {}'.format(result_chip, hash_chip)
                    time.sleep(0.01)
                    print("\033c")
    except KeyboardInterrupt:
        print 'Finished!\n'
        sys.exit()

    if end_result_chip == '' and choice == '-m':
        print 'Not Found!'
        print 'End time: {}\n'.format(time.strftime('%H:%M:%S'))
        sys.exit()
    elif end_result_chip == '' and choice == '-a':
        if module_type == LIST_MODULES_TYPE[-1]:
            print 'Not Found!'
            print 'End time: {}\n'.format(time.strftime('%H:%M:%S'))
            sys.exit()
        else: pass
    else: pass

if __name__ == '__main__':
    if len(sys.argv) == 1 or len(sys.argv) > 8: print_help()
    elif sys.argv[1] == '-m':
        try:
            if sys.argv[4] == '-c':
                decrypter(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[5], int(sys.argv[6]), int(sys.argv[7]))
            elif sys.argv[4] == '-ac':
                decrypter(sys.argv[1], sys.argv[2], sys.argv[3], CHRS, int(sys.argv[5]), int(sys.argv[6]))
            else: print_help()
        except IndexError: print_help()
    elif sys.argv[1] == '-a':
        try:
            for module_type in LIST_MODULES_TYPE:
                if sys.argv[3] == '-c':
                    decrypter(sys.argv[1], module_type, sys.argv[2], sys.argv[4], int(sys.argv[5]), int(sys.argv[6]))
                elif sys.argv[3] == '-ac':
                    decrypter(sys.argv[1], module_type, sys.argv[2], CHRS, int(sys.argv[4]), int(sys.argv[5]))
                else: print_help()
        except IndexError: print_help()
    else: print_help()