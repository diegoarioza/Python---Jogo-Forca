#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 17:52:34 2018

@author: diego
"""
import random
import os
import time

# Board (tabuleiro)
board = ['''
+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

class Hangman():
    def __init__(self, word_tip):
        self.word = word_tip[0]
        self.tip = word_tip[1]
        self.letras_acerto = []
        self.letras_erro = []
        self.palavra = "_"

                
    def perg_letra(self):
        try:
            letra_escolhida = input("Por Favor Digite uma letra: ")[0].lower()
            if len(letra_escolhida) > 1:
                print("Digite apenas uma letra, será considerada a primeira letra da palavra digitada - (" + letra_escolhida[0] + ")")
                time.sleep(4)
            return letra_escolhida
        except IndexError:
            print("digite uma letra apenas...")
            time.sleep(3)
            return " "
        except KeyboardInterrupt:
            print("\n\nJogo Fechado...")
            exit()
        
    def testar_letra(self):
        letra = self.perg_letra()
        if letra in self.word and letra not in self.letras_acerto:
            self.letras_acerto.append(letra)
        
        elif letra not in self.word and letra not in self.letras_erro:
            self.letras_erro.append(letra)
        
    def imprimir_palavra(self):
        self.palavra = ""
        for i in self.word:
            if i in self.letras_acerto:
                self.palavra += i + " "
            elif i == " ":
                self.palavra += "  "
            else: 
                self.palavra += "_ "
        return self.palavra
            
        
    def letras_corretas(self):
        return self.letras_acerto,len(self.letras_acerto)
    
    def letras_incorretas(self):
        return self.letras_erro,len(self.letras_erro)
    
    def ganhou(self):
        if len(self.letras_erro) >= 6:
            print("Perdeu , Tente de Novo !!!\n")
            print("Palavra era: ", self.word)
            print("Voce obteve", round((self.letras_corretas()[1] / (self.letras_incorretas()[1] + self.letras_corretas()[1])) * 100),"% de acerto")
            return True
        elif "_" in self.palavra:
            return False
        else:
            print("Parabens, voce ganhou !!!")
            print("Voce obteve", round((self.letras_corretas()[1] / (self.letras_incorretas()[1] + self.letras_corretas()[1])) * 100),"% de acerto")
            return True
    
def rand_word():
    with open("palavras.csv", "rt") as f:
        bank = f.readlines()
        #return bank[random.randint(0,len(bank)-1)].strip().lower()
        return bank[random.randint(0,len(bank)-1)].lower().strip().split(',')

def main():
    game = Hangman(rand_word())
    print("Jogo da Forca b\n",board[game.letras_incorretas()[1]])
    print("\nPalavra:", game.imprimir_palavra())
    print("\nDica:", game.tip)
    
    while not game.ganhou():
        game.testar_letra()
        
        os.system('clear')
        print(board[game.letras_incorretas()[1]])
        print("\nPalavra:", game.imprimir_palavra())
        print("\nDica:", game.tip)
        print("\nLetras Erradas: ", "-".join(game.letras_erro))
              
      

if __name__ == "__main__":
    main()
  
    
#print(rand_word())

            
