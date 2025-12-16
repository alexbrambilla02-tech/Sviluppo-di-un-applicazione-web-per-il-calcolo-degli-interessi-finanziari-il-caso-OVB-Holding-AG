"""
Progetto di Laurea - Calcolatore di Interessi
Autore: [Alex Brambilla]
Corso di Laurea in Informatica Per Le Aziende Digitali- A.A. 2024/2025

Questo file rappresenta il punto di ingresso dell'applicazione FastAPI.
Gestisce le rotte principali e collega la parte logica di calculator.py
con l'interfaccia web realizzata in HTML, CSS e JavaScript.
"""

from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
#Utilizzo Jinja2
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Import della logica di calcolo dal modulo dedicato
from services.calculator import calcola

# Inizializzazione dell’applicazione FastAPI
app = FastAPI(
    title="Calcolatore di Interessi",
    version="1.0",
    description="Applicazione per il calcolo di interessi semplici e composti"
)

# Montaggio della cartella dei file statici (CSS, JS, immagini)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Inizializzazione della cartella dei template HTML
templates = Jinja2Templates(directory="templates")



# ROTTA PRINCIPALE (GET)
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """
    Visualizza la pagina iniziale dell'applicazione.
    Da qui l'utente può inserire i dati del calcolo.
    """
    return templates.TemplateResponse("index.html", {"request": request})


# ROTTA API-BASED UFFICIALE (calcolo via backend, risposta JSON)
@app.post("/api/calculate")
async def api_calculate(
    vers_iniziale: float = Form(...),
    vers_periodico: float = Form(...),
    anni: float = Form(...),
    interesse: float = Form(...),
    tipo: str = Form(...),
    frequenza: str = Form(...)
):
    """
    Endpoint API-based: usato dal frontend tramite fetch().
    Restituisce un JSON con i risultati del calcolo.
    """
    try:
        risultati = calcola(vers_iniziale, vers_periodico, interesse, anni, tipo, frequenza)
        return JSONResponse(content=risultati)
    except Exception as e:
        print("Errore API:", e)
        raise HTTPException(status_code=400, detail= "Dati non validi o errore nel calcolo.")
