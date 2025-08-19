const { spawnSync } = require("child_process");

function run(cmd, args = [], opts = {}) {
  return spawnSync(cmd, args, {
    stdio: opts.stdio || "pipe",
    shell: true
  });
}

function checkCommand(cmd, args = ["--version"]) {
  const result = run(cmd, args);
  return result.status === 0;
}

function detectPython() {
  const candidates = ["python3", "python", "py"];
  for (let c of candidates) {
    if (checkCommand(c)) return c;
  }
  return null;
}

function detectPip() {
  const candidates = ["pip3", "pip", "py -m pip"];
  for (let c of candidates) {
    if (checkCommand(c.split(" ")[0])) return c;
  }
  return null;
}

function isSuperGeminiInstalled(pipCmd) {
  const result = run(pipCmd, ["show", "SuperGemini"]);
  return result.status === 0;
}

module.exports = { run, detectPython, detectPip, isSuperGeminiInstalled };
