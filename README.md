# Synthesis

Synthesis is a project designed to offload GitHub processes to OpenAI, aiming to automate and streamline various GitHub operations using OpenAI's capabilities. This includes automating commits, pull requests, branch management, and project tracking to reduce manual effort and increase efficiency.

## Goals

The primary goal of Synth is to leverage OpenAI's advanced algorithms to automate GitHub processes, thereby improving the accuracy and efficiency of these operations.

## Implementation

The implementation involves a combination of Python scripts for executing GitHub operations, GitHub Actions for continuous integration and linting, and OpenAI's API for intelligent decision-making and automation.

### Key Modules

- **OpenAI Assistant**: Integrates with OpenAI's API to provide functionalities like committing changes, managing branches, handling pull requests, and more.
- **CLI Interface**: A command-line interface for interacting with Synth functionalities directly from the terminal.
- **GitHub Actions**: Configured to run linting on push events to ensure code quality and consistency.
- **Setup Script**: Facilitates the installation and setup of the Synth package, including its dependencies.

### Dependencies

Dependencies include `fastapi`, `gunicorn`, `psutil`, `openai`, and `PyGithub`, essential for the web server, OpenAI integration, and GitHub operations. These are listed in `requirements.txt`.

## Setup Steps

1. Clone the repository to your local machine.
2. Ensure Python 3.8 or higher is installed.
3. Install the dependencies with `pip install -r requirements.txt`.
4. Set up environment variables for `GITHUB_OWNER`, `GITHUB_TOKEN`, and `OPENAI_API_KEY`.

## Running the Application

To run the CLI interface, use the following command:

```bash
python app/cli.py --repo <repository_name> --pr <pull_request_number>
```

The CLI supports various arguments for different operations, such as `--repo`, `--pr`, `--branch`, and `--commit`.
