import argparse
import os

from github import Github
from constants.config import ALLOWED_FILE_TYPES, EXCLUDE_DIRS, EXCLUDE_FILES, EXCLUDE_FILE_TYPES

def get_contents(input_path, owner, project_name=None):
    out_dir = os.path.expanduser(f"~/.synth/{owner}/code/{project_name}")
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    repo_name = os.path.basename(os.path.normpath(input_path))

    out_name = f"{repo_name}.txt"
    out_path = os.path.join(out_dir, out_name)
    with open(out_path, 'w') as out_file:
        out_file.write(f"File contents for {repo_name}:")
        for root, dirs, files in os.walk(input_path):
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

            for file in files:
                file_extension = os.path.splitext(file)[1]
                file_name = os.path.splitext(file)[0]

                full_path = os.path.join(root, file)
                relative_path = full_path.split(repo_name)[1][1:]

                if f"{file_name}{file_extension}" in EXCLUDE_FILES:
                    continue
                elif file_extension in EXCLUDE_FILE_TYPES:
                    continue
                elif file_extension not in ALLOWED_FILE_TYPES:
                    continue

                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path) / (1024 * 1024)
                if file_size > 0.2:
                    print(f'Large file: {file_path} ({file_size} MB)')

                try:
                    with open(file_path, 'r') as content_file:
                        relative_path = file_path.split(repo_name)[1][1:]
                        out_file.write(f"\n\n{relative_path}:\n\n")

                        file_content = content_file.read()
                        lines = file_content.split('\n')
                        for i, line in enumerate(lines, start=0):
                            if not line: continue
                            out_file.write(f"{i + 1}: {line.lstrip()}\\n")
                        
                        if not lines:
                            out_file.write(f"Empty file\\n")
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")

def concat_files(owner, project_name):
    base_dir = os.path.expanduser(f"~/.synth/{owner}/code/{project_name}")
    output_file = os.path.join(base_dir, f"concat.txt")

    with open(output_file, 'w') as outfile:
        for file in os.listdir(base_dir):
            repo_name = os.path.splitext(file)[0]
            if file.endswith(".txt") and file != "concat.txt" and repo_name != ".DS_Store" and file != ".idea.txt" and repo_name != ".aider.conf.yml":
                with open(os.path.join(base_dir, file), 'r') as infile:
                    print(f"{repo_name}")
                    outfile.write(infile.read())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Gets folder contents as a condensed txt file')
    parser.add_argument('--path', type=str, help='Path to a code repository')
    parser.add_argument('--project', type=str, help='Path to a project / workspace folder')
    parser.add_argument('--owner', required=True, type=str, help='Owner of the code repository')

    args = parser.parse_args()

    if args.project:
        project_name = os.path.basename(os.path.normpath(args.project))

        for dir in os.listdir(args.project):
            dir_path = os.path.join(args.project, dir)
            get_contents(dir_path, args.owner, project_name)
        
        concat_files(args.owner, project_name)
    else:
        input_path = args.path
        if not os.path.isdir(input_path):
            parser.error(f"Input path must be a directory.")

        get_contents(args.path, args.owner)
