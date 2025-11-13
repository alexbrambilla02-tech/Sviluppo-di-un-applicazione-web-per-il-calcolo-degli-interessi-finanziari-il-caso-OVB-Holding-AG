import math

"""
Progetto di Laurea - Calcolatore di Interessi
Autore: [Alex Brambilla]
Corso di Laurea in Informatica Per Le Aziende Digitali - A.A. 2024/2025

Questo file calculator contiene le funzioni per il calcolo dell'interesse
semplice e composto, usate dall'applicazione web principale.
"""

# Funzione per formattare un numero nel formato italiano
def formatta_euro(valore):
    # Esempio: 100000 -> "100.000,00"
    return f"{valore:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# Calcolo con interesse semplice 
def interesse_semplice(versamento_iniziale, vers_periodico, tasso, anni, frequenza):
    if versamento_iniziale < 0 or vers_periodico < 0 or tasso < 0 or anni < 0:
        raise ValueError("Tutti i valori devono essere positivi.")

    i = tasso / 100.0
    n = int(frequenza)
    m = int(n * anni)

    # Interesse semplice sul versamento iniziale
    mont_iniz = versamento_iniziale * (1 + i * anni)

    # Interesse semplice sui versamenti periodici (media temporale = (m-1)/(2n))
    mont_per = vers_periodico * m + vers_periodico * i * ((m - 1) / (2 * n))

    mont_tot = mont_iniz + mont_per
    vers_tot = versamento_iniziale + vers_periodico * m
    interessi = mont_tot - vers_tot

    return {
        "Montante Totale": formatta_euro(round(mont_tot, 2)),
        "Interessi Maturati": formatta_euro(round(interessi, 2)),
        "Versamenti Totali": formatta_euro(round(vers_tot, 2))
    }


# Calcolo con interesse composto (capitalizzazione periodica)
def interesse_composto(versamento_iniziale, vers_periodico, tasso, anni, frequenza):
    # Conversione e validazione
    versamento_iniziale = float(versamento_iniziale)
    vers_periodico = float(vers_periodico)
    tasso = float(tasso)
    anni = float(anni)
    n = int(frequenza)

    if versamento_iniziale < 0 or vers_periodico < 0 or tasso < 0 or anni < 0:
        raise ValueError("Tutti i valori devono essere positivi.")

    i = tasso / 100.0

    # Versamento iniziale capitalizzato
    mont_iniz = versamento_iniziale * math.pow((1 + i / n), n * anni)

    # Piano di accumulo dei versamenti periodici (gestisce tasso = 0)
    if i == 0:
        mont_per = vers_periodico * n * anni
    else:
        mont_per = vers_periodico * (math.pow(1 + i / n, n * anni) - 1) / (i / n)

    # Totale finale e interessi maturati
    mont_tot = mont_iniz + mont_per
    vers_tot = versamento_iniziale + vers_periodico * n * anni
    interessi = mont_tot - vers_tot

    return {
        "Montante Totale": formatta_euro(round(mont_tot, 2)),
        "Interessi Maturati": formatta_euro(round(interessi, 2)),
        "Versamenti Totali": formatta_euro(round(vers_tot, 2))
    }


# Funzione principale di calcolo, usata dal backend FastAPI nel main
def calcola(vers_iniz, vers_per, interesse, anni, tipo, freq_str):
    frequenze = {
        "annuale": 1,
        "trimestrale": 4,
        "mensile": 12
    }

    tipo = tipo.lower().strip()
    freq_str = freq_str.lower().strip()

    if freq_str not in frequenze:
        raise ValueError("Frequenza non valida. Usa 'annuale', 'trimestrale' o 'mensile'.")

    freq = frequenze[freq_str]

    # Seleziono il tipo di calcolo in base alla scelta dell’utente
    if tipo == "semplice":
        return interesse_semplice(vers_iniz, vers_per, interesse, anni, freq)
    elif tipo == "composto":
        return interesse_composto(vers_iniz, vers_per, interesse, anni, freq)
    else:
        raise ValueError("Tipo di interesse non valido. Usa 'semplice' o 'composto'.")
