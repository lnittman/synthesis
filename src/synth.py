#!/usr/bin/env python3
from github import Auth, Github
from logging import basicConfig, info, INFO

from constants.config import EXCLUDE_FILE_TYPES, EXCLUDE_DIRS
from src.openai.assistant import Assistant

basicConfig(level=INFO)

class Synth:
    def __init__(self, owner: str, token: str):
        self.owner = owner
        self.token = token
        self.analysis = {}
        self.repos = {}

        self.assistant = Assistant()
        self.github = Github(auth=Auth.Token(token))

        for repo in self.github.get_user().get_repos():
            self.repos[repo.name] = repo
            
    def branch(self, repo, branch_name):
        info(f"Analyzing {repo} branch {branch_name}...")

    def commit(self, repo, sha):
        info(f"Analyzing {repo} commit {sha}...")

    def pull_request(self, repo, pr_number):
        info(f"Analyzing {repo} pull request #{pr_number}...")

    def repo(self, repo_name):
        info(f"Analyzing {repo_name}...")

        repo = self.repos[repo_name]
        info(f"Repository: {repo.name}")
        info(f"Description: {repo.description}")
        info(f"Language: {repo.language}")
        info(f"Forks Count: {repo.forks_count}")
        info(f"Stars: {repo.stargazers_count}")
        info(f"Watchers: {repo.watchers_count}")
        info(f"Open Issues: {repo.open_issues_count}")
        info(f"Created at: {repo.created_at}")
        info(f"Updated at: {repo.updated_at}")
        info(f"Pushed at: {repo.pushed_at}")
        info(f"Size: {repo.size} KB")

        code = self._get_file_content(repo, repo.get_contents(""))

        info(code)

    def _get_file_content(self, repo, directory_contents, path="", contents=None):
        if contents is None:
            contents = {}

        for content_item in directory_contents:
            if content_item.type == "dir":
                if content_item.name in EXCLUDE_DIRS:
                    continue

                dir_contents = repo.get_contents(content_item.path)
                self._get_file_content(repo, dir_contents, content_item.path, contents)
            else:
                if any(content_item.name.endswith(ext) for ext in EXCLUDE_FILE_TYPES):
                    continue

                file_path = f"{path}/{content_item.name}" if path else content_item.name
                try:
                    file_content = content_item.decoded_content.decode('utf-8')
                    contents[file_path] = file_content
                except Exception as e:
                    print(f"Error decoding content for {file_path}: {e}")

        return contents

