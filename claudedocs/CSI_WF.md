# Command Syntax Inconsistency Workflow (CSI_WF)

**Generated**: 2025-11-05
**Project**: SuperGemini v4.3.0
**Scope**: Documentation standardization for command syntax consistency

---

## Executive Summary

**Analysis Results**:
- ✅ **645** SuperGemini references across documentation
- ✅ **1,393** `/sg:` command prefix usages
- ⚠️ **20** "superclaude" references (legacy/related project confusion)
- ⚠️ Mixed capitalization patterns for CLI executable name

**Root Cause**: SuperGemini has evolved from SuperClaude ecosystem, leaving legacy references and inconsistent naming conventions across documentation.

**Impact**: User confusion about correct command syntax, particularly for installation and CLI usage.

---

## 1. Authoritative Source Analysis

### **Package Identity (pyproject.toml:44-47)**
```toml
[project.scripts]
SuperGemini = "SuperGemini.__main__:main"  # Primary (capitalized)
supergemini = "SuperGemini.__main__:main"  # Alias (lowercase)
sg = "SuperGemini.__main__:main"           # Short alias
```

### **Command System (setup/components/commands.py:16)**
```python
super().__init__(install_dir, Path("commands/sg"))  # /sg: namespace
```

### **Brand Identity**
- **Official Name**: SuperGemini (capitalized)
- **PyPI Package**: `SuperGemini`
- **NPM Package**: `@superclaude-org/supergemini`
- **GitHub Org**: SuperClaude-Org (umbrella organization)

---

## 2. Standardization Rules

### **Rule 1: Product Name**
**Context**: Prose, documentation titles, marketing
**Standard**: **SuperGemini** (always capitalized)

✅ **Correct**:
```
"SuperGemini is a meta-programming framework..."
"Install SuperGemini with pipx"
"SuperGemini Framework v4.3.0"
```

❌ **Incorrect**:
```
"supergemini is a framework"
"Install superGemini"
"SUPERGEMINI framework"
```

---

### **Rule 2: CLI Executable**
**Context**: Terminal commands, shell examples
**Standard**: **SuperGemini** (capitalized) - matches primary script entry point

✅ **Correct**:
```bash
SuperGemini install --yes
SuperGemini update
SuperGemini uninstall
```

✅ **Also Acceptable** (for advanced users):
```bash
supergemini install  # lowercase alias
sg install           # short alias
```

**Documentation Approach**:
- **Always show primary**: `SuperGemini install`
- **Optional note**: "Advanced: Use `sg` for shorthand"

---

### **Rule 3: Slash Command Prefix**
**Context**: Inside Gemini CLI, after installation
**Standard**: **/sg:** (lowercase, colon-terminated)

✅ **Correct**:
```
/sg:analyze src/
/sg:implement "feature"
/sg:test --coverage
```

**Explanation Context**:
- "SuperGemini provides 18 slash commands with the **/sg:** prefix"
- "Commands are accessed via `/sg:[command]` pattern"

❌ **Incorrect**:
```
/SG:analyze          # uppercase prefix
/supergemini:analyze # full name in prefix
/sc:analyze          # wrong prefix (SuperClaude)
```

---

### **Rule 4: Related Projects**
**Context**: References to SuperClaude, SuperQwen, superagent
**Standard**: Clarify relationship explicitly

✅ **Correct**:
```
"SuperGemini is part of the SuperClaude-Org ecosystem"
"Migrate from SuperClaude using superagent MCP server"
"See also: SuperClaude Framework, SuperQwen Framework"
```

---

## 3. Identified Issues & Resolutions

### **Issue A: "superclaude install" in Documentation**

**Evidence**: TODO.md line 18 references `superclaude install`

**Analysis**: This is a **legacy reference** or **copy-paste error**. SuperClaude is a related project, NOT an alias for SuperGemini.

**Resolution**: Replace all instances with `SuperGemini install`

**Files to Fix**:
- Search pattern: `superclaude install`
- Expected: 0 matches in SuperGemini docs (should reference SuperClaude explicitly if intentional)

---

### **Issue B: Inconsistent Capitalization**

**Evidence**: Mixed `SuperGemini install` vs `supergemini install` in examples

**Current Distribution** (from grep analysis):
- installation.md: Predominantly uses `SuperGemini install` ✅
- README.md: Uses `SuperGemini install` ✅
- Some examples may use lowercase

**Resolution**: Standardize to `SuperGemini install` (matches pyproject.toml primary script)

---

### **Issue C: Command Prefix Ambiguity**

**Evidence**: Documentation sometimes writes `/sg:` vs `/sg:help` without context clarity

**Analysis**:
- `/sg:` is the **namespace prefix** (used in prose: "commands use /sg: prefix")
- `/sg:analyze` is the **full command** (used in examples)

**Resolution**: Context-dependent usage with clear distinction:

**Prose Context**:
```markdown
SuperGemini provides 18 slash commands with the `/sg:` prefix.
```

**Example Context**:
```markdown
Try these commands:
- `/sg:analyze src/`
- `/sg:implement "feature"`
```

---

## 4. Migration Plan

### **Phase 1: Critical Fixes** (Immediate)

**Target**: Remove incorrect/confusing references

| Pattern | Fix | Priority | Est. Occurrences |
|---------|-----|----------|------------------|
| `superclaude install` | `SuperGemini install` | 🔴 CRITICAL | ~5 |
| `SUPERGEMINI` (all caps) | `SuperGemini` | 🟡 HIGH | Unknown |
| `/sc:` (wrong prefix) | `/sg:` or clarify as SuperClaude | 🟡 HIGH | ~2 (in TODO.md) |

---

### **Phase 2: Standardization** (Next)

**Target**: Enforce consistent patterns project-wide

**A) CLI Executable Standardization**

**Files**: Docs/Getting-Started/installation.md, README.md, all tutorials

**Find**:
```regex
(?i)(supergemini|SUPERGEMINI)\s+(install|update|uninstall|--\w+)
```

**Strategy**:
- Replace with `SuperGemini [command]` for documentation
- Add note: "Aliases available: `supergemini`, `sg`"

**B) Slash Command Prefix Clarification**

**Files**: Docs/User-Guide/commands.md, quick-start-practices.md, modes.md

**Strategy**:
- **First mention**: "SuperGemini commands use the `/sg:` prefix"
- **Examples**: Always show full command `/sg:analyze`, not just `/sg:`
- **Add glossary entry**:
  ```markdown
  **Command Prefix**: `/sg:` - namespace for SuperGemini commands in Gemini CLI
  **Example**: `/sg:analyze src/` - runs the analyze command
  ```

---

### **Phase 3: Documentation Enhancement** (Future)

**A) Add Disambiguation Section**

**Location**: Docs/Getting-Started/installation.md (after installation instructions)

**Content**:
```markdown
## Command Syntax Reference

### Installation Commands (Terminal)
Run these in your terminal to manage SuperGemini:
```bash
SuperGemini install     # Install/configure SuperGemini
SuperGemini update      # Update to latest version
SuperGemini uninstall   # Remove SuperGemini
```

**Aliases**: Advanced users can use `supergemini` (lowercase) or `sg` (short form)

### Slash Commands (Gemini CLI)
After installation, use these inside Gemini CLI:
```
/sg:analyze src/        # Analyze codebase
/sg:implement "feature" # Implement feature
/sg:test --coverage     # Run tests
```

**Pattern**: All commands follow `/sg:[command]` format
```

---

**B) Add Related Projects Section**

**Location**: README.md (near badges/intro)

**Content**:
```markdown
## SuperClaude-Org Ecosystem

SuperGemini is part of the SuperClaude-Org framework family:

- 🔷 **SuperGemini** (this project) - Gemini CLI enhancement framework
- 🔶 **SuperClaude** - Claude Code enhancement framework
- 🔸 **SuperQwen** - Qwen CLI enhancement framework

Each framework is independent but shares similar architecture. Commands use different prefixes:
- SuperGemini: `/sg:` prefix
- SuperClaude: `/sc:` prefix
- SuperQwen: `/sq:` prefix
```

---

## 5. Implementation Checklist

### **Phase 1 Tasks** (Critical - Do First)

- [ ] **Search & Replace**: `superclaude install` → `SuperGemini install`
- [ ] **Validate**: Confirm no "superclaude" appears in installation docs (except MCP server references)
- [ ] **Clarify**: Add note distinguishing SuperClaude (related project) from SuperGemini

### **Phase 2 Tasks** (Standardization)

- [ ] **Audit**: Run `grep -ri "supergemini install\|SUPERGEMINI" Docs/` for inconsistent casing
- [ ] **Standardize CLI**: Ensure all installation examples use `SuperGemini` (capitalized)
- [ ] **Clarify Prefix**: Add glossary entry for `/sg:` vs `/sg:[command]` distinction
- [ ] **Update Commands Docs**: Ensure commands.md explains prefix clearly

### **Phase 3 Tasks** (Enhancement)

- [ ] **Add Disambiguation**: Create "Command Syntax Reference" section in installation.md
- [ ] **Document Ecosystem**: Add "SuperClaude-Org Ecosystem" section to README.md
- [ ] **Add Aliases Note**: Document `supergemini` and `sg` as advanced aliases
- [ ] **Cross-Reference**: Link to SuperClaude/SuperQwen docs where relevant

---

## 6. Validation Strategy

### **Automated Checks**

**A) Pattern Validation**
```bash
# Check for incorrect patterns
grep -ri "superclaude install" Docs/          # Should return 0 (except MCP refs)
grep -ri "SUPERGEMINI\s+" Docs/                # Should return 0
grep -ri "/sc:" Docs/ | grep -v "SuperClaude" # Should return 0

# Check for correct patterns
grep -r "SuperGemini install" Docs/ | wc -l   # Should be consistent
grep -r "/sg:" Docs/ | wc -l                  # Should be majority usage
```

**B) Context Validation**
```bash
# Ensure prose uses capitalized brand
grep -r "supergemini is\|supergemini provides" Docs/ # Should return 0

# Ensure examples use correct executable
grep -r "^supergemini install" Docs/ # Should return 0 (lowercase not in examples)
```

### **Manual Review Points**

- [ ] First-time user can distinguish terminal commands from Gemini CLI commands
- [ ] Installation instructions are unambiguous about `SuperGemini install` syntax
- [ ] Relationship to SuperClaude is clear (related project, different prefix)
- [ ] `/sg:` prefix explanation appears before first command example

---

## 7. Documentation Style Guide (Derived)

### **A) When to Capitalize**

| Context | Standard | Example |
|---------|----------|---------|
| Product name | SuperGemini | "SuperGemini is a framework" |
| Documentation title | SuperGemini | "SuperGemini User Guide" |
| Package reference | SuperGemini | "Install via `pipx install SuperGemini`" |
| CLI executable | SuperGemini | `SuperGemini install --yes` |
| Slash commands | lowercase | `/sg:analyze` (not `/SG:analyze`) |
| File paths | as-is | `SuperGemini/Commands/` (follows codebase) |

### **B) Command Formatting**

**Terminal Commands**:
```bash
# Always show in code blocks with bash syntax
SuperGemini install
SuperGemini update --components mcp
```

**Gemini CLI Commands**:
```markdown
# Show as inline code or in examples
Use `/sg:analyze` to analyze your codebase.

Try these commands:
- `/sg:implement "user auth"`
- `/sg:test --coverage`
```

### **C) Cross-Project References**

**When mentioning SuperClaude**:
```markdown
Migrating from SuperClaude? Use the superagent MCP server.
See also: [SuperClaude Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework)
```

**NOT**:
```markdown
superclaude users can migrate... ❌ (use "SuperClaude users")
```

---

## 8. Risk Assessment

### **Breaking Changes**: None
- All current commands remain valid
- Lowercase `supergemini` alias still works (pyproject.toml:46)
- Users won't experience functional changes

### **Documentation Debt**: Low-Medium
- ~645 references to audit for capitalization
- ~20 "superclaude" references to clarify/fix
- Clear patterns make bulk fixes feasible

### **User Confusion Risk**: Reduced
- Current state: Mixed patterns confuse new users
- Post-fix state: Clear, consistent syntax guidance

---

## 9. Success Metrics

**Quantitative**:
- 0 instances of `superclaude install` in SuperGemini docs
- 100% of CLI examples use `SuperGemini install` (primary form)
- 100% of slash command examples use `/sg:` prefix

**Qualitative**:
- First-time users can install without syntax confusion
- Clear distinction between terminal commands and Gemini CLI commands
- Relationship to SuperClaude ecosystem is explicit

---

## 10. Next Steps

### **Immediate Actions**:

1. **Review & Approve**: Stakeholder review of this proposal
2. **Prioritize**: Confirm Phase 1 (critical fixes) scope
3. **Execute Phase 1**: Fix `superclaude install` references
4. **Test**: Validate changes don't break installation flows

### **Follow-up Actions**:

1. Execute Phase 2 (standardization) after Phase 1 validation
2. Add enhancement sections (Phase 3) during next documentation sprint
3. Update contributor guidelines with new style standards
4. Create documentation linter rules to prevent future inconsistencies

---

## 11. Technical Implementation Notes

### **A) Bulk Find/Replace Safety**

**Safe Patterns** (can automate):
```bash
# Fix critical errors
sed -i 's/superclaude install/SuperGemini install/g' Docs/**/*.md

# Fix capitalization (case-sensitive contexts)
# Use with caution - may need manual review for prose
```

**Manual Review Required**:
- References to SuperClaude as a separate project (keep as-is)
- MCP server references: `@superclaude-org/superagent` (keep as-is)
- File paths that must match codebase structure

### **B) CI/CD Integration**

**Add Documentation Linters**:
```yaml
# .github/workflows/docs-lint.yml
- name: Check Command Syntax
  run: |
    # Fail if incorrect patterns found
    ! grep -r "superclaude install" Docs/
    ! grep -r "SUPERGEMINI\s+" Docs/
    ! grep -ri "/sc:" Docs/ | grep -v "SuperClaude"
```

---

## Appendix: Reference Counts

**Analysis Date**: 2025-11-05

| Pattern | Count | Status |
|---------|-------|--------|
| `SuperGemini` (any case) | 645 | ✅ Predominant |
| `/sg:` prefix | 1,393 | ✅ Correct usage |
| `superclaude` | 20 | ⚠️ Needs clarification |
| `/sc:` prefix | 2 | ⚠️ Context-dependent (TODO.md) |

**Key Files by Reference Density**:
1. Docs/Getting-Started/installation.md: High (primary installation guide)
2. Docs/User-Guide/commands.md: High (command reference)
3. README.md: Medium (project introduction)
4. Docs/Reference/quick-start-practices.md: Medium (examples)

---

**Document Status**: ✅ Ready for Review
**Confidence Level**: High (based on pyproject.toml authority + codebase analysis)
**Estimated Effort**: 4-6 hours (Phase 1+2), 8-12 hours (all phases)