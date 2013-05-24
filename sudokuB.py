# coding: utf-8

# Autore: Daniele Buffa
# Originariamente scritto per il progetto Eulero
# Risolve sudoku legali ( che hanno una soluzione )
# Perch� sudokuB? esistevano varie versioni, questa � risultata la pi� veloce
 

from itertools import permutations
#import random
from copy import deepcopy
import os
import sys
import time

start_time = time.time()

num =[1,2,3,4,5,6,7,8,9] 
perm = list(permutations(num))

sudoku = [[],[],[],[],[],[],[],[],[]] 
#lo zero rappresenta un numero ignoto

var = int(sys.argv[1]) # es: 'pypy sudokuB.py 0' dove zero significa il primo sudoku di sudoku.txt
f=open("sudoku.txt").readlines()
f=[x.strip() for x in f]
for index,item in enumerate(f[1+10*var:10+10*var]):
    sudoku[index]=[int(x) for x in item]
           
def processa(r,tmp_list): 
    #prende una lista di potenziali candidati la filtra per le condizioni che non devono essere violate
    #restituisce una lista di potenziali candidati
    for index,item in enumerate(sudoku[r]):
        if item != 0: #sapendo il numero filtriamo in positivo
            tmp_list = [x for x in tmp_list if x[index] == item]
        elif item == 0: #la casella � vuota ma possiamo filtrare per quello che NON deve essere
            #perch� non else? volevo esplicitare la condizione per renderlo pi� chiaro
            #perch� non un altro if? perch� questa funzione verr� chiamata un sacco di volte e cos� lo costringeremmmo a controllare due condizioni mutualmente esclusive, cosa priva di senso
            colonna = [sudoku[x][index] for x in range(9)]
            quadrante = [sudoku[x][y] for x in range(0+((r/3)*3),3+((r/3)*3)) for y in range(0+((index/3)*3),3+((index/3)*3))]
            tmp_list = [x for x in tmp_list if x[index] not in (colonna+quadrante)]
    return tmp_list
    
def stampa():
    for x in sudoku:
        print " ".join([str(c) for c in x])
stampa()

righe_da_risolvere = range(9)
colonne_da_risolvere = range(9)
sudoku_bak = deepcopy(sudoku)
righe_da_risolvere_bak = righe_da_risolvere[:]
j = 1
posizione = "Root"
cache = {}
esclusi = {}
righe_modificate = []
righe_processate = [processa(x,perm) for x in righe_da_risolvere]


while righe_da_risolvere:
    
    riga = righe_da_risolvere[0] #Cerchiamo di risolverlo da 0 a 8 in maniera lineare
    
    if posizione in cache: #Salviamo i calcoli per evitare di rifarli ogni volta
        tmp = cache[posizione]
    else:
        tmp = processa(riga,righe_processate[riga])
        cache[posizione] = tmp
    
        
    if posizione in esclusi: #Non percorriamo di nuovo strade che non portano a niente
        candidati_validi = [x for x in range(len(tmp)) if x not in esclusi[posizione]]
    else:
        candidati_validi = range(len(tmp))
    
    if candidati_validi:
        n_candidato = candidati_validi[0] 
        candidato = tmp[n_candidato]
        sudoku[riga][:]=list(candidato) 
        righe_modificate.append(riga)
        righe_da_risolvere.remove(riga)
        posizione_candidato = ","+str(n_candidato)
        #tutto questo casino � per salvare la nostra posizione attuale 
        ultimo_candidato = n_candidato
        posizione_precedente = posizione[:]
        posizione += posizione_candidato
    else:
        #il tentativo non � andato a buon fine resettiamo la posizione iniziale e proviamo un altro percorso
        j += 1
        for x in righe_modificate:
            sudoku[x] = sudoku_bak[x][:]
        #sudoku[ultima_riga] = sudoku_bak[ultima_riga][:]
        righe_modificate=[]
        righe_da_risolvere[:] = righe_da_risolvere_bak[:]
        if posizione_precedente in esclusi:
            if not ultimo_candidato in esclusi[posizione_precedente]: 
                esclusi[posizione_precedente].append(ultimo_candidato)
        else:
            esclusi[posizione_precedente]=[ultimo_candidato]
        posizione = "Root"
        




print "*"*80
print "TROVATA SOLUZIONE al tentativo n",j
stampa()
        
#questa parte scrive l'output su un file
if False:""" 
f = open("soluzioni.txt","a")
f.write("Sudoku n"+str(var)+"\n")
for x in sudoku:
    f.write(str(x)+"\n")
f.close()
"""

print
print time.time()-start_time,"sec"
raw_input() 
