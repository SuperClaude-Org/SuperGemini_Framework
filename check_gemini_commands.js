const { spawn } = require('child_process');

console.log('Checking Gemini CLI commands...\n');

const gemini = spawn('gemini', [], {
  env: { ...process.env, TERM: 'xterm-256color' }
});

let output = '';
let helpSent = false;
let timeoutId;

gemini.stdout.on('data', (data) => {
  output += data.toString();
  
  if (!helpSent && output.includes('>')) {
    console.log('Sending /help command...\n');
    gemini.stdin.write('/help\n');
    helpSent = true;
    
    // Collect output for 2 seconds then analyze
    timeoutId = setTimeout(() => {
      console.log('=== Available Commands ===\n');
      
      // Extract command list
      const lines = output.split('\n');
      let inCommandSection = false;
      let commands = [];
      
      for (const line of lines) {
        if (line.includes('Available commands') || line.includes('Commands:')) {
          inCommandSection = true;
          continue;
        }
        
        if (inCommandSection && line.trim() === '') {
          inCommandSection = false;
        }
        
        if (inCommandSection && line.includes('/')) {
          commands.push(line.trim());
        }
      }
      
      console.log('Found commands:');
      commands.forEach(cmd => console.log(cmd));
      
      console.log('\n=== Checking for /sc commands ===');
      const sgCommands = commands.filter(cmd => cmd.includes('sg:'));
      if (sgCommands.length > 0) {
        console.log('Found /sc commands:');
        sgCommands.forEach(cmd => console.log(cmd));
      } else {
        console.log('No /sc commands found');
      }
      
      gemini.stdin.write('/quit\n');
      setTimeout(() => process.exit(0), 500);
    }, 2000);
  }
});

gemini.on('error', (error) => {
  console.error('Error:', error);
  process.exit(1);
});