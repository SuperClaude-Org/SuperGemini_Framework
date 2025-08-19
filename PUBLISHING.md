# SuperGemini PyPI Publishing Guide

SuperGemini Framework is published to PyPI as a Python package with automated CI/CD workflows for testing, validation, and release management. The publishing process includes comprehensive testing, security validation, and multi-platform compatibility verification.

**Publishing Workflow Overview:**
1. **Development**: Feature development with comprehensive testing
2. **Version Management**: Semantic versioning and changelog updates
3. **Pre-Publication Testing**: TestPyPI validation and integration testing
4. **Quality Gates**: Security scanning, dependency validation, cross-platform testing
5. **Production Release**: PyPI publication with automated distribution
6. **Post-Release**: GitHub release creation, documentation updates, community notification

**Package Distribution:**
- **Primary**: PyPI (pip install SuperGemini)
- **Alternative**: npm (npm install -g superclaude) for Node.js environments
- **Development**: Direct GitHub installation for contributors and testers

## 🚀 Quick Start

**For Maintainers (Production Publishing):**
```bash
# 1. Prepare release
python scripts/validate_pypi_ready.py
git tag v4.0.1
git push origin v4.0.1

# 2. GitHub Actions handles the rest automatically
# - Builds package
# - Tests on multiple platforms
# - Publishes to PyPI
# - Creates GitHub release
```

**For Contributors (Testing):**
```bash
# 1. Local development testing
pip install -e ".[dev]"
python -m pytest tests/

# 2. Package validation
python scripts/validate_pypi_ready.py

# 3. TestPyPI testing (maintainers only)
python -m build
twine upload --repository testpypi dist/*
```

**For Users (Installation):**
```bash
# Production installation
pip install SuperGemini

# Development version
pip install git+https://github.com/SuperGemini-Org/SuperGemini_Framework.git

# Specific version
pip install SuperGemini==4.0.0
```

**Automated Release Process:**
- Git tag creation triggers GitHub Actions workflow
- Automated testing across Python 3.8-3.12 and multiple OS platforms
- Security scanning and dependency validation
- Automatic PyPI publication on successful validation
- GitHub release creation with changelog and artifacts

## 📋 Prerequisites

**PyPI Account Setup:**

**Account Requirements:**
- PyPI account: https://pypi.org/account/register/
- Two-factor authentication enabled (required for package maintenance)
- Project maintainer access to SuperGemini package
- TestPyPI account: https://test.pypi.org/ (for testing)

**API Token Configuration:**

**For GitHub Actions (Maintainers):**
```bash
# Generate PyPI API token with SuperGemini package scope
# Add to GitHub repository secrets as PYPI_API_TOKEN
# Token format: pypi-AgEIcHl... (scoped to SuperGemini package)
```

**For Local Publishing (Emergency Only):**
```bash
# Create ~/.pypirc file (never commit this)
[distutils]
index-servers = pypi testpypi

[pypi]
username = __token__
password = pypi-AgEIcHl...

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-AgEIcHl...
```

**Security Best Practices:**
- Use scoped API tokens (package-specific, not account-wide)
- Rotate tokens regularly (quarterly recommended)
- Never commit tokens or credentials to version control
- Use GitHub secrets for automated workflows
- Enable PyPI security notifications

**Permission Management:**
- Maintainer-level access required for publishing
- Owner permissions for critical package configuration
- Trusted publisher configuration for GitHub Actions (recommended)
- Regular review of package collaborator access
**Development Environment Setup:**

**Python Environment:**
```bash
# Python 3.8+ required
python3 --version

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# For Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"
```

**Required Tools:**
```bash
# Core publishing tools
pip install build twine wheel

# Development and testing tools
pip install pytest pytest-cov black flake8 mypy

# Security scanning
pip install safety bandit
```

**Local Configuration:**
```bash
# Verify package structure
python scripts/validate_pypi_ready.py

# Build package locally
python -m build

# Verify package contents
twine check dist/*

# Local installation test
pip install dist/SuperGemini-*.whl
```

**Git Configuration:**
```bash
# Configure for release tagging
git config user.name "Your Name"
git config user.email "your.email@example.com"

# GPG signing (recommended for releases)
git config commit.gpgsign true
git config tag.gpgsign true
```

**IDE Setup:**
- Configure Python interpreter to use virtual environment
- Enable linting and formatting tools (black, flake8, mypy)
- Set up testing framework integration
- Configure Git integration for commit signing
**Core Publishing Dependencies:**
- **build**: Modern Python package building (PEP 517/518)
- **twine**: Secure package uploading to PyPI
- **wheel**: Binary distribution format support
- **setuptools**: Package metadata and entry point management

**Development Dependencies:**
- **pytest**: Testing framework with comprehensive coverage
- **pytest-cov**: Code coverage analysis and reporting
- **black**: Code formatting for consistent style
- **flake8**: Linting and style checking
- **mypy**: Static type checking and validation

**Security Dependencies:**
- **safety**: Dependency vulnerability scanning
- **bandit**: Security linting for Python code
- **pip-audit**: Comprehensive dependency security analysis
- **twine**: Secure upload with signature verification

**CI/CD Dependencies:**
- **GitHub Actions**: Automated testing and deployment
- **tox**: Multi-environment testing automation
- **coverage**: Test coverage measurement and reporting
- **codecov**: Coverage reporting and integration

**Optional Tools:**
- **bumpversion**: Automated version management
- **changelog-generator**: Automated changelog creation
- **pre-commit**: Git hook automation for quality gates
- **sphinx**: Documentation generation (if needed)

**Platform Requirements:**
- **Python**: 3.8, 3.9, 3.10, 3.11, 3.12 (tested compatibility)
- **Operating Systems**: Linux, macOS, Windows (cross-platform testing)
- **Architecture**: x86_64, ARM64 (multi-architecture support)
- **Dependencies**: Minimal external dependencies for broad compatibility

## 📦 Package Information

**Package Information:**

**Package Name**: `SuperGemini`
**Current Version**: 4.0.0 (Major release with v4 architecture)
**PyPI URL**: https://pypi.org/project/SuperGemini/
**GitHub URL**: https://github.com/SuperGemini-Org/SuperGemini_Framework

**Entry Points:**
```python
[console_scripts]
SuperGemini = superclaude.cli:main
superclaude = superclaude.cli:main  # Alternative entry point
```

**Package Structure:**
```
SuperGemini/
├── superclaude/           # Main package code
│   ├── __init__.py       # Package initialization and version
│   ├── cli.py            # Command-line interface
│   ├── core/             # Core framework functionality
│   ├── setup/            # Installation and component management
│   └── utils/            # Utility functions and helpers
├── setup.py              # Package configuration and metadata
├── pyproject.toml        # Modern Python packaging configuration
├── README.md             # Package description for PyPI
├── CHANGELOG.md          # Version history and release notes
└── requirements.txt      # Runtime dependencies
```

**Metadata:**
- **Author**: SuperGemini Organization
- **License**: MIT License
- **Python Requires**: >=3.8
- **Classifiers**: Development Status :: 5 - Production/Stable
- **Keywords**: gemini, ai, development, automation, mcp, agents

## 🔧 Available Scripts

**Publishing Scripts:**

**scripts/validate_pypi_ready.py**
```bash
# Comprehensive pre-publication validation
python scripts/validate_pypi_ready.py

# Validates:
# - Package structure and metadata
# - Version consistency across files
# - Dependency compatibility
# - Entry point functionality
# - Security scanning results
# - Cross-platform compatibility
```

**scripts/build_package.py**
```bash
# Clean build process with validation
python scripts/build_package.py

# Features:
# - Clean previous builds
# - Generate wheel and source distributions
# - Validate package contents
# - Test installation locally
```

**scripts/test_installation.py**
```bash
# Test package installation in clean environment
python scripts/test_installation.py

# Tests:
# - Fresh virtual environment installation
# - Entry point functionality
# - Core component functionality
# - Dependency resolution
```

**Manual Commands:**
```bash
# Build package manually
python -m build

# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Upload to PyPI (production)
twine upload dist/*

# Clean build artifacts
rm -rf build/ dist/ *.egg-info/
```

**GitHub Actions Integration:**
- **Automated Testing**: Multi-platform validation on pull requests
- **Release Workflow**: Triggered by git tag creation
- **Security Scanning**: Dependency and code security validation
- **Cross-Platform Testing**: Linux, macOS, Windows compatibility verification

## 🤖 GitHub Actions Automation

**GitHub Actions Workflows:**

**.github/workflows/test.yml** (Pull Request Testing)
```yaml
# Triggered on: Pull requests, pushes to main
# Tests: Python 3.8-3.12, Linux/macOS/Windows
# Steps: Linting, testing, coverage, security scanning
```

**.github/workflows/publish.yml** (Release Publishing)
```yaml
# Triggered on: Git tag creation (v*.*.*)
# Steps:
# 1. Multi-platform testing
# 2. Security validation
# 3. Package building
# 4. PyPI publication
# 5. GitHub release creation
```

**Required GitHub Secrets:**
- **PYPI_API_TOKEN**: PyPI API token for package publishing
- **CODECOV_TOKEN**: Code coverage reporting integration
- **GPG_PRIVATE_KEY**: Optional GPG signing for releases

**Workflow Configuration:**
```bash
# Release workflow trigger
git tag v4.0.1
git push origin v4.0.1

# GitHub Actions automatically:
# - Runs comprehensive test suite
# - Validates package integrity
# - Publishes to PyPI
# - Creates GitHub release with changelog
```

**Manual Workflow Triggers:**
- **Repository Dispatch**: Manual workflow triggering for emergency releases
- **Workflow Dispatch**: Manual testing and validation workflows
- **Schedule**: Nightly dependency security scanning

**Status Checks:**
- **Required Checks**: All tests pass, security scan clean, coverage threshold met
- **Branch Protection**: Main branch protected with required status checks
- **Deployment Protection**: Production deployment requires maintainer approval

## 📈 Version Management

**Version Scheme (Semantic Versioning):**

**Format**: MAJOR.MINOR.PATCH (e.g., 4.0.0)
- **MAJOR**: Breaking changes, architectural updates, incompatible API changes
- **MINOR**: New features, agent additions, MCP server integrations, backward-compatible changes
- **PATCH**: Bug fixes, documentation updates, security patches, backward-compatible fixes

**Current Version**: 4.0.0
- Major architectural update with enhanced agent coordination
- 6 MCP server integrations and 13 specialized agents
- Comprehensive command system with 21 slash commands

**Version Update Process:**

**1. Version Planning:**
```bash
# Review changes since last release
git log v3.5.0..HEAD --oneline

# Determine version increment based on changes
# Breaking changes → MAJOR
# New features → MINOR  
# Bug fixes only → PATCH
```

**2. Version Updates:**
```bash
# Update version in multiple files:
# - superclaude/__init__.py
# - setup.py
# - pyproject.toml
# - CHANGELOG.md

# Validate version consistency
python scripts/validate_pypi_ready.py
```

**3. Release Creation:**
```bash
# Create and push git tag
git tag -a v4.0.1 -m "Release v4.0.1: Bug fixes and stability improvements"
git push origin v4.0.1

# GitHub Actions handles automated publishing
```

**Pre-release Versions:**
- **Alpha**: 4.1.0a1 (early development, unstable)
- **Beta**: 4.1.0b1 (feature complete, testing phase)
- **Release Candidate**: 4.1.0rc1 (production candidate, final testing)
**Version Validation Checklist:**

**Pre-Release Validation:**
```bash
# 1. Version consistency check
python scripts/validate_pypi_ready.py

# 2. Verify version in all files matches
grep -r "4\.0\.0" superclaude/ setup.py pyproject.toml

# 3. Changelog validation
# Ensure CHANGELOG.md includes version with release date and changes

# 4. Dependency validation
pip-compile requirements.in
safety check
```

**Git Tagging Workflow:**
```bash
# 1. Ensure clean working directory
git status
git pull origin main

# 2. Create annotated tag with release notes
git tag -a v4.0.1 -m "Release v4.0.1

Bug Fixes:
- Fixed MCP server connection timeout
- Resolved agent coordination race condition

Improvements:
- Enhanced error messaging for command validation
- Updated documentation for best practices"

# 3. Push tag to trigger release
git push origin v4.0.1
```

**Tag Validation:**
```bash
# Verify tag creation
git tag -l "v4.0.*"
git show v4.0.1

# Verify tag signature (if GPG signing enabled)
git tag -v v4.0.1
```

**Automated Validation:**
- **GitHub Actions**: Triggered automatically on tag push
- **Tests**: Full test suite across multiple Python versions and platforms
- **Security**: Dependency scanning and vulnerability assessment
- **Package**: Build validation and installation testing

## 🔍 Package Structure

**PyPI Package Structure:**

**Source Distribution Contents:**
```
SuperGemini-4.0.0.tar.gz
├── superclaude/
│   ├── __init__.py                 # Version and package metadata
│   ├── cli.py                      # Main CLI entry point
│   ├── core/
│   │   ├── __init__.py
│   │   ├── agent_manager.py        # Agent coordination logic
│   │   ├── command_parser.py       # Command parsing and routing
│   │   └── session_manager.py      # Session persistence
│   ├── setup/
│   │   ├── __init__.py
│   │   ├── installer.py            # Component installation
│   │   ├── components/             # Component definitions
│   │   └── validators.py           # Installation validation
│   └── utils/
│       ├── __init__.py
│       ├── file_utils.py           # File system utilities
│       └── logging_utils.py        # Logging configuration
├── setup.py                        # Package setup configuration
├── pyproject.toml                  # Modern packaging configuration
├── README.md                       # PyPI package description
├── LICENSE                         # MIT license text
├── CHANGELOG.md                    # Version history
├── requirements.txt                # Runtime dependencies
└── PKG-INFO                        # Package metadata
```

**Wheel Distribution:**
```
SuperGemini-4.0.0-py3-none-any.whl
├── superclaude/                    # Compiled package code
├── SuperGemini-4.0.0.dist-info/   # Package metadata
│   ├── METADATA                    # Package description and requirements
│   ├── WHEEL                       # Wheel format metadata
│   ├── entry_points.txt            # CLI entry points
│   └── LICENSE                     # License information
```

**Entry Points Configuration:**
```ini
[console_scripts]
SuperGemini = superclaude.cli:main
superclaude = superclaude.cli:main
```

**Package Dependencies:**
- **Runtime**: Minimal dependencies for broad compatibility
- **Development**: Extended toolchain for contributors
- **Optional**: MCP server dependencies installed as needed

## 🧪 Testing

**Local Testing Procedures:**

**Package Build Testing:**
```bash
# 1. Clean environment setup
rm -rf build/ dist/ *.egg-info/
python -m venv test_env
source test_env/bin/activate

# 2. Build package
python -m build

# 3. Validate package contents
twine check dist/*
tar -tzf dist/SuperGemini-*.tar.gz | head -20

# 4. Local installation test
pip install dist/SuperGemini-*.whl
SuperGemini --version
SuperGemini install --dry-run
```

**TestPyPI Testing (Maintainers):**
```bash
# 1. Upload to TestPyPI
twine upload --repository testpypi dist/*

# 2. Test installation from TestPyPI
pip install --index-url https://test.pypi.org/simple/ SuperGemini

# 3. Functional testing
SuperGemini install --list-components
SuperGemini --help

# 4. Clean up test environment
pip uninstall SuperGemini
```

**Cross-Platform Testing:**
```bash
# Docker-based testing for Linux environments
docker run -v $(pwd):/app python:3.9 /bin/bash -c "
  cd /app && 
  pip install dist/SuperGemini-*.whl && 
  SuperGemini --version
"

# Virtual machine testing for Windows/macOS
# Manual testing on target platforms
```

**Integration Testing:**
```bash
# Test with real Gemini Code environment
gemini --version
SuperGemini install --components core
# Verify slash commands work: SuperGemini help
```

## 🚨 Troubleshooting

**Common Publishing Issues:**

**Build Failures:**
```bash
# Issue: "No module named 'setuptools'"
# Solution: Update setuptools
pip install --upgrade setuptools wheel

# Issue: "error: Microsoft Visual C++ 14.0 is required"
# Solution: Install Visual Studio Build Tools (Windows)
# Or use wheel distribution instead of source

# Issue: "Permission denied" during build
# Solution: Check file permissions and virtual environment
chmod -R u+w build/ dist/
```

**Upload Failures:**
```bash
# Issue: "403 Forbidden" during upload
# Solution: Verify API token and package permissions
twine upload --username __token__ --password pypi-... dist/*

# Issue: "Package already exists"
# Solution: Version already published, increment version
# Check: https://pypi.org/project/SuperGemini/

# Issue: "File already exists"
# Solution: Clean dist/ directory and rebuild
rm -rf dist/ && python -m build
```

**Installation Issues:**
```bash
# Issue: "No matching distribution found"
# Solution: Check Python version compatibility
python --version  # Must be 3.8+

# Issue: "Command 'SuperGemini' not found"
# Solution: Check PATH and entry points
pip show -f SuperGemini | grep console_scripts
which SuperGemini
```

**GitHub Actions Failures:**
```bash
# Issue: "PYPI_API_TOKEN not found"
# Solution: Configure repository secrets
# GitHub Settings → Secrets → Add PYPI_API_TOKEN

# Issue: "Tag validation failed"
# Solution: Ensure tag follows semver pattern
git tag -d v4.0.0 && git tag v4.0.0
```
**Publishing Support Resources:**

**Documentation:**
- [Python Packaging Guide](https://packaging.python.org/) - Official Python packaging documentation
- [PyPI Help](https://pypi.org/help/) - PyPI-specific guidance and troubleshooting
- [Twine Documentation](https://twine.readthedocs.io/) - Secure package uploading
- [GitHub Actions Documentation](https://docs.github.com/en/actions) - CI/CD automation

**SuperGemini-Specific Support:**
- **GitHub Issues**: https://github.com/SuperGemini-Org/SuperGemini_Framework/issues
- **Maintainer Contact**: For urgent publishing issues
- **Community Discussions**: General publishing questions and experiences
- **Documentation**: [Contributing Guide](CONTRIBUTING.md) for development setup

**Emergency Publishing:**
For critical security patches or urgent fixes:
- Contact maintainers directly for expedited review
- Use emergency publishing workflow with manual approval
- Follow security advisory process for vulnerability patches

**Community Resources:**
- **Python Packaging Discord**: Real-time help with packaging issues
- **PyPA GitHub**: Python Packaging Authority resources and discussions  
- **Stack Overflow**: Tag questions with 'python-packaging' and 'pypi'
- **Reddit r/Python**: Community discussion and troubleshooting

**Professional Support:**
For organizations requiring dedicated packaging support:
- Custom CI/CD pipeline development
- Enterprise PyPI mirror setup
- Private package repository configuration
- Compliance and security validation automation

## 📊 Publication Checklist

**Pre-Publication Checklist:**

**Code Quality:**
- [ ] All tests pass locally and in CI
- [ ] Code coverage meets minimum threshold (>90%)
- [ ] Linting and formatting checks pass (black, flake8, mypy)
- [ ] Security scanning clean (bandit, safety)
- [ ] No critical TODO items or debugging code

**Package Validation:**
- [ ] Version updated in all relevant files (\_\_init\_\_.py, setup.py, pyproject.toml)
- [ ] CHANGELOG.md updated with release notes and date
- [ ] Package builds successfully (`python -m build`)
- [ ] Package contents validated (`twine check dist/*`)
- [ ] Entry points functional (`SuperGemini --version`)

**Documentation:**
- [ ] README.md updated with new features and changes
- [ ] API documentation reflects current functionality
- [ ] Installation instructions tested and accurate
- [ ] Breaking changes clearly documented with migration guide

**Testing:**
- [ ] Local installation test successful
- [ ] TestPyPI upload and installation successful
- [ ] Cross-platform compatibility verified (Linux, macOS, Windows)
- [ ] Integration testing with Gemini Code environment
- [ ] MCP server integrations functional

**Security:**
- [ ] Dependency vulnerabilities resolved
- [ ] API tokens and secrets properly configured
- [ ] No sensitive information in package or repository
- [ ] GPG signatures enabled for release tags (if applicable)

**Release Management:**
- [ ] Git tag created with proper semantic version
- [ ] GitHub Actions workflow configured and tested
- [ ] Release notes prepared for GitHub release
- [ ] Community notification plan prepared

## 🎯 Production Publishing

**Production Publishing Options:**

**Option 1: Automated GitHub Actions (Recommended)**
```bash
# Create release tag
git tag -a v4.0.1 -m "Release v4.0.1: Bug fixes and improvements"
git push origin v4.0.1

# GitHub Actions automatically:
# 1. Runs full test suite
# 2. Validates package integrity  
# 3. Publishes to PyPI
# 4. Creates GitHub release
```

**Option 2: Manual Publishing (Emergency Only)**
```bash
# 1. Validate and build
python scripts/validate_pypi_ready.py
python -m build

# 2. Upload to PyPI
twine upload dist/*

# 3. Create GitHub release manually
gh release create v4.0.1 --title "v4.0.1" --notes-file CHANGELOG.md
```

**Recommended Workflow:**

**1. Pre-Release (Development)**
- Feature development with comprehensive testing
- Version planning and changelog preparation
- TestPyPI validation for complex changes

**2. Release Preparation**
- Final version update and validation
- Documentation review and updates
- Security scanning and dependency audit

**3. Production Release**
- Git tag creation triggers automated workflow
- Monitoring of GitHub Actions progress
- Verification of PyPI publication success

**4. Post-Release**
- GitHub release creation with changelog
- Community notification (social media, forums)
- Documentation updates and link validation

**Release Cadence:**
- **Major Releases**: Quarterly (significant features, breaking changes)
- **Minor Releases**: Monthly (new features, agents, MCP servers)
- **Patch Releases**: As needed (bug fixes, security patches)
- **Hotfixes**: Emergency releases for critical issues

## 🔐 Security Best Practices

**API Token Security:**

**Token Management:**
- Use package-scoped tokens (not account-wide) for PyPI publishing
- Rotate tokens quarterly or after any security incident
- Store tokens only in GitHub repository secrets, never in code
- Enable two-factor authentication on PyPI account

**GitHub Secrets Configuration:**
```bash
# Required secrets for automated publishing:
PYPI_API_TOKEN          # PyPI publishing token (scoped to SuperGemini)
CODECOV_TOKEN          # Code coverage reporting
GPG_PRIVATE_KEY        # Optional: GPG signing for releases
GPG_PASSPHRASE         # Optional: GPG key passphrase
```

**Token Scope Configuration:**
- **Project Scope**: Limited to SuperGemini package only
- **Permission Level**: Upload permissions only (not management)
- **Expiration**: Set reasonable expiration dates (1 year maximum)
- **Audit Trail**: Regular review of token usage and access logs

**Credential Protection:**
```bash
# Never store credentials in:
# - Source code or configuration files
# - Shell history or scripts
# - Documentation or comments
# - Temporary files or logs

# Use secure storage:
# - GitHub repository secrets
# - Environment variables (local development)
# - Secure credential managers (keyring, etc.)
```

**Security Monitoring:**
- Enable PyPI security notifications for package changes
- Monitor GitHub Actions logs for credential usage
- Regular audit of repository access and collaborator permissions
- Automated alerts for unauthorized publishing attempts

**Incident Response:**
- Immediately revoke compromised tokens
- Generate new tokens with updated scope
- Review recent package releases for unauthorized changes
- Notify community of security incidents affecting package integrity

## 📝 Post-Publication

**Post-Publication Tasks:**

**Immediate Verification (Within 1 hour):**
```bash
# 1. Verify PyPI publication
curl -s https://pypi.org/pypi/SuperGemini/json | jq '.info.version'

# 2. Test installation from PyPI
pip install SuperGemini==4.0.1
SuperGemini --version

# 3. Verify entry points functional
SuperGemini install --list-components
```

**GitHub Release Management:**
```bash
# 1. GitHub release created automatically by Actions
# 2. Verify release notes and changelog accuracy
# 3. Upload additional assets if needed (documentation, etc.)
# 4. Pin release for major versions

# Manual release creation (if automated fails):
gh release create v4.0.1 \
  --title "SuperGemini v4.0.1" \
  --notes-file CHANGELOG.md \
  --latest
```

**Community Notification:**
- **GitHub Discussions**: Announce release with highlights and breaking changes
- **Social Media**: Share release announcement with key features
- **Documentation**: Update installation guides with new version numbers
- **Issue Tracking**: Close resolved issues and update project boards

**Documentation Updates:**
- Verify documentation links work with new version
- Update version references in installation guides
- Refresh example commands and outputs
- Update compatibility matrices and requirements

**Monitoring and Support:**
- Monitor GitHub issues for installation problems
- Watch PyPI download statistics and user feedback
- Respond to community questions about new features
- Track adoption and usage patterns for future development

**Release Follow-up (Within 1 week):**
- Analyze download statistics and adoption metrics
- Collect community feedback and feature requests
- Plan next release cycle based on feedback and roadmap
- Update project roadmap and documentation priorities

---

**Publishing Support Contacts:**

**Primary Maintainers:**
- **GitHub**: @SuperGemini-Org maintainer team
- **Issues**: https://github.com/SuperGemini-Org/SuperGemini_Framework/issues
- **Email**: maintainers@superclaude.org (for urgent publishing issues)

**Specific Support Areas:**

**PyPI Publishing Issues:**
- GitHub Issues with `publishing` label
- Include: version, platform, error messages, steps to reproduce
- Response time: 24-48 hours for critical publishing failures

**GitHub Actions / CI/CD:**
- Workflow failures and automation issues
- Repository configuration and secrets management
- Cross-platform testing and validation problems

**Package Distribution:**
- Installation failures and dependency conflicts
- Entry point and command-line interface issues
- Cross-platform compatibility problems

**Security-Related Publishing:**
- Security token management and rotation
- Vulnerability disclosure and patch releases
- Secure publishing workflow configuration

**Emergency Contacts:**
For critical security patches or urgent publishing needs:
- **Security**: security@superclaude.org
- **Direct**: Maintainer contact information provided upon first contact
- **Priority**: Use `urgent` label on GitHub issues for expedited response

**Self-Service Resources:**
Before contacting support:
1. Review this publishing guide thoroughly
2. Check [Troubleshooting](Reference/troubleshooting.md) documentation
3. Search existing GitHub issues for similar problems
4. Test with latest versions and clean environments