sequenceDiagram
    participant Utente
    participant FE as Interfaccia Web (HTML/JS)
    participant BE as API FastAPI (main.py)
    participant CL as Logica di Calcolo (calculator.py)

    Utente->>FE: 1. Inserisce i parametri di calcolo e clicca 'Calcola'
    FE->>BE: 2. Richiesta POST /api/calculate (Form Data: vers_iniziale, anni, tipo, ecc.)
    activate BE
    BE->>CL: 3. Chiama la funzione calcola() con tutti i parametri di input
    activate CL
    CL-->>BE: 4. Restituisce il dizionario dei risultati (Montante, Interessi, Versamenti)
    deactivate CL
    BE-->>FE: 5. Restituisce JSONResponse (contenuto: risultati formattati)
    deactivate BE
    FE->>Utente: 6. Aggiorna l'interfaccia con i risultati estratti dal JSON
