from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()

templates = Jinja2Templates(directory="templates")

url = "https://freetestapi.com/api/v1/weathers"

response = requests.get(url)
weather = response.json()

@app.get("/all_cities")
async def show_cities(request:Request):
    context = {"request":request,"weather":weather}
    return templates.TemplateResponse("all_cities.html",context)

@app.get("/city/{city_id}")
async def show_city(request:Request, city_id:int):
    for exiting_city in weather:
        if exiting_city["id"] == city_id:
            context = {"request":request,"exiting_city":exiting_city}
            return templates.TemplateResponse("city.html",context)
        
