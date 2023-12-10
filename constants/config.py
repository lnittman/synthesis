GITHUB_OWNER = "lnittman"
GITHUB_TOKEN = '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'
OPENAI_API_KEY = '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'

MAIN_BRANCH = "main"
DEV_BRANCH = "dev"

ALLOWED_FILE_TYPES = [
    '.py',                              # Python files
    '.go',                              # Go files
    '.java',                            # Java files
    '.cs',                              # C# files
    '.cpp', '.hpp', '.c', '.h',         # C and C++ files
    '.env',                             # Environment files
    '.gitignore',                       # Gitignore files
    '.gitattributes',                   # Gitattributes files
    '.gitmodules',                      # Gitmodules files
    '.gitkeep',                         # Gitkeep files
    '.graphql',                         # GraphQL files
    '.html', '.css', '.scss',           # HTML and CSS files
    '.js', '.jsx', '.ts', '.tsx',       # JS and TS files
    '.rs',                              # Rust files
    '.swift',                           # Swift files
    '.yaml', '.yml',                    # YAML files
    '.php',                             # PHP files
    '.json',                            # JSON files
    '.rb',                              # Ruby files
    '.sh',                              # Shell files
    '.sql',                             # SQL files
    '.toml',                            # TOML files
    '.vim',                             # Vim files
    '.xml',                             # XML files
]

EXCLUDE_FILE_TYPES = [
    '.appxbundle',                      # Windows app bundle
    '.dll', '.exe',                     # Windows executables
    '.fbx', '.FBX'                      # 3D model
    '.ico',                             # Icon files
    '.md', '.txt',                      # Documentation and text files
    '.pdf',                             # PDF documents
    '.png', '.jpg', '.jpeg', '.gif',    # Images
    '.pyc',                             # Compiled Python files
    '.ttf', '.otf',                     # Fonts
    '.wav', '.aac', '.mp3', '.flac',    # Audio files
    '.whl', '.gz',                      # Distribution packages
    '.xcuserstate',                     # Xcode user state
    '.lock',                            # Lock files
]

EXCLUDE_FILES = [
    '.DS_Store',                        # Mac OS metadata
    '.gitignore',                       # Gitignore files
    '__init__.py',                      # Python init files
    'LICENSE',                          # License files
    'README.md',                        # Readme files
    'package-lock.json',                # NPM lock files
    'webpack.config.js',                # Webpack config files
    'webpack.config.prod.js',           # Webpack config files
    'webpack.config.dev.js',            # Webpack config files
    'webpack.config.common.js',         # Webpack config files
    'webpack.config.base.js',           # Webpack config files
    'webpack.config.vendor.js',         # Webpack config files
    'webpack.config.vendor.prod.js',    # Webpack config files
    'webpack.config.vendor.dev.js',     # Webpack config files
    'webpack.config.vendor.common.js',  # Webpack config files
    'webpack.config.vendor.base.js',    # Webpack config files
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
    'lib', 'libs',                      # Libraries
]

EXCLUDE_REPOS = [
    'pediatric-cardiac',
    'legalcontracts',
    'go-proto-gql',
    'goa-grpc-option',
    'graphql-merge-cli',
    'rainbowkit',
    'uppy',
]