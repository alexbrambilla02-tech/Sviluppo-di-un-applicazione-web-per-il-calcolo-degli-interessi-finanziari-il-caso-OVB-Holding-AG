"""
Progetto di Laurea - Calcolatore di Interessi
Autore: [Alex Brambilla]
Corso di Laurea in Informatica Per Le Aziende Digitali- A.A. 2024/2025

Questo file rappresenta il punto di ingresso dell'applicazione FastAPI.
Gestisce le rotte principali e collega la parte logica di calculator.py
con l'interfaccia web realizzata in HTML, CSS e JavaScript.
"""

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
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



# ROTTA DI CALCOLO (POST)

@app.post("/calculate", response_class=HTMLResponse)
async def calculate(
    request: Request,
    vers_iniziale: float = Form(...),
    vers_periodico: float = Form(...),
    anni: float = Form(...),
    interesse: float = Form(...),
    tipo: str = Form(...),
    frequenza: str = Form(...)
):
    """
    Riceve i dati inviati dal form, esegue il calcolo
    e restituisce i risultati all’utente tramite il template HTML.
    """
    context = {"request": request}

    try:
        risultati = calcola(vers_iniziale, vers_periodico, interesse, anni, tipo, frequenza)
        context["risultati"] = risultati
    except Exception as e:
        print("Errore durante il calcolo:", e)
        context["errore"] = "Si è verificato un problema durante il calcolo. Controllare i dati inseriti."

    return templates.TemplateResponse("index.html", context)
