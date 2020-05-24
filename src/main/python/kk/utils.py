import os
import logging
from time import time, ctime
from os import system, name 
import pydash as _

class Utils:

    @staticmethod
    def clear():
        # for windows 
        if name == 'nt': 
            _ = system('cls') 
    
        # for mac and linux(here, os.name is 'posix') 
        else: 
            _ = system('clear')     

    @staticmethod
    def print_preety(dict_object, *argv):
        pattern = ''
        vars = []

        for a in argv:
            key_name = a
            size = 16
            default_padding = 4            
            if(':' in key_name):
                key_name, size = Utils.parse_key_val(a, ':')
            pattern += '{:'+ str(int(size) + default_padding) + '.' + str(size) + '}'
            vars.append(str(_.get(dict_object,key_name)))

        print(pattern.format(*vars))

    def append_to_logfile(txt):
        f=open("k8s_events.log", "a+")
        f.write(txt)
        f.write(f"\n-----------------------------------------{ctime(time())}----------------------------------------------------\n")
        f.close()

    @staticmethod
    def parse_key_val(param, delim = '='):
        if param is None:
            return ()
        _split = param.split(delim)
        return (_split[0], _split[1])


