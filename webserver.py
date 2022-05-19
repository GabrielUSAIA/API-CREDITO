from fastapi import FastAPI, Form, Request
import requests
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

url="http://127.0.0.1:8000/predict"
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/consultar")
async def consultar(nombre: str=Form(...),
            sexo :str=Form(...), 
            edad: int=Form(...), 
            monto: int=Form(...),
            vivienda: str=Form(...)):

    response = requests.post(url, {"sexo": sexo, "edad": edad, "monto": monto, "vivienda": vivienda})
    respuesta = response.json()
    if respuesta["prob_bad_client"] > 0.5:
        mensaje = f"<h2>Apreciado {nombre}, su credito fue denegado</h2>"
    else:
        mensaje = f"<h2>Apreciado {nombre}, su credito fue aprobado</h2>"
    return mensaje


