#!/usr/bin/env python3
import argparse

from fastapi import FastAPI
from logging import basicConfig, INFO
from subprocess import run

from constants.config import OWNER, TOKEN
from src.synth import Synth
from src.utils import kill_process_by_port

basicConfig(level=INFO)

app = FastAPI(title="Synth API")
synth = Synth(owner=OWNER, token=TOKEN)

@app.get("/")
async def root():
    return {"message": "Synth API is running"}

@app.get("/pull_request/")
async def pull_request(repo_name, pr_number):
    return synth.pull_request(repo_name, pr_number)

@app.get("/repo/")
async def repo(repo_name):
    return synth.repo(repo_name)

@app.get("/repos/")
async def repos(repos):
    return synth.repos(repos)

def main():
    parser = argparse.ArgumentParser(description='Analyze GitHub repositories for pull request quality.')
    parser.add_argument('--repo', type=str, help='Name of the GitHub repository')
    parser.add_argument('--pr', type=int, help='Pull request number')
    args = parser.parse_args()

    if args.repo and args.pr:
        synth.pull_request(args.repo, args.pr)
    elif args.repo:
        synth.repo(args.repo)
    else:
        run_service()

def run_service():
    kill_process_by_port(8000)    
    run(
        [
            "gunicorn",
            "app.main:app",
            "-k",
            "uvicorn.workers.UvicornWorker",
            "--bind",
            "192.168.1.210:8000",
            "--timeout",
            "0",
        ]
    )

if __name__ == "__main__":
    main()

