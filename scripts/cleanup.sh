#!/bin/bash
# SuperClaude Project Cleanup Script
# Removes build artifacts, cache files, and temporary files

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

echo -e "${BLUE}🧹 SuperClaude Project Cleanup${NC}"
echo -e "📁 Project root: $PROJECT_ROOT"

cd "$PROJECT_ROOT"

# Function to safely remove files/directories
safe_remove() {
    local target="$1"
    local description="$2"
    
    if [ -e "$target" ]; then
        rm -rf "$target"
        echo -e "${GREEN}✅ Removed $description${NC}"
    else
        echo -e "${YELLOW}ℹ️  $description not found (already clean)${NC}"
    fi
}

echo -e "\n${YELLOW}🗑️  Removing Python cache files...${NC}"
find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
find . -name "*.pyc" -type f -delete 2>/dev/null || true
find . -name "*.pyo" -type f -delete 2>/dev/null || true
find . -name "*.pyd" -type f -delete 2>/dev/null || true
echo -e "${GREEN}✅ Python cache files cleaned${NC}"

echo -e "\n${YELLOW}📦 Removing build artifacts...${NC}"
safe_remove "build/" "Build directory"
safe_remove "dist/" "Distribution directory" 
safe_remove "*.egg-info" "Egg-info directories"
safe_remove ".eggs/" "Eggs directory"
safe_remove "wheels/" "Wheels directory"
safe_remove "pip-wheel-metadata/" "Pip wheel metadata"

echo -e "\n${YELLOW}🧪 Removing test artifacts...${NC}"
safe_remove ".pytest_cache/" "Pytest cache"
safe_remove ".tox/" "Tox directory"
safe_remove ".nox/" "Nox directory"
safe_remove "htmlcov/" "HTML coverage reports"
safe_remove ".coverage" "Coverage data file"
safe_remove "coverage.xml" "Coverage XML report"
safe_remove ".hypothesis/" "Hypothesis directory"

echo -e "\n${YELLOW}🔧 Removing development tool cache...${NC}"
safe_remove ".mypy_cache/" "MyPy cache"
safe_remove ".ruff_cache/" "Ruff cache"
safe_remove ".black/" "Black cache"

echo -e "\n${YELLOW}🗄️  Removing temporary files...${NC}"
find . -name "*.tmp" -type f -delete 2>/dev/null || true
find . -name "*.temp" -type f -delete 2>/dev/null || true
find . -name "*~" -type f -delete 2>/dev/null || true
find . -name "*.bak" -type f -delete 2>/dev/null || true
find . -name "*.backup" -type f -delete 2>/dev/null || true
echo -e "${GREEN}✅ Temporary files cleaned${NC}"

echo -e "\n${YELLOW}📋 Removing PyPI publishing artifacts...${NC}"
safe_remove "twine.log" "Twine log file"
safe_remove ".twine/" "Twine directory"
safe_remove "PYPI_SETUP_COMPLETE.md" "Setup completion file"

echo -e "\n${YELLOW}🧽 Removing OS-specific files...${NC}"
find . -name ".DS_Store" -type f -delete 2>/dev/null || true
find . -name "._*" -type f -delete 2>/dev/null || true
find . -name "Thumbs.db" -type f -delete 2>/dev/null || true
find . -name "Desktop.ini" -type f -delete 2>/dev/null || true
echo -e "${GREEN}✅ OS-specific files cleaned${NC}"

echo -e "\n${GREEN}🎉 Cleanup completed successfully!${NC}"
echo -e "${BLUE}📊 Project is clean and ready for development or publishing${NC}"

# Show summary
echo -e "\n${BLUE}📈 Summary:${NC}"
echo -e "  • Python cache files: Removed"
echo -e "  • Build artifacts: Cleaned"
echo -e "  • Test artifacts: Removed" 
echo -e "  • Development tool cache: Cleared"
echo -e "  • Temporary files: Deleted"
echo -e "  • PyPI artifacts: Cleaned"
echo -e "  • OS-specific files: Removed"

echo -e "\n${YELLOW}💡 Next steps:${NC}"
echo -e "  • Run validation: ${BLUE}python3 scripts/validate_pypi_ready.py${NC}"
echo -e "  • Test build: ${BLUE}./scripts/publish.sh build${NC}"
echo -e "  • Check git status: ${BLUE}git status${NC}"