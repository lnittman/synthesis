#!/usr/bin/env python3
import argparse
import sys

from constants.config import GITHUB_OWNER, GITHUB_TOKEN, OPENAI_API_KEY
from src.synth import Synth

class Cli:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='synth cli')
        self.parser.add_argument('--repo', type=str, help='Name of the GitHub repository')
        self.parser.add_argument('--pr', type=int, help='Pull request number')
        self.parser.add_argument('--branch', type=int, help='Pull request number')
        self.parser.add_argument('--commit', type=int, help='Pull request number')
        self.parser.add_argument('--user', type=str, help='GitHub username for scoping actions')

    async def run(self):
        args = self._parse_args()
        synth = Synth(owner=GITHUB_OWNER, token=GITHUB_TOKEN, key=OPENAI_API_KEY)

        if args.user:
            synth.set_user(args.user)

        if args.branch:
            synth.branch(args.repo, args.branch)
        elif args.commit:
            synth.commit(args.repo, args.commit)
        elif args.pr:
            await synth.pull_request(args.repo, args.pr)
        elif args.repo:
            synth.repo(args.repo)
        else:
            print("No valid arguments provided")

    def _parse_args(self):
        args = self.parser.parse_args()

        if (args.pr or args.branch or args.commit) and not args.repo:
            self.parser.error("The --pr, --branch, and --commit arguments require --repo to be specified.")

        if not args.repo:
            self.parser.print_help()
            sys.exit(1)

        return args
