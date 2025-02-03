# **Principle of Least Privilege (PoLP)**  
The **Principle of Least Privilege (PoLP)** ensures that a user, process, or service has the minimum permissions necessary to perform its tasks. It reduces the attack surface and limits the potential damage in case of a security breach.

---

## **Key Concepts of PoLP**
- Grant only **necessary permissions**.
- Limit access to sensitive resources.
- Remove unnecessary admin privileges.
- Periodically review and revoke permissions.

---

## **Code Examples for PoLP Implementation**

### **1. Role-Based Access Control (RBAC)**  
Restrict API routes based on user roles.

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock user roles
users = {
    "alice": "admin",
    "bob": "user"
}

# Mock data
sensitive_data = {"secret": "Top Secret Data"}

def check_role(required_role):
    """Decorator to check user role."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            username = request.headers.get("X-User")
            if not username or users.get(username) != required_role:
                return jsonify({"error": "Access denied"}), 403
            return func(*args, **kwargs)
        return wrapper
    return decorator

@app.route('/admin-data', methods=['GET'])
@check_role("admin")
def admin_data():
    return jsonify(sensitive_data)

if __name__ == "__main__":
    app.run(debug=True)
```
### **2. AWS IAM Policy for Least Privilege**  
Grant only S3 read access to a specific bucket.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::my-secure-bucket/*"
    }
  ]
}
```

### ** 4. Linux File Permissions **
Limit file access to only the owner.

```bash
# Owner has read and write, others have no access
chmod 600 sensitive_file.txt
```

### ** 5 Limiting Database Access in Code **
Use a database user with restricted privileges.
```c++
#include <iostream>
#include <pqxx/pqxx> // Include the PostgreSQL library

using namespace std;
using namespace pqxx;

int main() {
    try {
        // Connect to the database as a read-only user
        connection conn("dbname=mydb user=readonly_user password=securepassword host=localhost");
        
        if (conn.is_open()) {
            cout << "Connected to the database successfully." << endl;

            // Create a non-transactional object to execute queries
            nontransaction work(conn);

            // Execute SQL query
            result res = work.exec("SELECT * FROM sensitive_data;");

            // Print query results
            for (auto row : res) {
                for (auto field : row) {
                    cout << field.c_str() << " ";
                }
                cout << endl;
            }

            conn.disconnect();
        } else {
            cout << "Failed to connect to the database." << endl;
        }
    } catch (const std::exception &e) {
        cerr << e.what() << endl;
    }

    return 0;
}
```

