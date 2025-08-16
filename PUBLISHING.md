# SuperClaude PyPI Publishing Guide

This guide covers the complete process for publishing SuperClaude to PyPI (Python Package Index).

## 🚀 Quick Start

### 1. Validate Project Readiness
```bash
python3 scripts/validate_pypi_ready.py
```

### 2. Test Upload to TestPyPI
```bash
./scripts/publish.sh test
```

### 3. Test Installation
```bash
./scripts/publish.sh test-install
```

### 4. Production Upload
```bash
./scripts/publish.sh prod
```

## 📋 Prerequisites

### 1. PyPI Accounts
- **Production PyPI**: https://pypi.org/account/register/
- **TestPyPI**: https://test.pypi.org/account/register/

### 2. API Tokens
Generate tokens with appropriate permissions:
- **PyPI**: https://pypi.org/manage/account/ → API tokens
- **TestPyPI**: https://test.pypi.org/manage/account/ → API tokens

### 3. Local Configuration
Create `~/.pypirc`:
```ini
[pypi]
username = __token__
password = pypi-[your-production-token-here]

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-[your-test-token-here]
```

### 4. Install Required Tools
```bash
pip install --upgrade build twine toml
```

## 📦 Package Information

- **Package Name**: `SuperClaude`
- **Current Version**: `4.0.0b1` (beta release)
- **Entry Points**: 
  - `SuperClaude` → `SuperClaude.__main__:main`
  - `superclaude` → `SuperClaude.__main__:main`
- **Recent Improvements**: Enhanced PyPI publishing infrastructure with automated validation and deployment

## 🔧 Available Scripts

### Shell Script (Recommended)
```bash
# Test publishing
./scripts/publish.sh test

# Test installation from TestPyPI  
./scripts/publish.sh test-install

# Production publishing
./scripts/publish.sh prod

# Build package only
./scripts/publish.sh build

# Clean build artifacts
./scripts/publish.sh clean

# Validate project structure
./scripts/publish.sh check
```

### Python Script (Advanced)
```bash
# Basic TestPyPI upload
python3 scripts/build_and_upload.py --testpypi

# TestPyPI with installation test
python3 scripts/build_and_upload.py --testpypi --test-install

# Production upload
python3 scripts/build_and_upload.py

# Skip validation (faster)
python3 scripts/build_and_upload.py --skip-validation --testpypi

# Clean artifacts only
python3 scripts/build_and_upload.py --clean
```

### Validation Script
```bash
# Check if project is ready for publishing
python3 scripts/validate_pypi_ready.py
```

## 🤖 GitHub Actions Automation

The project includes automated publishing via GitHub Actions:

### Automatic Release Publishing
1. Create a new release on GitHub
2. GitHub Actions automatically builds and publishes to PyPI
3. Package becomes available on PyPI within minutes

### Manual Publishing
1. Go to GitHub Actions tab
2. Select "Publish to PyPI" workflow  
3. Click "Run workflow"
4. Choose target (testpypi or pypi)

### Required Secrets
Set these in GitHub repository settings:
- `PYPI_API_TOKEN`: Production PyPI token
- `TEST_PYPI_API_TOKEN`: TestPyPI token

## 📈 Version Management

### Current Version: 4.0.0b1
The project uses [semantic versioning](https://semver.org/) with beta notation:
- `4.0.0b1` = Version 4.0.0, Beta 1
- `4.0.0b2` = Version 4.0.0, Beta 2  
- `4.0.0` = Version 4.0.0, Stable Release

### Update Version Process
1. Update version in:
   - `pyproject.toml`
   - `SuperClaude/__init__.py`
   - `SuperClaude/__main__.py`
   - `setup/__init__.py`

2. Validate consistency:
   ```bash
   python3 scripts/validate_pypi_ready.py
   ```

3. Commit and tag:
   ```bash
   git add .
   git commit -m "Bump version to X.Y.Z"
   git tag vX.Y.Z
   git push origin main --tags
   ```

## 🔍 Package Structure

The package includes:
```
SuperClaude/
├── SuperClaude/          # Main package
│   ├── __init__.py       # Package metadata
│   ├── __main__.py       # CLI entry point
│   ├── Core/             # Framework core files
│   ├── Commands/         # Command definitions  
│   ├── Agents/           # Agent specifications
│   ├── Modes/            # Behavioral modes
│   └── MCP/              # MCP server configs
├── setup/                # Installation system
├── scripts/              # Publishing scripts
├── pyproject.toml        # Package configuration
├── README.md             # Project documentation
├── LICENSE               # MIT license
└── MANIFEST.in           # Package manifest
```

## 🧪 Testing

### Local Testing
```bash
# Build package
python3 -m build

# Check distribution
python3 -m twine check dist/*

# Test local installation
pip install dist/SuperClaude-4.0.0b1-py3-none-any.whl
```

### TestPyPI Testing
```bash
# Upload to TestPyPI
./scripts/publish.sh test

# Install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ \
           --extra-index-url https://pypi.org/simple/ \
           SuperClaude

# Test CLI
SuperClaude --version
```

## 🚨 Troubleshooting

### Common Issues

#### Version Already Exists
PyPI doesn't allow re-uploading the same version. Increment version number:
```bash
# Current: 4.0.0b1
# Next: 4.0.0b2 or 4.0.0
```

#### Import Errors
Check package structure and `__init__.py` files:
```bash
python3 scripts/validate_pypi_ready.py
```

#### Upload Failures
1. Check API tokens are correct
2. Verify network connectivity
3. Try TestPyPI first
4. Check PyPI status page

#### Build Failures
1. Ensure Python ≥3.8
2. Update build tools: `pip install --upgrade build twine`
3. Clean artifacts: `./scripts/publish.sh clean`

### Getting Help
- PyPI Help: https://pypi.org/help/
- Packaging Guide: https://packaging.python.org/
- GitHub Issues: https://github.com/SuperClaude-Org/SuperClaude_Framework/issues

## 📊 Publication Checklist

Before publishing to production PyPI:

- [ ] All tests passing
- [ ] Version number updated
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] TestPyPI upload successful
- [ ] TestPyPI installation test passed
- [ ] GitHub release created (for automatic publishing)

## 🎯 Production Publishing

### Option 1: GitHub Release (Recommended)
1. Push all changes to main branch
2. Create new release on GitHub with tag `v4.0.0b1`
3. GitHub Actions automatically publishes to PyPI

### Option 2: Manual Publishing
```bash
# Validate everything
python3 scripts/validate_pypi_ready.py

# Test on TestPyPI first
./scripts/publish.sh test
./scripts/publish.sh test-install

# Publish to production
./scripts/publish.sh prod
```

## 🔐 Security Best Practices

- Store API tokens securely (use `~/.pypirc` or environment variables)
- Never commit tokens to version control
- Use minimal permission tokens
- Regularly rotate API tokens
- Use Trusted Publishing for GitHub Actions when possible

## 📝 Post-Publication

After successful publication:

1. **Update README badges** with new version
2. **Announce release** on relevant channels
3. **Monitor for issues** in GitHub Issues
4. **Update documentation** if needed
5. **Plan next release** based on feedback

---

*For questions or issues with publishing, please open an issue on GitHub or contact the maintainers.*