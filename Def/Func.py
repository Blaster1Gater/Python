from colorama import Fore, Back
from random import choice

class Char:
    # Letras minúsculas do alfabeto latino
    letrasMin = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # Letras maiúsculas do alfabeto latino
    letrasMai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    # Letras minúsculas do alfabeto cirílico russo
    letrasCirilicoMin = [
        'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
        'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'
    ]
    
    # Letras maiúsculas do alfabeto cirílico russo
    letrasCirilicoMai = [
        'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О',
        'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я'
    ]

    # Números
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    # Combinar todas as listas
    tudo = letrasMin + letrasMai + letrasCirilicoMin + letrasCirilicoMai + numeros


class Cores:
    # Dicionário para mapear nomes de cores aos seus valores de Fore e Back
    coresFore = {
        'RED': Fore.RED,
        'GREEN': Fore.GREEN,
        'YELLOW': Fore.YELLOW,
        'BLUE': Fore.BLUE,
        'MAGENTA': Fore.MAGENTA,
        'CYAN': Fore.CYAN,
        'WHITE': Fore.WHITE,
    }

    coresBack = {
        'RED': Back.RED,
        'GREEN': Back.GREEN,
        'YELLOW': Back.YELLOW,
        'BLUE': Back.BLUE,
        'MAGENTA': Back.MAGENTA,
        'CYAN': Back.CYAN,
        'WHITE': Back.WHITE
    }

    normalFore = Fore.RESET
    normalBack = Back.RESET


class Inutilidades:
    @staticmethod
    def Wow():
        # Obter os nomes das cores
        nomes_cores_fore = list(Cores.coresFore.keys())
        nomes_cores_back = list(Cores.coresBack.keys())

        while True:
            # Escolher um nome de cor aleatório para texto e fundo
            nome_fore = choice(nomes_cores_fore)
            nome_back = choice(nomes_cores_back)

            # Garantir que as cores de texto e fundo sejam diferentes
            while nome_fore == nome_back:
                nome_back = choice(nomes_cores_back)

            # Recuperar os valores correspondentes (Fore e Back)
            fore = Cores.coresFore[nome_fore]
            back = Cores.coresBack[nome_back]

            # Exibir o caractere com as cores escolhidas
            print(f'{fore}{back}{choice(Char.tudo)}{Cores.normalBack}{Cores.normalFore}', end='')



class Ionalidades:
    def palavraAleatoria(tamanho):
        palavra = ''
        for _ in range(tamanho):
            palavra += choice(Char.letras)
        return palavra
