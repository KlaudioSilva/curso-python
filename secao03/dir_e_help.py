"""
Utilitários Python para auxiliar na programação.

DIR -> Apresenta todos os atributos/propriedades e funções/métodos disponíveis
para determinado tipo de dado ou variável.
dir(tipo de dado/variável)

HELP -> Apresenta a documentação/como utilizar os atributos/propriedades e 
funções/métodos disponíveis para determinado tipo de dado ou variável.
help(tipo de dado/variável.propriedade)

é mais prático e rápido usando o console python.

>>> dir('Geek')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help('Geek'.lower)
Help on built-in function lower:

lower() method of builtins.str instance
    Return a copy of the string converted to lowercase.

Ou seja: usando o método lower na palavra 'Geek', toda a string será convertida para letras minúsculas.
Se tivéssemos usado o método upper, todas as letras serão convertidas para maiúsculas.
Veja o exemplo se utilizarmos o método title em um nome dentro de um banco de dados:

>>> 'josé KLAUDIO silva'.title()
'José Klaudio Silva'
>>>
"""