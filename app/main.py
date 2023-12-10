#!/usr/bin/env python3
import asyncio
import os

from dotenv import load_dotenv

from app.api import run_service
from app.cli import Cli

load_dotenv()

async def run_cli():
    await Cli().run()

if __name__ == "__main__":
    if os.getenv('SYNTH_CLI'):
        asyncio.run(run_cli())
    else:
        run_service()
