#!/usr/bin/env node
const { run, detectPip } = require("./checkEnv");

let pipCmd = detectPip();
if (!pipCmd) {
  console.error("❌ pip not found, cannot update.");
  process.exit(1);
}

console.log("🔄 Updating SuperGemini from PyPI...");
const result = run(pipCmd, ["install", "--upgrade", "SuperGemini"], { stdio: "inherit" });
if (result.status !== 0) {
  console.error("❌ Update failed.");
  process.exit(1);
}
console.log("✅ SuperGemini updated successfully!");
                            
