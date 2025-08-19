# Diagnostic Reference Guide

**Advanced Diagnostics Focus**: This guide provides comprehensive diagnostic procedures for performance monitoring, session management, and system-level troubleshooting. Use these procedures for complex issues that require deep analysis and systematic investigation.

**Systematic Investigation**: Each diagnostic section includes monitoring tools, analysis procedures, and optimization strategies to identify root causes and implement effective solutions.

## Performance Monitoring and Analysis

### System Resource Diagnostics

**Comprehensive Performance Monitoring:**
```bash
# Complete system resource analysis
echo "=== SuperGemini Performance Diagnostics ==="

# CPU usage analysis
echo "=== CPU Usage ==="
top -b -n 1 | head -10
ps aux --sort=-%cpu | head -10

# Memory usage analysis
echo "=== Memory Usage ==="
free -h
ps aux --sort=-%mem | head -10

# Disk I/O analysis
echo "=== Disk I/O ==="
iostat -x 1 3
df -h

# Network analysis (if MCP servers used)
echo "=== Network Status ==="
netstat -i
ss -tuln | grep -E ":8000|:8001|:8002"

# Process analysis
echo "=== SuperGemini Processes ==="
ps aux | grep -E "python.*SuperGemini|node.*mcp|gemini"
```

**Real-time Performance Monitoring:**
```bash
# Continuous monitoring setup
echo "=== Setting up continuous monitoring ==="

# Install monitoring tools if needed
# Ubuntu/Debian: sudo apt install htop iotop nethogs
# CentOS/RHEL: sudo yum install htop iotop nethogs
# macOS: brew install htop

# Real-time monitoring commands
echo "Use these commands for real-time monitoring:"
echo "htop              # Interactive process monitor"
echo "iotop             # I/O usage by process"
echo "nethogs           # Network usage by process"
echo "watch free -h     # Memory usage updates"
echo "watch df -h       # Disk space updates"

# Performance baseline establishment
echo "=== Establishing performance baselines ==="
time python3 -m SuperGemini --version
time ls ~/.gemini/
time cat ~/.gemini/GEMINI.md | wc -l
```

**Performance Bottleneck Identification:**
```bash
# Systematic bottleneck analysis
echo "=== Bottleneck Analysis ==="

# CPU bottleneck detection
echo "CPU Analysis:"
top -b -n 1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1
if [ $(top -b -n 1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1 | cut -d'.' -f1) -gt 80 ]; then
    echo "⚠️ High CPU usage detected"
    echo "Solutions: Reduce operation scope, use --scope flags"
fi

# Memory bottleneck detection
echo "Memory Analysis:"
MEM_USAGE=$(free | grep Mem | awk '{printf "%.0f", $3/$2 * 100}')
if [ $MEM_USAGE -gt 85 ]; then
    echo "⚠️ High memory usage: ${MEM_USAGE}%"
    echo "Solutions: Clear sessions, restart Gemini CLI"
fi

# Disk I/O bottleneck detection
echo "Disk I/O Analysis:"
iostat -x 1 1 | tail -n +4 | awk '$10 > 80 {print "⚠️ High I/O on " $1 ": " $10 "% utilization"}'

# Network bottleneck detection (for MCP servers)
echo "Network Analysis:"
ping -c 3 8.8.8.8 | tail -1 | awk -F'/' '{if($5 > 100) print "⚠️ High network latency: " $5 "ms"}'
```

### Performance Optimization Strategies

**CPU Optimization:**
```bash
# CPU usage optimization
echo "=== CPU Optimization Strategies ==="

# Identify CPU-intensive processes
ps aux --sort=-%cpu | grep -E "python.*SuperGemini|node.*mcp" | head -5

# Optimization solutions
echo "CPU Optimization Actions:"
echo "1. Use scope limiting: --scope file instead of --scope project"
echo "2. Break complex tasks into smaller operations"
echo "3. Use selective MCP servers: --c7 --seq instead of --all-mcp"
echo "4. Restart Gemini CLI session to clear accumulated processes"

# CPU monitoring during operations
echo "Monitor CPU during operations:"
echo "watch 'ps aux --sort=-%cpu | head -10'"
```

**Memory Optimization:**
```bash
# Memory usage optimization
echo "=== Memory Optimization Strategies ==="

# Memory analysis
echo "Current memory status:"
free -h
echo ""
echo "Process memory usage:"
ps aux --sort=-%mem | head -10

# Session memory cleanup
echo "Session cleanup commands:"
echo "rm -rf ~/.gemini/sessions/old-*     # Remove old sessions"
echo "rm -rf ~/.gemini/temp/              # Clear temporary files"
echo "rm -rf /tmp/superclaude-*           # Clear system temp files"

# Memory monitoring
echo "Memory monitoring:"
echo "watch 'free -h && echo && ps aux --sort=-%mem | head -5'"
```

**Disk I/O Optimization:**
```bash
# Disk I/O optimization
echo "=== Disk I/O Optimization ==="

# Disk usage analysis
du -sh ~/.gemini/
du -sh ~/.gemini/sessions/ 2>/dev/null || echo "No sessions directory"
df -h ~/.gemini/

# I/O optimization actions
echo "I/O Optimization Actions:"
echo "1. Focus on specific files instead of entire projects"
echo "2. Use faster storage (SSD) for ~/.gemini directory"
echo "3. Regular cleanup of session files"
echo "4. Move large projects to faster storage"

# I/O monitoring
echo "Monitor I/O usage:"
echo "iotop -o -d 1  # Show processes doing I/O"
```

## Session Management Diagnostics

### Session Lifecycle Analysis

**Session State Diagnosis:**
```bash
# Complete session state analysis
echo "=== Session State Diagnostics ==="

# Session directory analysis
echo "Session Directory Analysis:"
ls -la ~/.gemini/sessions/ 2>/dev/null || echo "No sessions directory found"
du -sh ~/.gemini/sessions/ 2>/dev/null || echo "No sessions to analyze"

# Session file integrity check
echo "Session File Integrity:"
find ~/.gemini/sessions/ -name "*.json" -type f 2>/dev/null | while read file; do
    if python3 -c "import json; json.load(open('$file'))" 2>/dev/null; then
        echo "✅ Valid: $(basename $file)"
    else
        echo "❌ Corrupted: $(basename $file)"
    fi
done

# Session memory usage analysis
echo "Session Memory Usage:"
find ~/.gemini/sessions/ -name "*.json" -type f -exec du -h {} \; 2>/dev/null | sort -hr | head -10
```

**Session Performance Analysis:**
```bash
# Session performance diagnostics
echo "=== Session Performance Analysis ==="

# Session load time testing
echo "Session Load Performance:"
time ls ~/.gemini/sessions/ >/dev/null 2>&1

# Session access pattern analysis
echo "Session Access Patterns:"
find ~/.gemini/sessions/ -type f -printf "%T@ %p\n" 2>/dev/null | sort -n | tail -10 | while read timestamp file; do
    date -d @${timestamp} "+%Y-%m-%d %H:%M:%S"
    basename "$file"
    echo "---"
done

# Session storage efficiency
echo "Session Storage Efficiency:"
total_sessions=$(find ~/.gemini/sessions/ -name "*.json" 2>/dev/null | wc -l)
total_size=$(du -sb ~/.gemini/sessions/ 2>/dev/null | cut -f1)
if [ "$total_sessions" -gt 0 ] && [ "$total_size" -gt 0 ]; then
    avg_size=$((total_size / total_sessions))
    echo "Total sessions: $total_sessions"
    echo "Total size: $(echo $total_size | awk '{print $1/1024/1024 "MB"}')"
    echo "Average session size: $(echo $avg_size | awk '{print $1/1024 "KB"}')"
fi
```

### Session Recovery Procedures

**Session Corruption Recovery:**
```bash
# Session corruption diagnosis and recovery
echo "=== Session Corruption Recovery ==="

# Identify corrupted sessions
echo "Identifying corrupted sessions:"
find ~/.gemini/sessions/ -name "*.json" -type f 2>/dev/null | while read file; do
    if ! python3 -c "import json; json.load(open('$file'))" 2>/dev/null; then
        echo "Corrupted: $file"
        mv "$file" "$file.corrupted.$(date +%s)"
        echo "Backed up to: $file.corrupted.$(date +%s)"
    fi
done

# Session backup creation
echo "Creating session backups:"
if [ -d ~/.gemini/sessions/ ]; then
    backup_dir=~/.gemini/sessions.backup.$(date +%Y%m%d_%H%M%S)
    cp -r ~/.gemini/sessions/ "$backup_dir"
    echo "Sessions backed up to: $backup_dir"
fi

# Session validation procedure
echo "Session validation procedure:"
cat << 'EOF' > /tmp/validate_session.py
import json
import sys
import os

def validate_session(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        # Basic structure validation
        required_keys = ['timestamp', 'context']
        for key in required_keys:
            if key not in data:
                return False, f"Missing key: {key}"
        
        return True, "Valid session"
    except json.JSONDecodeError as e:
        return False, f"JSON error: {e}"
    except Exception as e:
        return False, f"Error: {e}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_session.py <session_file>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    is_valid, message = validate_session(filepath)
    print(f"{'✅' if is_valid else '❌'} {filepath}: {message}")
EOF

find ~/.gemini/sessions/ -name "*.json" -type f 2>/dev/null | while read file; do
    python3 /tmp/validate_session.py "$file"
done

rm /tmp/validate_session.py
```

**Session Optimization Procedures:**
```bash
# Session optimization and cleanup
echo "=== Session Optimization ==="

# Archive old sessions
echo "Archiving old sessions (>30 days):"
find ~/.gemini/sessions/ -name "*.json" -type f -mtime +30 2>/dev/null | while read file; do
    archive_dir=~/.gemini/sessions.archive/$(date +%Y-%m)
    mkdir -p "$archive_dir"
    mv "$file" "$archive_dir/"
    echo "Archived: $(basename $file)"
done

# Compress large sessions
echo "Compressing large sessions (>1MB):"
find ~/.gemini/sessions/ -name "*.json" -type f -size +1M 2>/dev/null | while read file; do
    gzip "$file"
    echo "Compressed: $(basename $file).gz"
done

# Session defragmentation
echo "Session defragmentation:"
if [ -d ~/.gemini/sessions/ ]; then
    # Sort sessions by access time and reorganize
    temp_dir=$(mktemp -d)
    find ~/.gemini/sessions/ -name "*.json" -type f -printf "%A@ %p\n" 2>/dev/null | sort -n | while read atime file; do
        cp "$file" "$temp_dir/$(basename $file)"
    done
    echo "Sessions reorganized in: $temp_dir"
    echo "Replace sessions directory with: mv $temp_dir ~/.gemini/sessions.optimized"
fi
```

## Advanced System Diagnostics

### Comprehensive Health Assessment

**System-Wide Health Check:**
```bash
# Complete SuperGemini system health assessment
echo "=== SuperGemini System Health Assessment ==="

# Core component verification
echo "Core Component Status:"
python3 -m SuperGemini --version && echo "✅ SuperGemini installed" || echo "❌ SuperGemini not found"
ls ~/.gemini/GEMINI.md >/dev/null 2>&1 && echo "✅ Configuration exists" || echo "❌ Configuration missing"
grep -q "SuperGemini" ~/.gemini/GEMINI.md 2>/dev/null && echo "✅ Configuration valid" || echo "❌ Configuration invalid"

# Dependency verification
echo "Dependency Status:"
python3 --version | grep -E "3\.[8-9]|3\.[1-9][0-9]" >/dev/null && echo "✅ Python version OK" || echo "❌ Python version incompatible"
which gemini >/dev/null 2>&1 && echo "✅ Gemini CLI available" || echo "❌ Gemini CLI not found"

# MCP server verification
echo "MCP Server Status:"
node --version 2>/dev/null | grep -E "v1[6-9]|v[2-9][0-9]" >/dev/null && echo "✅ Node.js version OK" || echo "⚠️ Node.js version may be incompatible"
npm list -g 2>/dev/null | grep -E "context7|sequential|magic" >/dev/null && echo "✅ MCP servers installed" || echo "⚠️ No MCP servers found"

# File system verification
echo "File System Status:"
[ -w ~/.gemini/ ] && echo "✅ Configuration directory writable" || echo "❌ Configuration directory not writable"
df -h ~/.gemini/ | tail -1 | awk '{if($5+0 < 90) print "✅ Sufficient disk space: " $5 " used"; else print "⚠️ Low disk space: " $5 " used"}'

# Network verification (if MCP servers require internet)
echo "Network Status:"
ping -c 1 8.8.8.8 >/dev/null 2>&1 && echo "✅ Internet connectivity OK" || echo "⚠️ Internet connectivity issues"
```

**Configuration Integrity Analysis:**
```bash
# Configuration file integrity analysis
echo "=== Configuration Integrity Analysis ==="

# GEMINI.md structure analysis
echo "GEMINI.md Analysis:"
if [ -f ~/.gemini/GEMINI.md ]; then
    line_count=$(wc -l ~/.gemini/GEMINI.md | cut -d' ' -f1)
    if [ $line_count -gt 100 ]; then
        echo "✅ Configuration size appropriate: $line_count lines"
    else
        echo "⚠️ Configuration may be incomplete: $line_count lines"
    fi
    
    # Check for required imports
    import_count=$(grep -c "^@" ~/.gemini/GEMINI.md 2>/dev/null)
    if [ $import_count -gt 5 ]; then
        echo "✅ Import structure OK: $import_count imports"
    else
        echo "⚠️ Few imports found: $import_count imports"
    fi
    
    # Check for circular imports
    echo "Circular import check:"
    if grep -q "@GEMINI.md" ~/.gemini/GEMINI.md 2>/dev/null; then
        echo "❌ Circular import detected"
    else
        echo "✅ No circular imports"
    fi
else
    echo "❌ GEMINI.md not found"
fi

# Component file analysis
echo "Component Files Analysis:"
for component in FLAGS RULES PRINCIPLES; do
    if [ -f ~/.gemini/${component}.md ]; then
        size=$(wc -l ~/.gemini/${component}.md | cut -d' ' -f1)
        echo "✅ ${component}.md: $size lines"
    else
        echo "❌ ${component}.md missing"
    fi
done
```

### Error Pattern Analysis

**Error Classification and Analysis:**
```bash
# Error pattern analysis and classification
echo "=== Error Pattern Analysis ==="

# Create error classification function
classify_error() {
    local error_msg="$1"
    
    case "$error_msg" in
        *"permission denied"*|*"Permission denied"*)
            echo "PERMISSION_ERROR: File system access issue"
            ;;
        *"command not found"*|*"not recognized"*)
            echo "COMMAND_ERROR: Installation or configuration issue"
            ;;
        *"timeout"*|*"connection failed"*)
            echo "NETWORK_ERROR: Connectivity or server issue"
            ;;
        *"memory"*|*"out of memory"*)
            echo "RESOURCE_ERROR: Insufficient system resources"
            ;;
        *"syntax error"*|*"invalid"*)
            echo "CONFIGURATION_ERROR: Configuration file corruption"
            ;;
        *"dependency"*|*"module not found"*)
            echo "DEPENDENCY_ERROR: Missing required components"
            ;;
        *)
            echo "UNKNOWN_ERROR: Requires manual investigation"
            ;;
    esac
}

# Error log analysis (if logs exist)
echo "Error Log Analysis:"
if [ -f ~/.gemini/error.log ]; then
    echo "Recent errors:"
    tail -20 ~/.gemini/error.log | while read line; do
        error_type=$(classify_error "$line")
        echo "$error_type: $line"
    done
else
    echo "No error log found"
fi

# System log analysis for SuperGemini-related errors
echo "System Log Analysis:"
journalctl --since "1 day ago" 2>/dev/null | grep -i -E "superclaude|gemini|python.*error" | tail -10 || echo "No system logs available"
```

**Root Cause Analysis Procedures:**
```bash
# Systematic root cause analysis
echo "=== Root Cause Analysis ==="

# Problem reproduction framework
echo "Problem Reproduction Framework:"
cat << 'EOF'
Root Cause Analysis Steps:

1. OBSERVATION: What exactly is failing?
   - Record exact error messages
   - Note system state when error occurs
   - Document reproduction steps

2. HYPOTHESIS: What might be causing the issue?
   - Installation problems
   - Configuration errors
   - Resource constraints
   - Environmental issues

3. TESTING: How to verify the hypothesis?
   - Isolated component testing
   - Resource monitoring during failure
   - Configuration validation
   - Dependency verification

4. RESOLUTION: How to fix the identified cause?
   - Apply targeted solutions
   - Verify fix effectiveness
   - Prevent recurrence
   - Document solution
EOF

# Automated diagnostic procedures
echo "Automated Diagnostic Procedures:"

# Test isolation procedure
test_isolation() {
    echo "Testing component isolation:"
    
    # Test basic Python functionality
    python3 -c "print('Python OK')" && echo "✅ Python working" || echo "❌ Python issue"
    
    # Test SuperGemini installation
    python3 -m SuperGemini --version >/dev/null 2>&1 && echo "✅ SuperGemini installed" || echo "❌ SuperGemini issue"
    
    # Test configuration loading
    [ -f ~/.gemini/GEMINI.md ] && echo "✅ Configuration exists" || echo "❌ Configuration missing"
    
    # Test MCP servers (if applicable)
    if which node >/dev/null 2>&1; then
        npm list -g >/dev/null 2>&1 && echo "✅ npm working" || echo "❌ npm issue"
    fi
}

test_isolation
```

## Performance Benchmarking

### Baseline Performance Metrics

**Performance Baseline Establishment:**
```bash
# Establish SuperGemini performance baselines
echo "=== Performance Baseline Establishment ==="

# System capability assessment
echo "System Capability Assessment:"
echo "CPU cores: $(nproc)"
echo "Memory: $(free -h | grep Mem | awk '{print $2}')"
echo "Storage type: $(lsblk -o NAME,ROTA | grep "0$" >/dev/null && echo "SSD" || echo "HDD")"
echo "Python version: $(python3 --version)"

# Operation timing benchmarks
echo "Operation Timing Benchmarks:"

# Basic operations
echo "Basic operation timings:"
time_basic() {
    local start_time=$(date +%s.%N)
    eval "$1" >/dev/null 2>&1
    local end_time=$(date +%s.%N)
    echo "$(echo "$end_time - $start_time" | bc)s"
}

echo "SuperGemini version check: $(time_basic 'python3 -m SuperGemini --version')"
echo "Configuration read: $(time_basic 'cat ~/.gemini/GEMINI.md | wc -l')"
echo "Session directory list: $(time_basic 'ls ~/.gemini/sessions/')"

# File operation benchmarks
echo "File Operation Benchmarks:"
temp_file="/tmp/superclaude_test_$(date +%s).txt"
dd if=/dev/zero of="$temp_file" bs=1M count=10 >/dev/null 2>&1
read_time=$(time_basic "cat $temp_file")
echo "10MB file read: ${read_time}"
rm "$temp_file"

# Memory usage baseline
echo "Memory Usage Baseline:"
python3 -c "
import psutil
import os
process = psutil.Process(os.getpid())
print(f'Current memory usage: {process.memory_info().rss / 1024 / 1024:.1f} MB')
"
```

**Performance Regression Testing:**
```bash
# Performance regression detection
echo "=== Performance Regression Testing ==="

# Create performance test suite
create_performance_test() {
    cat << 'EOF' > /tmp/superclaude_perf_test.py
#!/usr/bin/env python3
import time
import subprocess
import json
import sys
import os

def time_operation(command, description):
    """Time a shell command and return duration"""
    start_time = time.time()
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
        end_time = time.time()
        duration = end_time - start_time
        success = result.returncode == 0
        return {
            'description': description,
            'duration': duration,
            'success': success,
            'command': command
        }
    except subprocess.TimeoutExpired:
        return {
            'description': description,
            'duration': 30.0,
            'success': False,
            'command': command,
            'error': 'timeout'
        }

def run_performance_tests():
    """Run suite of performance tests"""
    tests = [
        ('python3 -m SuperGemini --version', 'Version check'),
        ('ls ~/.gemini/', 'Config directory list'),
        ('cat ~/.gemini/GEMINI.md | wc -l', 'Config file read'),
        ('find ~/.gemini/ -name "*.md" | wc -l', 'Config file search'),
    ]
    
    results = []
    for command, description in tests:
        print(f"Testing: {description}...")
        result = time_operation(command, description)
        results.append(result)
        status = "✅" if result['success'] else "❌"
        print(f"  {status} {description}: {result['duration']:.3f}s")
    
    return results

if __name__ == "__main__":
    print("SuperGemini Performance Test Suite")
    print("=" * 40)
    results = run_performance_tests()
    
    # Save results for comparison
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    results_file = f"/tmp/superclaude_perf_{timestamp}.json"
    with open(results_file, 'w') as f:
        json.dump({
            'timestamp': timestamp,
            'results': results
        }, f, indent=2)
    
    print(f"\nResults saved to: {results_file}")
    
    # Summary statistics
    successful_tests = [r for r in results if r['success']]
    if successful_tests:
        avg_duration = sum(r['duration'] for r in successful_tests) / len(successful_tests)
        print(f"Average operation time: {avg_duration:.3f}s")
    
    failed_tests = [r for r in results if not r['success']]
    if failed_tests:
        print(f"Failed tests: {len(failed_tests)}")
        for test in failed_tests:
            print(f"  - {test['description']}")
EOF

    python3 /tmp/superclaude_perf_test.py
    rm /tmp/superclaude_perf_test.py
}

create_performance_test
```

### Resource Usage Optimization

**Memory Usage Optimization:**
```bash
# Memory usage optimization and monitoring
echo "=== Memory Usage Optimization ==="

# Memory usage analysis
analyze_memory_usage() {
    echo "Current memory state:"
    free -h
    echo ""
    
    echo "SuperGemini-related processes:"
    ps aux | grep -E "python.*SuperGemini|node.*mcp" | head -10
    echo ""
    
    echo "Memory-intensive processes:"
    ps aux --sort=-%mem | head -10
    echo ""
    
    # Memory usage recommendations
    total_mem=$(free -m | grep Mem | awk '{print $2}')
    used_mem=$(free -m | grep Mem | awk '{print $3}')
    mem_percent=$((used_mem * 100 / total_mem))
    
    echo "Memory usage: ${mem_percent}%"
    if [ $mem_percent -gt 80 ]; then
        echo "⚠️ High memory usage detected"
        echo "Recommendations:"
        echo "  - Clear old session files: rm -rf ~/.gemini/sessions/old-*"
        echo "  - Restart Gemini CLI session"
        echo "  - Use scope limiting: --scope file"
        echo "  - Close unused applications"
    elif [ $mem_percent -gt 60 ]; then
        echo "ℹ️ Moderate memory usage"
        echo "Consider periodic session cleanup"
    else
        echo "✅ Memory usage is acceptable"
    fi
}

analyze_memory_usage

# Memory cleanup procedures
echo "Memory Cleanup Procedures:"
echo "1. Session cleanup: find ~/.gemini/sessions/ -mtime +7 -delete"
echo "2. Temporary file cleanup: rm -rf /tmp/superclaude-*"
echo "3. System cache cleanup: sync && echo 3 > /proc/sys/vm/drop_caches (requires sudo)"
echo "4. Browser cache cleanup (if using Playwright MCP)"
```

**CPU Usage Optimization:**
```bash
# CPU usage optimization
echo "=== CPU Usage Optimization ==="

# CPU analysis
analyze_cpu_usage() {
    echo "CPU usage analysis:"
    
    # Current CPU load
    cpu_load=$(uptime | awk -F'load average:' '{print $2}' | awk '{print $1}' | cut -d',' -f1)
    cpu_cores=$(nproc)
    cpu_percent=$(echo "$cpu_load * 100 / $cpu_cores" | bc -l | cut -d'.' -f1)
    
    echo "CPU load average: $cpu_load (${cpu_percent}% of capacity)"
    
    # Process CPU usage
    echo "Top CPU consumers:"
    ps aux --sort=-%cpu | head -10
    
    # SuperGemini-specific CPU usage
    echo "SuperGemini-related CPU usage:"
    ps aux | grep -E "python.*SuperGemini|node.*mcp" | awk '{sum+=$3} END {print "Total CPU: " sum "%"}'
    
    # CPU optimization recommendations
    if [ $cpu_percent -gt 80 ]; then
        echo "⚠️ High CPU usage detected"
        echo "Recommendations:"
        echo "  - Use operation scope limiting"
        echo "  - Break complex tasks into smaller operations"
        echo "  - Avoid parallel MCP server operations"
        echo "  - Consider system upgrade"
    else
        echo "✅ CPU usage is acceptable"
    fi
}

analyze_cpu_usage
```

## Advanced Troubleshooting Techniques

### Systematic Problem Resolution

**Multi-Layer Diagnostic Approach:**
```bash
# Multi-layer diagnostic framework
echo "=== Multi-Layer Diagnostic Framework ==="

# Layer 1: System level
echo "Layer 1 - System Level Diagnostics:"
echo "Operating system: $(uname -a)"
echo "Available memory: $(free -h | grep Mem | awk '{print $7}')"
echo "Available disk: $(df -h ~ | tail -1 | awk '{print $4}')"
echo "System load: $(uptime | awk -F'load average:' '{print $2}')"

# Layer 2: Python environment
echo "Layer 2 - Python Environment:"
echo "Python version: $(python3 --version)"
echo "Python executable: $(which python3)"
echo "Python modules: $(python3 -c 'import sys; print(len(sys.modules))') loaded"
echo "SuperGemini installation: $(python3 -m SuperGemini --version 2>/dev/null || echo 'Not installed')"

# Layer 3: SuperGemini configuration
echo "Layer 3 - SuperGemini Configuration:"
echo "Configuration directory: $(ls -ld ~/.gemini/ 2>/dev/null || echo 'Not found')"
echo "Configuration files: $(find ~/.gemini/ -name "*.md" 2>/dev/null | wc -l) files"
echo "Session files: $(find ~/.gemini/sessions/ -name "*.json" 2>/dev/null | wc -l) sessions"

# Layer 4: MCP servers
echo "Layer 4 - MCP Servers:"
if which node >/dev/null 2>&1; then
    echo "Node.js version: $(node --version)"
    echo "MCP servers: $(npm list -g 2>/dev/null | grep -E "context7|sequential|magic" | wc -l) installed"
else
    echo "Node.js: Not installed"
fi

# Layer 5: Gemini CLI integration
echo "Layer 5 - Gemini CLI Integration:"
if which gemini >/dev/null 2>&1; then
    echo "Gemini CLI: $(gemini --version 2>/dev/null || echo 'Version unknown')"
else
    echo "Gemini CLI: Not found in PATH"
fi
```

**Dependency Chain Analysis:**
```bash
# Dependency chain verification
echo "=== Dependency Chain Analysis ==="

# Create dependency verification function
verify_dependency_chain() {
    local status=0
    
    echo "Verifying dependency chain:"
    
    # Level 1: Operating system
    echo -n "1. Operating system compatibility: "
    case "$(uname -s)" in
        Linux*) echo "✅ Linux" ;;
        Darwin*) echo "✅ macOS" ;;
        CYGWIN*|MINGW*) echo "✅ Windows" ;;
        *) echo "⚠️ Unknown OS"; status=1 ;;
    esac
    
    # Level 2: Python
    echo -n "2. Python 3.8+ requirement: "
    if python3 -c "import sys; sys.exit(0 if sys.version_info >= (3, 8) else 1)" 2>/dev/null; then
        echo "✅ $(python3 --version)"
    else
        echo "❌ Python 3.8+ required"
        status=1
    fi
    
    # Level 3: SuperGemini package
    echo -n "3. SuperGemini package: "
    if python3 -m SuperGemini --version >/dev/null 2>&1; then
        echo "✅ Installed"
    else
        echo "❌ Not installed or corrupted"
        status=1
    fi
    
    # Level 4: Configuration files
    echo -n "4. Configuration files: "
    if [ -f ~/.gemini/GEMINI.md ] && [ -s ~/.gemini/GEMINI.md ]; then
        echo "✅ Present and non-empty"
    else
        echo "❌ Missing or empty"
        status=1
    fi
    
    # Level 5: Node.js (optional but recommended)
    echo -n "5. Node.js for MCP servers: "
    if which node >/dev/null 2>&1; then
        node_version=$(node --version | cut -d'v' -f2 | cut -d'.' -f1)
        if [ "$node_version" -ge 16 ]; then
            echo "✅ Node.js $(node --version)"
        else
            echo "⚠️ Node.js version may be too old"
        fi
    else
        echo "⚠️ Not installed (MCP servers unavailable)"
    fi
    
    # Level 6: Gemini CLI integration
    echo -n "6. Gemini CLI integration: "
    if which gemini >/dev/null 2>&1; then
        echo "✅ Gemini CLI available"
    else
        echo "⚠️ Gemini CLI not found"
    fi
    
    return $status
}

verify_dependency_chain
dependency_status=$?

if [ $dependency_status -eq 0 ]; then
    echo "✅ All dependencies satisfied"
else
    echo "❌ Dependency issues detected - resolve before proceeding"
fi
```

## Emergency Procedures

### Complete System Recovery

**Full System Recovery Protocol:**
```bash
# Complete SuperGemini system recovery
echo "=== SuperGemini Emergency Recovery Protocol ==="

# Step 1: System state backup
echo "Step 1: Creating system state backup..."
backup_timestamp=$(date +%Y%m%d_%H%M%S)
backup_dir=~/superclaude_recovery_$backup_timestamp

mkdir -p "$backup_dir"
[ -d ~/.gemini/ ] && cp -r ~/.gemini/ "$backup_dir/claude_config/"
[ -d ~/.npm/ ] && cp -r ~/.npm/  "$backup_dir/npm_config/" 2>/dev/null || true
env | grep -E "CLAUDE|PYTHON|NODE" > "$backup_dir/environment_vars.txt"
python3 -m pip list > "$backup_dir/python_packages.txt" 2>/dev/null || true
npm list -g > "$backup_dir/npm_packages.txt" 2>/dev/null || true

echo "Backup created in: $backup_dir"

# Step 2: Complete cleanup
echo "Step 2: Performing complete cleanup..."
rm -rf ~/.gemini/
npm cache clean --force 2>/dev/null || true
python3 -m pip uninstall SuperGemini -y 2>/dev/null || true

# Step 3: Fresh installation
echo "Step 3: Fresh SuperGemini installation..."
python3 -m pip install SuperGemini
if [ $? -eq 0 ]; then
    echo "✅ SuperGemini package installed"
else
    echo "❌ Package installation failed"
    exit 1
fi

# Step 4: Configuration setup
echo "Step 4: Configuration setup..."
python3 -m SuperGemini install --fresh
if [ $? -eq 0 ]; then
    echo "✅ Configuration installed"
else
    echo "❌ Configuration setup failed"
    exit 1
fi

# Step 5: MCP server installation (if Node.js available)
if which node >/dev/null 2>&1; then
    echo "Step 5: MCP server installation..."
    python3 -m SuperGemini install --components mcp --force
    if [ $? -eq 0 ]; then
        echo "✅ MCP servers installed"
    else
        echo "⚠️ MCP server installation failed - continuing without MCP"
    fi
else
    echo "Step 5: Skipping MCP servers (Node.js not available)"
fi

# Step 6: Verification
echo "Step 6: Installation verification..."
if python3 -m SuperGemini --version && [ -f ~/.gemini/GEMINI.md ]; then
    echo "✅ Recovery completed successfully"
    echo "Backup available at: $backup_dir"
else
    echo "❌ Recovery failed - check logs and backup"
    exit 1
fi
```

**Disaster Recovery Checklist:**
```bash
# Disaster recovery checklist and procedures
echo "=== Disaster Recovery Checklist ==="

cat << 'EOF'
SuperGemini Disaster Recovery Checklist:

PRE-RECOVERY ASSESSMENT:
□ Identify specific failure symptoms
□ Document error messages and conditions
□ Check system resource availability
□ Verify backup existence and integrity

RECOVERY STEPS:
□ Create system state backup
□ Stop all Gemini CLI sessions
□ Clear corrupted configurations
□ Perform fresh installation
□ Verify basic functionality
□ Restore custom configurations (if applicable)
□ Test core operations
□ Reinstall MCP servers (if needed)
□ Validate full functionality

POST-RECOVERY VERIFICATION:
□ Test SuperGemini version command
□ Verify configuration file integrity
□ Test basic operations in Gemini CLI
□ Validate MCP server functionality
□ Document recovery process and lessons learned

PREVENTION MEASURES:
□ Regular configuration backups
□ System resource monitoring
□ Update management procedures
□ Recovery procedure documentation
□ Test recovery procedures periodically
EOF
```

## Related Resources

### Diagnostic Tool References
- **System Monitoring**: `htop`, `iostat`, `netstat`, `free`, `df`
- **Process Analysis**: `ps`, `top`, `pgrep`, `lsof`
- **Network Diagnostics**: `ping`, `curl`, `wget`, `ss`
- **Log Analysis**: `journalctl`, `tail`, `grep`, `awk`

### SuperGemini-Specific Resources
- **Common Issues**: [common-issues.md](common-issues.md) - Basic troubleshooting procedures
- **MCP Server Guide**: [mcp-server-guide.md](mcp-server-guide.md) - MCP-specific diagnostics
- **Installation Guide**: [../Getting-Started/installation.md](../Getting-Started/installation.md) - Setup procedures
- **User Guide**: [../User-Guide/](../User-Guide/) - Operational documentation

### Support and Community
- **GitHub Issues**: [Technical support and bug reporting](https://github.com/SuperGemini-Org/SuperGemini_Framework/issues)
- **GitHub Discussions**: [Community support and best practices](https://github.com/SuperGemini-Org/SuperGemini_Framework/discussions)
- **Contributing Guide**: [../Developer-Guide/contributing-code.md](../Developer-Guide/contributing-code.md) - Development contribution

---

**Diagnostic Philosophy**: Approach problems systematically - start with basic verification, isolate components, test hypotheses, and apply targeted solutions. Document findings for future reference and community benefit.

**Emergency Contact**: For critical system failures, use the complete recovery protocol above. If issues persist after recovery, document the full diagnostic output and seek community support through GitHub issues.