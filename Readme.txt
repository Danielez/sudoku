Questo programmino risolve sudoku legali
Raggiunge la soluzione filtrando liste di candidati
La lista iniziale è la lista di tutte le possibili permutazioni di [1,2,3,4,5,6,7,8,9]
La lista viene successivamente filtrata rispetto alle condizioni che non devono essere violate:
nel sudoku una riga una colonna e il rispettivo quadrante devono essere contemporaneamente una permutazione valida.
L'Algoritmo viene ripetuto successivamente per ogni riga.
Per i sudoku più semplici basta il "filtro logico" (la funzione: "processa") pr trovare la soluzione.
Per quelli più complessi si procede a tentativi ma sempre usando candidati logicamente "validi".



 