#!/usr/bin/env python3
from github import Auth, Github
from src.openai.assistant import Assistant

class Synth:
    def __init__(self, owner: str, token: str):
        self.owner = owner
        self.token = token
        self.analysis = {}
        self.repos = {}

        self.assistant = Assistant()
        self.github = Github(auth=Auth.Token(token))

        for repo in self.github.get_user().get_repos():
            print(repo.name)
            self.repos[repo.name] = repo
            
    def branch(self, pr: int):
        pass

    def commit(self, sha: str):
        pass

    def pull_request(self, repo, pr_number):
        pr = self.repos[repo].get_pull(pr_number)
        # analysis = self.assistant.pull_request(repo, pr)
        # print(analysis)

    def repo(self, repo_name):
        print(self.repos[repo_name].get_pulls().totalCount)
        # analysis = self.assistant.repo(repo)
        # print(analysis)

    def repos(self, repo_names):
        pass
            
