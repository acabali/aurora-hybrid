from fastapi import FastAPI
import json, os

BASE = os.path.expanduser("~/aurora-hybrid/data")

app = FastAPI(title="Aurora Hybrid API")

def load(name):
    return json.load(open(os.path.join(BASE, name)))

@app.get("/status")
def status():
    return {"status": "ok"}

@app.get("/company")
def company():
    return load("company.json")

@app.get("/products")
def products():
    return load("products.json")

@app.get("/automations")
def automations():
    return load("automations.json")

@app.get("/agents")
def agents():
    return load("agents.json")
