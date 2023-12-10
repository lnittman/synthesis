#!/usr/bin/env python3
import os

from dotenv import load_dotenv

from app.api import run_service
from app.cli import Cli

load_dotenv()

if __name__ == "__main__":
    Cli().run() if os.getenv('SYNTH_CLI') else run_service()
