#!/usr/bin/env python3
from enum import Enum
from src.github import Github 
from src.github.repository import Repository

class PullRequest():
    class State(Enum):
        OPEN = "open"
        CLOSED = "closed"
        ALL = "all"

    def __init__(self, github: Github, repository: Repository, pr_number: int):
        self.data = github.get_pull_request(repository, pr_number)
        self.repository = repository
