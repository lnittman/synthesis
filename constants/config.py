GITHUB_OWNER = "lnittman"
GITHUB_TOKEN = "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"
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
    '.rb',                              # Ruby files
    '.sh',                              # Shell files
    '.sql',                             # SQL files
    '.toml',                            # TOML files
    '.vim',                             # Vim files
    '.xml',                             # XML files
    '.md',                              # Markdown files
]

EXCLUDE_FILE_TYPES = [
    '.appxbundle',                      # Windows app bundle
    '.dll', '.exe',                     # Windows executables
    '.fbx', '.FBX'                      # 3D model
    '.ico',                             # Icon files
    '.pdf',                             # PDF documents
    '.png', '.jpg', '.jpeg', '.gif',    # Images
    '.pyc',                             # Compiled Python files
    '.ttf', '.otf',                     # Fonts
    '.wav', '.aac', '.mp3', '.flac',    # Audio files
    '.whl', '.gz',                      # Distribution packages
    '.xcuserstate',                     # Xcode user state
    '.java',                            # Java files
    '.svg',                             # SVG files
    '.png',                             # PNG files
    '.pkl',                             # Pickle files
    '.1mzf',                            # 1mzf files
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
    'stems.abi.tsx',                    # stems-webapp ABI file
    'ensdomains.d.ts',                  # stems-webapp ENS domains file
    'introspection.json',               # GraphQL introspection files
    'RectAreaLightUniformsLib.js',
    'types.d.ts',
    'WebpackOptions.check.js',
    'async.js',
    'lodash.js',
]

EXCLUDE_DIRS = [
    '.next',                            # Next.js directory
    'out',                              # Output directory
    'node_modules',                     # Node.js modules
    'webview/node_modules',             # webview Node.js modules
    'shared',                           # Shared directory
    '.git',                             # Git directory
    '__pycache__',                      # Python cache directory
    'dist',                             # Distribution directory
    'build',                            # Build directory
    'Pods',                             # CocoaPods directory
    '.idea',                            # IDE configuration directory
    '.vscode',                          # VSCode configuration directory
    'vendor',                           # Vendor directory
    'venv', 'env',                      # Virtual environments
    'synth.egg-info',                   # Python egg-info directory
    'lib', 'libs',                      # Libraries
    '__tests__',                        # Test directory
    'android',                          # Android directory
    'swagger',                          # Swagger directory
    'protocol',                         # stems-backend protocol directory
    'collections',                      # stems-backend collections directory
    'postgresql',                       # stems-backend postgresql directory
    'keystore',                         # stems-backend keystore directory
    'docs',                             # stems-backend docs directory
    'pkg',                              # stems-backend pkg directory
    'logging', 'log'                    # stems-backend logging directory
    'ffmpeg-6.0/model',                 # stems-demucs ffmpeg directory
    'generated',                        # generated directory
    'contracts',                        # contracts directory
    'store',                            # storage directory
    'storybook',                        # storybook directory
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