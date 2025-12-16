# Calcolatore di Interessi

Ho sviluppato una semplice e intuitiva applicazione web per il calcolo degli interessi, sia **semplici** che **composti**.  
Il progetto è suddiviso in:

- *Frontend* → HTML, CSS e JavaScript  
- *Backend* → Python con FastAPI e Jinja2 per i template  
- *Logica di calcolo* → file `calculator.py`, richiamato dal backend



# Funzionalità

La pagina permette di inserire:

- versamento iniziale  
- versamento periodico  
- durata in anni  
- tasso di interesse annuo  
- tipologia di interesse (semplice o composto)  
- frequenza dei versamenti (annuale, trimestrale, mensile)

Mostra poi:

- *Capitale finale*
- *Versamenti totali*
- *Interessi maturati*
- *Grafico dell’andamento del capitale nel tempo*



# Tecnologie utilizzate

- Python (FastAPI)
- HTML / CSS / JavaScript
- Jinja2 (template)
- Chart.js (grafico)



# Struttura del progetto

\Backend <   main.py (Applicazione FastApi)
            services/calculator.py (Logica di calcolo degli interessi) >

\Frontend < templates/index.html (Interfaccia web)
            static/style.css (Stili della pagina) >


#AVVIO APPLICAZIONE

    - Installare Python attraverso python.org
    - Installare i pacchetti necessari: py -m pip install fastapi uvicorn jinja2 python-multipart
    - Spostarsi nella cartella backend: cd backend
    - Avviare il server: uvicorn main:app --reload
    - Aprire nel Browser: http://127.0.0.1:8000/
