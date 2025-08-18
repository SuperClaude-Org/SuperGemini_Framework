import setuptools
import sys
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_version():
    """Get version from VERSION file with proper error handling."""
    try:
        with open("VERSION", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        logger.warning("VERSION file not found, using fallback version")
        return "4.0.4"
    except Exception as e:
        logger.error(f"Error reading VERSION file: {e}")
        return "4.0.4"

def get_long_description():
    """Get long description from README with error handling."""
    try:
        with open("README.md", "r", encoding="utf-8") as fh:
            return fh.read()
    except FileNotFoundError:
        logger.warning("README.md not found")
        return "SuperGemini Framework Management Hub"
    except Exception as e:
        logger.error(f"Error reading README.md: {e}")
        return "SuperGemini Framework Management Hub"

def get_install_requires():
    """Get install requirements with proper dependency management."""
    base_requires = ["setuptools>=45.0.0"]
    
    # Add Python version-specific dependencies
    if sys.version_info < (3, 8):
        base_requires.append("importlib-metadata>=1.0.0")
    
    # Add other dependencies your project needs
    # base_requires.extend([
    #     "requests>=2.25.0",
    #     "click>=7.0",
    #     # etc.
    # ])
    
    return base_requires

# Main setup configuration
setuptools.setup(
    name="SuperGemini",
    version=get_version(),
    author="hyunjae lim, NomenAK, Mithun Gowda B",
    author_email="thecurrent.lim@gmail.com",
    description="SuperGemini Framework Management Hub",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/SuperClaude-Org/SuperGemini_Framework",
    packages=setuptools.find_packages() + setuptools.find_packages(where=".", include=["setup*"]),
    include_package_data=True,
    install_requires=get_install_requires(),
    entry_points={
        "console_scripts": [
            "SuperGemini=SuperGemini.__main__:main",
            "supergemini=SuperGemini.__main__:main",
            "sg=SuperGemini.__main__:main",
        ],
    },
    python_requires=">=3.8",
    project_urls={
        "GitHub": "https://github.com/SuperClaude-Org/SuperGemini_Framework",
        "Bug Tracker": "https://github.com/SuperClaude-Org/SuperGemini_Framework/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
    ],
        )
