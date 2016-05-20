#Python Crazy Decrypter

:unlock: Python Crazy Decrypter is real crazy tool to decrypt md5, sha1, sha224, sha256, sha384, and sha512 with Brute Force method.

```
Python Crazy Decrypter
Author  : Summon Agus
Version : {VERSION}

Python Crazy Decrypter is real crazy tool
to decrypt md5, sha1, sha224, sha256, sha384, and sha512 with Brute Force method.

PARAMETERS:
    -m       To try with specific module choice.
    -a       To try with all modules.
    -c       To try with specific charachters.
    -ac      To try with all charachters. 

USAGE:
    SPECIFIC MODULE
     - crazy_decrypt.py -m <module_type> <hashed> -c <chars> <min_length> <max_length>
     - crazy_decrypt.py -m md5 d73d1e93a306b8230410cbe496ec84bf -c ABC 1 2

     - crazy_decrypt.py -m <module_type> <hashed> -ac <min_length> <max_length>
     - crazy_decrypt.py -m md5 d73d1e93a306b8230410cbe496ec84bf -ac 1 2

    ALL MODULES
     - crazy_decrypt.py -a <hashed> -c <chars> <min_length> <max_length>
     - crazy_decrypt.py -a d73d1e93a306b8230410cbe496ec84bf -c ABC 1 2

     - crazy_decrypt.py -a <hashed> -ac <min_length> <max_length>
     - crazy_decrypt.py -a d73d1e93a306b8230410cbe496ec84bf -ac 1 2
```

####Example Usage

```bash
$ python crazy_decrypt.py -a 2f2ec1296695a9fb3251bbc94a2e0cef -c ichp 4 4
```

####Example Proccess

```bash
   *** Please drink your coffee first! ***
    Python Crazy Decrypter 0.0.1

CTRL+C to Exit!
Type Decrypt has been tried: ['sha1', 'sha224']
Charachters to try : ichp
Type Decrypt now   : md5
Trying with        : ippc - 1ddae1fbbc4dcd27055140e831e2309d
```

####Example Result

```bash
Decrypt found : chip
Type Decrypt  : md5
End time      : 06:53:06
```

##INSTATALATION

```
$ python setup.py install
```

##LICENSE

* [MIT](https://github.com/agusmakmun/Crazy-Decrypter/blob/master/LICENSE)