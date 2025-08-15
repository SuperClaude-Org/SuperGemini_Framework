#!/bin/bash
"""
SuperClaude PyPI Publishing Helper Script
Easy-to-use wrapper for the Python build and upload script
"""

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
BUILD_SCRIPT="$SCRIPT_DIR/build_and_upload.py"

echo -e "${BLUE}🚀 SuperClaude PyPI Publishing Helper${NC}"
echo -e "📁 Project root: $PROJECT_ROOT"

# Function to show usage
show_usage() {
    echo -e "${YELLOW}Usage:${NC}"
    echo "  $0 test       - Build and upload to TestPyPI"
    echo "  $0 test-install - Test installation from TestPyPI"
    echo "  $0 prod       - Build and upload to production PyPI"
    echo "  $0 build      - Only build the package"
    echo "  $0 clean      - Clean build artifacts"
    echo "  $0 check      - Validate project structure only"
    echo ""
    echo -e "${YELLOW}Examples:${NC}"
    echo "  $0 test                    # Upload to TestPyPI"
    echo "  $0 test && $0 test-install # Upload and test"
    echo "  $0 prod                    # Upload to production"
}

# Check if Python script exists
if [ ! -f "$BUILD_SCRIPT" ]; then
    echo -e "${RED}❌ Build script not found: $BUILD_SCRIPT${NC}"
    exit 1
fi

# Parse command
case "${1:-}" in
    "test")
        echo -e "${YELLOW}📦 Building and uploading to TestPyPI...${NC}"
        python3 "$BUILD_SCRIPT" --testpypi
        echo -e "${GREEN}✅ Uploaded to TestPyPI! Test with:${NC}"
        echo -e "   pip install --index-url https://test.pypi.org/simple/ SuperClaude"
        ;;
    
    "test-install")
        echo -e "${YELLOW}🧪 Testing installation from TestPyPI...${NC}"
        python3 "$BUILD_SCRIPT" --testpypi --test-install --skip-build
        ;;
    
    "prod"|"production")
        echo -e "${YELLOW}🚨 Building and uploading to PRODUCTION PyPI...${NC}"
        echo -e "${RED}⚠️  This cannot be undone!${NC}"
        python3 "$BUILD_SCRIPT"
        echo -e "${GREEN}✅ Uploaded to PyPI! Install with:${NC}"
        echo -e "   pip install SuperClaude"
        ;;
    
    "build")
        echo -e "${YELLOW}🔨 Building package only...${NC}"
        python3 "$BUILD_SCRIPT" --skip-validation --testpypi --skip-upload
        echo -e "${GREEN}✅ Package built in dist/ directory${NC}"
        ;;
    
    "clean")
        echo -e "${YELLOW}🧹 Cleaning build artifacts...${NC}"
        python3 "$BUILD_SCRIPT" --clean
        echo -e "${GREEN}✅ Build artifacts cleaned${NC}"
        ;;
    
    "check"|"validate")
        echo -e "${YELLOW}🔍 Validating project structure...${NC}"
        python3 "$BUILD_SCRIPT" --skip-build --testpypi
        ;;
    
    "help"|"-h"|"--help"|"")
        show_usage
        ;;
    
    *)
        echo -e "${RED}❌ Unknown command: $1${NC}"
        echo ""
        show_usage
        exit 1
        ;;
esac