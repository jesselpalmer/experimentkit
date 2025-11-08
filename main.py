from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI(title="Experiment Engineer", version="0.1.0")

app.mount("/static", StaticFiles(directory="ui/static"), name="static")

@app.get("/", response_class=HTMLResponse)
def home():
    return """<html><body><h1>Experiment Engineer</h1>
    <p>Upload a dataset at <code>/upload</code> then call <code>/plan</code>.</p></body></html>"""
