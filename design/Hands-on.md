# Case Study: Remote Patient Monitoring System

### Overview:
The healthcare industry is increasingly adopting remote patient monitoring solutions to provide better care for patients outside traditional clinical settings. This case study focuses on designing a secure system for monitoring patients' health vitals using wearable sensors, cloud-based storage, and a web-based interface for clinicians.

---

### System Components:
1. **Wearable Sensor Device:**  
   - Continuously captures patient health data such as heart rate, blood pressure, and activity levels.  
   - Communicates with the mobile app via Bluetooth.  
   - Sends encrypted data packets to maintain confidentiality.  

2. **Mobile Application:**  
   - Installed on the patient's smartphone.  
   - Receives data from the wearable sensor.  
   - Displays real-time vitals to the patient.  
   - Transmits data securely to the cloud over HTTPS.  
   - Provides alerts for abnormal health readings.  

3. **Cloud Storage Service:**  
   - Securely stores patient health data for analysis and reporting.  
   - Enforces data encryption at rest and during transmission.  
   - Ensures regulatory compliance (e.g., HIPAA, GDPR).  

4. **Admin Interface for Clinicians (Web Application):**  
   - Allows clinicians to view, analyze, and manage patient data remotely.  
   - Provides dashboards for visualizing patient trends.  
   - Supports role-based access control for data privacy.  
   - Maintains audit logs for tracking access to patient information.  

---

### Data Flow:
1. **Wearable Sensor → Mobile App:**  
   - Sensor securely connects to the mobile app via Bluetooth.  
   - Data is transmitted in encrypted format using AES (Advanced Encryption Standard).  

2. **Mobile App → Cloud Storage:**  
   - Patient data is transmitted over a secure HTTPS connection.  
   - Authentication via API keys ensures only authorized requests.  

3. **Cloud Storage → Admin Interface:**  
   - Clinicians access data via the secure web application.  
   - Role-based access control restricts access to authorized personnel.  

---


### Security Requirements:
- **Confidentiality:** Protect sensitive patient data using encryption and access control mechanisms.  
- **Integrity:** Ensure data is not tampered with during transmission or storage.  
- **Availability:** Maintain system uptime to provide continuous monitoring for patients.  
- **Authentication:** Ensure only authorized users and devices can access the system.  
- **Authorization:** Implement RBAC to limit user permissions based on roles.  

---

### Regulatory Considerations:
- **HIPAA (Health Insurance Portability and Accountability Act):** For handling patient health information in the U.S.  
- **GDPR (General Data Protection Regulation):** For protecting patient data in the EU.  
- **FDA Guidelines:** For secure software in medical devices.  

This case study forms the foundation for participants to identify security risks, apply secure design principles, and develop effective mitigation strategies during the group activity.

## Deliverable 
### 1. Threat Modeling and Risk Identification 
- Each group creates a data flow diagram (DFD) for the system.
- Identify threats using the STRIDE methodology (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege).
### 2. Prioritization and Mitigation 
- Prioritize threats based on their impact and likelihood.
- Develop mitigation strategies aligned with secure design principles.
- Document design choices (e.g., encrypting patient data, implementing multi-factor authentication).
