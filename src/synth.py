#!/usr/bin/env python3
import os
import requests

from itertools import islice
from github import Auth, Github
from logging import basicConfig, info, INFO

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

            print(f'Adding repo {repo.name} to repos...')
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
        info(f"Description: {pull_request.body}")

        main_head = repo.get_branch('main')
        print(f"Main Head: {main_head.commit.sha}")

        dev_head = repo.get_branch('dev')
        print(f"Dev Head: {dev_head.commit.sha}")

        diff_url = repo.compare(dev_head.commit.sha, main_head.commit.sha).diff_url
        info(f"Diff URL: {diff_url}")

        diff_response = requests.get(diff_url)
        print(f"Diff Response: {diff_response.status_code}")

        if diff_response.status_code == 200:
            diff_text = diff_response.text
            print("Code Diff:\n", diff_text)
        else:
            print(f"Failed to fetch diff from {diff_url} with status code {diff_response.status_code}")

        comments = pull_request.get_issue_comments()
        if comments.totalCount > 0:
            print("Comments:")
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

        self.file_contents[repo_name] = self._collect_repo_file_contents(repo)

    def set_user(self, username):
        self.username = username
    
    def user(self, username):
        info(f"Analyzing {username}...")

    def _collect_repo_file_contents(self, repo):
        print(f"Getting file contents for {repo.name}...")
        self.file_contents[repo.name] = self._get_file_contents(repo, repo.get_contents(""))
        
    def _get_file_contents(self, repo, directory_contents, path="", contents={}):
        for content_item in directory_contents:
            if content_item.type == "dir":
                if content_item.name in EXCLUDE_DIRS:
                    continue

                dir_contents = repo.get_contents(content_item.path)
                self._get_file_contents(repo, dir_contents, content_item.path, contents)
            else:
                file_extension = os.path.splitext(content_item.name)[1]
                if file_extension in EXCLUDE_FILE_TYPES or file_extension not in ALLOWED_FILE_TYPES:
                    continue
    
                file_path = f"{path}/{content_item.name}" if path else content_item.name

                try:
                    file_content = content_item.decoded_content.decode('utf-8')
                    print(f"Adding {file_path} to file contents...")
                    contents[file_path] = file_content
                except Exception as e:
                    print(f"Error decoding content for {file_path}: {e}")

        return contents
