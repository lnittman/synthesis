#!/usr/bin/env python3
from fastapi import FastAPI
from psutil import process_iter
from subprocess import run

from constants.config import GITHUB_OWNER, GITHUB_TOKEN, OPENAI_API_KEY
from src.synth import Synth

app = FastAPI(title="Synth API")
synth = Synth(owner=GITHUB_OWNER, token=GITHUB_TOKEN, key=OPENAI_API_KEY)

@app.get("/")
async def root():
    return {"message": "Synth API is running"}

@app.get("/health")
async def health():
    return {"message": "Synth API is healthy"}

@app.get("/user/")
async def user(username):
    return synth.user(username)

@app.get("/repo/")
async def repo(repo_name):
    return synth.repo(repo_name)

@app.get("/pull_request/")
async def pull_request(repo_name, pr_number):
    return synth.pull_request(repo_name, pr_number)

@app.get("/branch/")
async def branch(repo_name, branch_name):
    return synth.pull_request(repo_name, branch_name)

@app.get("/commit/")
async def commit(repo_name, commit_sha):
    return synth.pull_request(repo_name, commit_sha)

def kill_process_by_port(port: int):
    for proc in process_iter(['pid', 'name', 'connections']):
        if proc.info['connections']:
            for conn in proc.info['connections']:
                if conn.laddr.port == port:
                    print(f"Killing process {proc.info['pid']} using port {port}")
                    proc.kill()
                    break

def run_service():
    kill_process_by_port(8000)
    run(["gunicorn", "app.main:app", "-c", "gunicorn_config.py"])

