OWNER = "StemsDAO"
TOKEN = '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'
OPENAI_API_KEY = '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'

EXCLUDE_FILE_TYPES = [
    '.md', '.txt',                      # Documentation and text files
    '.pyc',                             # Compiled Python files
    '.whl', '.gz',                      # Distribution packages
    '.png', '.jpg', '.jpeg', '.gif',    # Images
    '.pdf',                             # PDF documents
]

EXCLUDE_DIRS = [
    'node_modules',                     # Node.js modules
    '.git',                             # Git directory
    '__pycache__',                      # Python cache directory
    'dist',                             # Distribution directory
    'build',                            # Build directory
    '.idea',                            # IDE configuration directory
    '.vscode',                          # VSCode configuration directory
    'venv', 'env',                      # Virtual environments
    'synth.egg-info',                   # Python egg-info directory
]