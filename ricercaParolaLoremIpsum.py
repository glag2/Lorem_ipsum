from threading import Thread
import time

def cerca_parola(testo,parola):
    start_time = time.time()
    trovato = False
    risultato = []
    for i, riga in enumerate(testo,1):
        if parola in riga:
            risultato.append((i, riga.index(parola) + 1))
            trovato = True
    if not trovato:
        risultato.append("Parola non presente")
    end_time = time.time()
    print(risultato)
    print("Tempo di esecuzione:", end_time - start_time, "secondi")

try:
    file = open("Lorem ipsum.txt", "r")
except FileNotFoundError as e:
    print("Errore: il file non esiste")
    exit()
while True:
    print("premere q per uscire")
    ricerca = input("Inserisci la parola che vuoi cercare nel file: ")
    if ricerca == 'q': 
        file.close()
        exit()
    thread = Thread(target=cerca_parola, args=(file,ricerca))
    thread.start()
    thread.join()
    file.seek(0)
