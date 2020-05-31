import os
import logging
from time import time, ctime
from os import system, name 
import pydash as _
import json
import jsonpickle
from json import JSONEncoder

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
    def print_preety(dict_object, header_only, *argv):
        pattern = ''
        vars = []

        for a in argv:
            key_name = a
            size = 16
            default_padding = 4            
            if(':' in key_name):
                key_name, size = Utils.parse_key_val(a, ':')
            pattern += '{:'+ str(int(size) + default_padding) + '.' + str(size) + '}'

            if header_only:
                vars.append(key_name)
            else :
                vars.append(str(_.get(dict_object,key_name)))

        print(pattern.format(*vars))

    @staticmethod
    def print_dict(dict_object, *argv):
        if argv: 
            for a in argv:
                print(f'--------------------{a}------------------------')
                print(_.get(dict_object, a))
        else:
            print(dict_object)


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


