# **Defense in Depth**

## **Definition**
**Defense in Depth (DiD)** is a cybersecurity strategy that uses multiple layers of security controls to protect systems and data. If one layer fails, others remain to mitigate the attack.

---

## **Key Security Layers**
1. **Network Security:** Firewalls, secure network architecture.
2. **Access Control:** Role-based access, authentication, and authorization.
3. **Application Security:** Input validation, secure APIs.
4. **Data Security:** Encryption and data integrity mechanisms.
5. **Endpoint Security:** Antivirus, device security policies.
6. **Monitoring and Auditing:** Intrusion detection systems.

---

## **Code Examples for Each Layer**

### **1. Network Security with Firewall Rules**
A basic firewall rule using `iptables` in Linux:

```bash
# Allow incoming traffic on port 443 (HTTPS)
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Drop all other traffic by default
sudo iptables -P INPUT DROP
```

2. Access Control in a Web Application (C++) 
```c++
#include <iostream>
#include <map>
#include <string>

using namespace std;

// Simple role-based access control
map<string, string> userRoles = {{"alice", "admin"}, {"bob", "user"}};

bool hasAccess(const string &username, const string &requiredRole) {
    return userRoles[username] == requiredRole;
}

int main() {
    string username = "bob";
    
    if (hasAccess(username, "admin")) {
        cout << "Access granted to admin resources." << endl;
    } else {
        cout << "Access denied." << endl;
    }
    return 0;
}

```

3. Application Security: Input Validation (C++)
Preventing command injection by sanitizing user input:

```c++
#include <iostream>
#include <regex>

using namespace std;

bool isValidInput(const string &input) {
    // Allow only alphanumeric characters
    regex pattern("^[a-zA-Z0-9]+$");
    return regex_match(input, pattern);
}

int main() {
    string userInput;
    cout << "Enter a search term: ";
    cin >> userInput;

    if (isValidInput(userInput)) {
        cout << "Safe input: " << userInput << endl;
    } else {
        cout << "Invalid input detected!" << endl;
    }

    return 0;
}
```

4. Data Security: Encrypting Data (C++)
Using OpenSSL for AES encryption.

```c++
#include <openssl/aes.h>
#include <iostream>
#include <cstring>

using namespace std;

int main() {
    unsigned char key[AES_BLOCK_SIZE];   // 128-bit key
    unsigned char inputText[AES_BLOCK_SIZE] = "SensitiveData";
    unsigned char encryptedText[AES_BLOCK_SIZE];
    
    // Set the key
    memset(key, 0, AES_BLOCK_SIZE);
    strncpy((char *)key, "mysecretkey12345", AES_BLOCK_SIZE);

    AES_KEY encryptKey;
    AES_set_encrypt_key(key, 128, &encryptKey);

    AES_encrypt(inputText, encryptedText, &encryptKey);

    cout << "Encrypted Data: ";
    for (int i = 0; i < AES_BLOCK_SIZE; i++) {
        printf("%02x", encryptedText[i]);
    }
    cout << endl;

    return 0;
}
```

5. Endpoint Security: File Permissions
Set file permissions on Linux to secure sensitive files.

```bash
# Owner has read and write permissions, others have no access
chmod 600 sensitive_file.txt
```
6. Monitoring and Auditing: Logging in C++
```c++

#include <iostream>
#include <fstream>
#include <ctime>

using namespace std;

void logEvent(const string &event) {
    ofstream logFile("security_log.txt", ios::app);
    if (logFile.is_open()) {
        time_t now = time(0);
        char *dt = ctime(&now);
        logFile << dt << ": " << event << endl;
        logFile.close();
    } else {
        cerr << "Unable to open log file" << endl;
    }
}

int main() {
    logEvent("User login attempt.");
    logEvent("Access to sensitive data denied.");
    return 0;
}

```


