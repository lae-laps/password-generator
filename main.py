# Este script genera contraseñas aleatorias en base a algoritmos simples de construcción propia
# Se puede obtener una lista de todos los comandos con help

import os
import sys
import random

try:
    import pyperclip
except ModuleNotFoundError:
    print('\033[38;5;121m[+] Installing dependencies ~ Required\033[m')
    os.system('pip3 install pyperclip')
    import pyperclip

class GenerateRandomString:
    def __init__(self):
        self.__letter_dict = {
            1: 'a',
            2: 'b',
            3: 'c',
            4: 'd',
            5: 'e',
            6: 'f',
            7: 'g',
            8: 'h',
            9: 'i',
            10: 'j',
            11: 'k',
            12: 'l',
            13: 'm',
            14: 'n',
            15: 'o',
            16: 'p',
            17: 'q',
            18: 'r',
            19: 's',
            20: 't',
            21: 'u',
            22: 'w',
            23: 'x',
            24: 'y',
            25: 'z'
        }

        self.__number_dict = {
            1: '1',
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
            10: '0'
        }

        self.__symbol_dict = {
            1: '-',
            2: '<',
            3: '>',
            4: '!',
            5: '[',
            6: ']',
            7: '(',
            8: ')',
            9: '_',
            10: '+',
            11: '=',
            12: '@',
            13: '%',
            14: '#',
            15: '/',
            16: '$',
            17: '*'
        }

        self.length = 60
        self.letters = True
        self.numbers = True
        self.symbols = True
        self.option_number = 3
        self.allowed_types = []
        self.final_string = ''

    def set_length(self, length):
        if length == None:
            length = input('Longitud de contraseña: ')
        length = int(length)
        self.length = length

    def get_random_char(self, type):
        if type == 1:
            rand = random.randint(1, 25)
            return self.__letter_dict[rand]
        elif type == 2:
            rand = random.randint(1, 10)
            return self.__number_dict[rand]
        else:
            rand = random.randint(1, 17)
            return self.__symbol_dict[rand]

    def get_random_string(self):
        string = ''

        while True:
            random_type = random.randint(1, 3)
            random_char = self.get_random_char(random_type)
            
            if self.letters and random_type == 1:
                string += random_char
            elif self.numbers and random_type == 2:
                string += random_char
            elif self.symbols and random_type==3:
                string += random_char

            if len(string) == self.length:
                self.final_string = string
                password_string_object = Interface()
                password_string_object.cprint(string, 'green')
                return string
            
class Interface:
    def __init__(self):
        self.color_dict = {
            'green': '121',
            'red': '196',
            'blue': '51',
            'orange': '208',
            'light-green': '118'
        }

    def cprint(self, content, color) -> int:
        toprint = '\033[38;5;' + self.color_dict[color] + 'm' + content + '\033[m'
        lastcontent = content[-11:]
        if lastcontent == '/notnewline':
            print('\033[38;5;' + self.color_dict[color] + 'm' + content[:-11] + '\033[m', end=' ')
        else:
            print(toprint)
        return 0

    def banner(self):
        self.cprint('''                                                           _             
                                                          | |            
 _ __   __ _ ___ ___        __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| '_ \ / _` / __/ __|______/ _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| |_) | (_| \__ \__ \_____| (_| |  __/ | | |  __/ | | (_| | || (_) | |   
| .__/ \__,_|___/___/      \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|   
| |                         __/ |                                        
|_|                        |___/                  Created By: lae-laps''', 'blue')
        print()
        self.cprint('Usa help para obtener ayuda', 'light-green')

    def show(self):
        password_object = GenerateRandomString()
        while True:
            print()
            self.cprint('passgenerator > /notnewline', 'blue')
            option = input()
            print()
            options = option.split()
            header = options[0]

            if header == 'help': 
                self.cprint('''generate / gen .............. generar contraseña
  |> generate -c / -copy .... genera una contraseña y la copia
  |> generate <valor> ....... genera el número de contraseñas especificado
show conf ................... muestra la configuración
set <opción> <valor> ........ cambia un parámetro de la configuración
  |> length <valor> ......... cambia la longitud de la contraseña generada al valor dado
  |> letters <True/False> ... determina si la contraseña contiene letras
  |> numbers <True/False> ... determina si la contraseña contiene números
  |> symbols <True/False> ... determina si la contraseña comtiene símbolos
clear ....................... borra todo
help ........................ da esta ayuda acerca de los comandos
exit ........................ sale de la aplicación
    ''', 'green')
            elif header == 'generate' or header == 'gen':
                try:
                    options[1]
                    if options[1] == '-c' or options[1] == '-copy':
                        password_object.get_random_string()
                        pyperclip.copy(password_object.final_string)
                        print()
                        self.cprint('[+] ~ Contraseña copiada al portapapeles', 'light-green')
                    else:
                        range_number = int(options[1])
                            
                        for password in range(range_number):
                            password_object.get_random_string()
                            print()
                except:
                    password_object.get_random_string()

            elif header == 'set':
                try :
                    options[1]
                    if options[1] == 'length':
                        try:
                            password_object.set_length(options[2])
                        except:
                            password_object.set_length(None)
                    elif options[1] == 'letters':
                        if options[2] == 'True':
                            password_object.letters = True
                        else:
                            password_object.letters = False
                    elif options[1] == 'numbers':
                        if options[2] == 'True':
                            password_object.numbers = True
                        else:
                            password_object.numbers = False
                    elif options[1] == 'symbols':
                        if options[2] == 'True':
                            password_object.symbols = True
                        else:
                            password_object.symbols = False
                except:
                    self.cprint('[-] ~ Se obtuvo 1 argumento => Se esperaban 3', 'red')

            elif header == 'show':
                try: 
                    options[1]
                    if options[1] == 'conf':
                        self.cprint(f'Password length ... {password_object.length}', 'green')
                        self.cprint(f'Letters ........... {password_object.letters}', 'green')
                        self.cprint(f'Numbers ........... {password_object.numbers}', 'green')
                        self.cprint(f'Symbols ........... {password_object.symbols}', 'green')
                    else:
                        self.cprint('Option', options[1], 'does not exist', 'red')
                except:
                    self.cprint('[-] ~ Se esperaban 2 parametros => Se encontró solo uno', 'red')
            
            elif header == 'exit':
                self.cprint('Seguro que quieres salir de la aplicación [y/N]:/notnewline', 'orange')
                sure = input()
                if sure == 'y':
                    sys.exit()
            elif header == 'clear':
                os.system('clear')
            else:
                self.cprint('[-] ~ El comando no fué reconocido', 'red')

if __name__ == '__main__':
    interface_object = Interface()
    interface_object.banner()
    interface_object.show()
