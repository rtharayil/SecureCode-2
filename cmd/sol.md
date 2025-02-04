Command injection is a security vulnerability that occurs when an attacker can execute arbitrary commands on the host operating system by manipulating input that is passed to a system command. In Node.js, this can happen when user input is improperly sanitized and passed to functions like `child_process.exec` or `child_process.execSync`.

Below is an example of a vulnerable Node.js application that demonstrates command injection, followed by a secure version that mitigates the vulnerability.

---

### **Vulnerable Node.js Application (Command Injection Example)**

#### **Code:**
```javascript
const express = require('express');
const { exec } = require('child_process');

const app = express();
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    res.send(`
        <h1>Ping a Website</h1>
        <form method="POST" action="/ping">
            <label for="host">Enter a hostname or IP address:</label>
            <input type="text" id="host" name="host" placeholder="e.g., google.com">
            <button type="submit">Ping</button>
        </form>
    `);
});

app.post('/ping', (req, res) => {
    const host = req.body.host;

    // Vulnerable code: user input is directly passed to exec
    exec(`ping -c 4 ${host}`, (error, stdout, stderr) => {
        if (error) {
            return res.send(`Error: ${stderr}`);
        }
        res.send(`<pre>${stdout}</pre>`);
    });
});

app.listen(3000, () => {
    console.log('Server running on http://localhost:3000');
});
```

---

#### **How It Works:**
1. The application provides a form where users can enter a hostname or IP address to ping.
2. The input is passed directly to the `exec` function, which executes the `ping` command on the server.

---

#### **Exploitation:**
An attacker can inject additional commands by appending them to the input. For example:
- Input: `google.com; ls -la`
- Resulting Command: `ping -c 4 google.com; ls -la`
- The `ls -la` command will list all files in the current directory, demonstrating command injection.

---

### **Secure Node.js Application (Mitigating Command Injection)**

To prevent command injection, you should:
1. **Validate and sanitize user input.**
2. **Use safer alternatives like `child_process.execFile` or `child_process.spawn`.**
3. **Avoid passing user input directly to system commands.**

#### **Code:**
```javascript
const express = require('express');
const { execFile } = require('child_process');

const app = express();
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    res.send(`
        <h1>Ping a Website</h1>
        <form method="POST" action="/ping">
            <label for="host">Enter a hostname or IP address:</label>
            <input type="text" id="host" name="host" placeholder="e.g., google.com">
            <button type="submit">Ping</button>
        </form>
    `);
});

app.post('/ping', (req, res) => {
    const host = req.body.host;

    // Validate the input (allow only alphanumeric, dots, and hyphens)
    if (!/^[a-zA-Z0-9.-]+$/.test(host)) {
        return res.status(400).send('Invalid hostname');
    }

    // Secure code: use execFile with arguments
    execFile('ping', ['-c', '4', host], (error, stdout, stderr) => {
        if (error) {
            return res.send(`Error: ${stderr}`);
        }
        res.send(`<pre>${stdout}</pre>`);
    });
});

app.listen(3000, () => {
    console.log('Server running on http://localhost:3000');
});
```

---

#### **How It Works:**
1. The input is validated using a regular expression to ensure it only contains alphanumeric characters, dots, and hyphens.
2. The `execFile` function is used instead of `exec`. It takes the command and arguments as separate parameters, preventing command injection.

---

#### **Why This is Secure:**
- **Input Validation:** The regular expression ensures that only valid hostnames or IP addresses are accepted.
- **Safer Command Execution:** `execFile` separates the command from its arguments, making it impossible to inject additional commands.

---

### **Additional Recommendations**
1. **Use a Whitelist:**
   Maintain a whitelist of allowed commands and arguments to further restrict what can be executed.
2. **Use Libraries for Shell Commands:**
   Use libraries like `shell-quote` or `sanitize-filename` to safely handle user input.
3. **Run with Least Privilege:**
   Execute the Node.js process with the least privileges necessary to reduce the impact of a potential attack.
4. **Log and Monitor:**
   Log all command executions and monitor for suspicious activity.

---

### **Example of a Whitelist Approach**
```javascript
const allowedCommands = {
    ping: ['-c', '4']
};

app.post('/ping', (req, res) => {
    const host = req.body.host;

    if (!/^[a-zA-Z0-9.-]+$/.test(host)) {
        return res.status(400).send('Invalid hostname');
    }

    const command = 'ping';
    const args = [...allowedCommands[command], host];

    execFile(command, args, (error, stdout, stderr) => {
        if (error) {
            return res.send(`Error: ${stderr}`);
        }
        res.send(`<pre>${stdout}</pre>`);
    });
});
```

---

### **Conclusion**
Command injection is a serious vulnerability that can allow attackers to execute arbitrary commands on your server. By validating and sanitizing user input, using safer alternatives like `execFile`, and following best practices, you can mitigate this risk and build secure Node.js applications.