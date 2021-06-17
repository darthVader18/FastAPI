from typing import Optional
from fastapi import FastAPI, Request
from app import SpeakText, time_zone, weather_by_city_name

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/speech")
def speech():
    return str(SpeakText())


@app.get("/timezone")
def timezone(city_name):
    return str(time_zone(city_name))


@app.get("/weather")
def weather(city_name):
    return str(weather_by_city_name(city_name))


#@app.post("/translate")
#def translation():
#    lang_from = request.args.get('from')
#    lang_to = request.args.get('to')
#    text = request.args.get('text')
#    return str(translate(lang_from, lang_to, text))


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)