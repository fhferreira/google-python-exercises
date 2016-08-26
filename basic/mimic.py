#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys


def mimic_dict(filename):
    """Returns mimic dict mapping each word to list of words which follow it."""
    # Abre o arquivo
    # Open a file
    myfile = open(filename, 'r')
    # save data of file inside a new variable
    # and replace all new lines by empty-string
    # atribui os dados do texto a uma váriavel
    # substitui as quebras de linhas por strings vazias
    data = myfile.read().replace('\n', '')
    # fecha-se o arquivo
    myfile.close()

    # quebra-se todas as palavras utilizando os
    # espaços como delimitadores
    # split all words on text by blank spaces
    words = data.split()
    # palavra inicial da iteração
    # fist word on iteration
    prevword = ''
    # dicionario inicializado
    # dict initialized
    mimic = {}

    for word in words:
        # se a palavra já existir no dicionario,
        # adiciona-a a lista existente, caso não,
        # crie uma nova lista com a palavra existente e adicione
        # as palavras que vierem na sequencia até que seja encontrada
        # uma nova palavra e uma nova lista seja iniciada
        if prevword in mimic:
            mimic[prevword].append(word)
        else:
            mimic[prevword] = [word]
        # update the current word
        # atualiza a palavra atual
        prevword = word

    return mimic


def print_mimic(mimic_dict, word):
    """Given mimic dict and start word, prints 200 random words."""
    for i in range(300):
        word = printnextword(mimic_dict, word)
    return


def printnextword(mimic_dict, word):
    next_word = random.choice(mimic_dict.get(word))
    print(next_word, end=' ')
    return next_word


# Provided main(), calls mimic_dict() and mimic()
def main():
    if len(sys.argv) != 2:
        print('usage: ./mimic.py file-to-read')
        sys.exit(1)

    dict = mimic_dict(sys.argv[1])
    print_mimic(dict, '')


if __name__ == '__main__':
    main()
