#!/usr/bin/env python3
from src.github import Github

class Repository():
    def __init__(self, github: Github, owner: str, name: str):
        self.owner = owner 
        self.name = name 

        self.data = github.get_repository(name)
        self.branches = github.list_branches(name)
