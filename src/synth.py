#!/usr/bin/env python3
import os
import json
import requests

from itertools import islice
from github import Auth, Github
from logging import basicConfig, error, info, INFO

from constants.config import ALLOWED_FILE_TYPES, EXCLUDE_FILE_TYPES, EXCLUDE_DIRS, EXCLUDE_REPOS
from src.openai.assistant import Assistant

basicConfig(level=INFO)

class Synth:
    def __init__(self, owner: str, token: str, key: str):
        self.owner = owner
        self.token = token
        self.analysis = {}
        self.repos = {}
        self.file_contents = {}

        self.assistant = Assistant(key)
        self.github = Github(auth=Auth.Token(token))

        for repo in self.github.get_user().get_repos():
            if repo.name in EXCLUDE_REPOS:
                continue

            self.repos[repo.name] = repo

    def branch(self, repo_name, branch_name):
        info(f"Analyzing {repo_name} branch {branch_name}...")

    def commit(self, repo_name, commit_sha):
        info(f"Analyzing {repo_name} commit {commit_sha}...")

    async def pull_request(self, repo_name, pr_number):
        info(f"Analyzing {repo_name} pull request #{pr_number}...")

        try:
            repo = self.repos[repo_name]
        except KeyError:
            raise Exception(f"Repo {repo_name} not found")
    
        try:
            pull_request = repo.get_pull(pr_number)
        except Exception as e:
            raise Exception(f"Pull request #{pr_number} not found: {e}")
        
        info(f"Pull Request: {pull_request.title}")
        print(f"Pull Request Keys: {pull_request.keys()}")
        info(f"Description: {pull_request.body}")

        diff_url = repo.compare('main', 'dev').diff_url
        info(f"Diff URL: {diff_url}")

        diff_response = await requests.get(diff_url)
        print(f"Diff Response: {diff_response.status_code}")

        if diff_response.status_code == 200:
            diff_text = diff_response.text
        else:
            error(f"Failed to fetch diff from {diff_url} with status code {diff_response.status_code}")

        comments = pull_request.get_issue_comments()
        if comments.totalCount > 0:
            for comment in comments:
                print(f"{comment.user.login} commented: {comment.body}")
        else:
            print("No comments")

    def repo(self, repo_name):
        info(f"Analyzing {repo_name}...")

        try:
            repo = self.repos[repo_name]
        except KeyError:
            raise Exception(f"Repo {repo_name} not found")

        info(f"Repository: {repo.name}")
        info(f"Description: {repo.description}")
        info(f"Forks Count: {repo.forks_count}")
        info(f"Stars: {repo.stargazers_count}")
        info(f"Watchers: {repo.watchers_count}")
        info(f"Open Issues: {repo.open_issues_count}")
        info(f"Created at: {repo.created_at}")
        info(f"Updated at: {repo.updated_at}")
        info(f"Pushed at: {repo.pushed_at}")

        self.file_contents[repo_name] = self._get_repo_contents(repo)
        self._save_file_contents_to_disk(repo)

    def set_user(self, username):
        self.username = username
    
    def user(self, username):
        info(f"Analyzing {username}...")

    def _get_repo_contents(self, repo, path="", repo_contents={}):
        for content_item in repo.get_contents(path):
            if content_item.type == "dir":
                if content_item.name in EXCLUDE_DIRS:
                    continue

                new_path = f"{path}/{content_item.name}" if path else content_item.name
                self._get_repo_contents(repo, new_path, repo_contents)
            else:
                print(f"Getting file contents for {content_item.name}...")
                file_path = f"{path}/{content_item.name}" if path else content_item.name
                repo_contents[file_path] = self._get_file_info(content_item, file_path, repo_contents)

        return repo_contents
    
    def _get_file_info(self, content_item, path, repo_contents):
        file_extension = os.path.splitext(content_item.name)[1]
        if file_extension in EXCLUDE_FILE_TYPES or file_extension not in ALLOWED_FILE_TYPES:
            return None 

        file_path = f"{path}/{content_item.name}" if path else content_item.name

        try:
            file_content = content_item.decoded_content.decode('utf-8')
            info(f"Adding {file_path} to file contents...")
        except Exception as e:
            error(f"Error decoding content for {file_path}: {e}")
            return None

        return file_content 
    
    def _save_file_contents_to_disk(self, repo):
        repo_dir = os.path.expanduser(f"~/.synth/output/{self.owner}/{repo.name}/")
        if not os.path.exists(repo_dir):
            os.makedirs(repo_dir)

        file_name = f"{repo.name}.txt"
        file_path = os.path.join(repo_dir, file_name)

        with open(file_path, 'w') as f:
            for path, file_content in self.file_contents[repo.name].items():
                if not file_content:
                    continue

                condensed_content = file_content.replace('\n', '\\n')

                f.write(f"{path}: /// ")
                f.write(f"{condensed_content}\n")
