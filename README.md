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
     $ crazy_decrypter -m <module_type> <hashed> -c <chars> <min_length> <max_length>
     $ crazy_decrypter -m md5 d73d1e93a306b8230410cbe496ec84bf -c ABC 1 2

     $ crazy_decrypter -m <module_type> <hashed> -ac <min_length> <max_length>
     $ crazy_decrypter -m md5 d73d1e93a306b8230410cbe496ec84bf -ac 1 2

    ALL MODULES
     $ crazy_decrypter -a <hashed> -c <chars> <min_length> <max_length>
     $ crazy_decrypter -a d73d1e93a306b8230410cbe496ec84bf -c ABC 1 2

     $ crazy_decrypter -a <hashed> -ac <min_length> <max_length>
     $ crazy_decrypter -a d73d1e93a306b8230410cbe496ec84bf -ac 1 2
```

####Example Usage

```bash
$ crazy_decrypter -a 2f2ec1296695a9fb3251bbc94a2e0cef -c ichp 4 4
```

####Example Proccess

```bash
   *** Please drink your coffee first! ***
    Python Crazy Decrypter 0.0.3

CTRL+C to Exit!
Charachters to try : ichp
Min-length         : 3
Max-length         : 4
Type Decrypt found : md5
Trying with        : iipc - 373fa60ea77f4695bc05fbc1b49d40e3
```

####Example Result

```bash
Decrypt found : chip
Type Decrypt  : md5
End time      : 06:53:06
```

##INSTALATION

```
$ python setup.py install
```

##LICENSE

* [MIT](https://github.com/agusmakmun/Crazy-Decrypter/blob/master/LICENSE)