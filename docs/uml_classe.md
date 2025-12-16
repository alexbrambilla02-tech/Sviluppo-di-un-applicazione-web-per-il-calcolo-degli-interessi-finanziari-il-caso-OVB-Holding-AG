classDiagram
    direction LR

    class InputParameters {
        +float vers_iniziale
        +float vers_periodico
        +float interesse
        +float anni
        +string tipo
        +string frequenza
    }

    class CalculationResult {
        +string Montante Totale
        +string Interessi Maturati
        +string Versamenti Totali
    }

    class InterestCalculatorService {
        <<Service>>
        +calcola(params) InputParameters: CalculationResult
        +interesse_semplice(p, a, i, n, freq): CalculationResult
        +interesse_composto(p, a, i, n, freq): CalculationResult
        +formatta_euro(valore): string
    }

    class APIController {
        <<Controller>>
        +post /api/calculate(formData): JSONResponse
    }

    APIController --o InputParameters : 1 riceve
    APIController --> InterestCalculatorService : 1 esegue il calcolo
    InterestCalculatorService --o CalculationResult : 1 restituisce
