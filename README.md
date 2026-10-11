# SIEM — Security Information and Event Management System

## 1. Project Overview

The Security Information and Event Management (SIEM) System is a Python-based security monitoring application designed to analyze system logs, identify suspicious activities, generate security alerts, and create incident reports.

The project demonstrates basic security monitoring and rule-based threat detection using sample log data.

## 2. Objectives

- Analyze logs from simulated systems and servers.
- Identify repeated failed login attempts.
- Detect malware-related events recorded in logs.
- Monitor privilege-change events.
- Classify alerts according to severity.
- Display security information through a dashboard.
- Generate incident reports in CSV format.

## 3. Technologies Used

- **Python** — application logic and threat detection.
- **Pandas** — log processing and data analysis.
- **Streamlit** — interactive security monitoring dashboard.
- **CSV** — sample log storage and incident report generation.
- **Visual Studio Code** — development environment.

## 4. Project Modules

### Log Analysis
Reads sample security logs from a CSV file and processes event timestamps, source systems, usernames, IP addresses, event types, and statuses.

### Threat Detection
Uses rule-based detection to identify:
- Five or more failed login attempts from the same IP address within a five-minute window.
- Malware detection events.
- Privilege-change events.

### Security Dashboard
Displays the total number of events, detected alerts, critical alerts, and high-severity alerts. It also provides event charts and filtering options.

### Incident Reporting
Exports detected security alerts to `incident_report.csv` for further analysis.

## 5. Project Structure

```text
siem-project/
├── .venv/
├── app.py
├── detector.py
├── generate_report.py
├── logs.csv
├── incident_report.csv
└── README.md
```

## 6. How to Run the Project

1. Open the project folder in VS Code.
2. Activate the virtual environment:

   `source .venv/bin/activate`

3. Start the dashboard:

   `streamlit run app.py`

4. Open the local URL displayed in the terminal.

5. To generate an incident report, open another terminal, activate the virtual environment, and run:

   `python generate_report.py`

## 7. Expected Results

The supplied sample data is designed to produce three alerts:

- **High:** Repeated Failed Logins.
- **Critical:** Malware Detection Event.
- **Medium:** Privilege Change.

The dashboard displays the alerts, and the report generator saves them to a CSV file.

## 8. Limitations and Future Enhancements

- The current implementation uses sample CSV logs rather than live logs from real servers.
- Detection is based on predefined rules, not machine learning.
- Future versions could support live log ingestion, additional detection rules, alert notifications, authentication, and integration with multiple log sources.

## 9. Conclusion

This project demonstrates the fundamentals of log analysis, rule-based threat detection, security event monitoring, and incident reporting through a Python-based SIEM prototype.