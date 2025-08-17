#!/usr/bin/env node
const { spawnSync } = require("child_process");
const { detectPython, detectPip } = require("./checkEnv");

let pythonCmd = detectPython();
if (!pythonCmd) {
  console.error("❌ Python 3 is required but not found.");
  process.exit(1);
}

const args = process.argv.slice(2);

// Special case: update command
if (args[0] === "update") {
  require("./update");
  process.exit(0);
}

// Forward everything to Python SuperGemini
const result = spawnSync(pythonCmd, ["-m", "SuperGemini", ...args], { stdio: "inherit", shell: true });
process.exit(result.status);
    
