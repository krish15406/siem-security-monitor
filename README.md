
# SENTINEL — SIEM System

## 1. Project Overview

SENTINEL is a Python-based Security Information and Event Management (SIEM) prototype. It analyzes sample security logs, detects suspicious activities, generates security alerts, and creates incident reports through an interactive dashboard.

## 2. Objectives

- Analyze security logs from simulated systems.
- Detect repeated failed login attempts.
- Identify malware detection events.
- Monitor privilege-change events.
- Classify alerts by severity.
- Display security information through a dashboard.
- Generate downloadable incident reports.
- Test threat detection rules using automated tests.

## 3. Technologies Used

- **Python** — application logic and threat detection.
- **Pandas** — log processing and data analysis.
- **Streamlit** — interactive dashboard.
- **CSV** — sample log storage and incident reports.
- **Git and GitHub** — version control and project hosting.

## 4. Project Modules

### Log Analysis
Reads sample security logs from a CSV file and processes timestamps, source systems, usernames, IP addresses, event types, and statuses.

### Threat Detection
Uses predefined rules to detect:
- Five or more failed login attempts from the same IP address within a five-minute window.
- Malware detection events.
- Privilege-change events.

### Security Dashboard
Displays event totals, security alerts, severity charts, searchable logs, and incident details.

### Incident Reporting
Exports detected security alerts to `incident_report.csv`.

### Automated Testing
Uses `test_detector.py` to test repeated failed logins, malware detection, and privilege-change detection.

## 5. Project Structure

```text
siem-project/
├── app.py
├── detector.py
├── generate_report.py
├── test_detector.py
├── logs.csv
├── incident_report.csv
├── README.md
├── requirements.txt
└── .gitignore
```


## 6. Installation

### Prerequisites

- Python 3 installed
- Git installed (optional if downloading the ZIP)

### Setup

Clone the repository:

```bash
git clone https://github.com/krish15406/siem-security-monitor.git
cd siem-security-monitor
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

On Windows, activate it using:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```


## 7. Running the Dashboard

Run:

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal.

## 8. Generating an Incident Report

Run:

```bash
python generate_report.py
```

The generated report is saved as `incident_report.csv`.

## 9. Running Automated Tests

Run:

```bash
python test_detector.py
```

The tests verify the three implemented detection rules. The expected output includes three PASS messages and `All tests passed!`.

## 10. Expected Results

The supplied sample data produces three expected alert types:

| Threat | Severity |
|---|---|
| Repeated Failed Logins | High |
| Malware Detection Event | Critical |
| Privilege Change | Medium |

## 11. Limitations and Future Enhancements

This project is a prototype that uses sample CSV logs. It is not connected to live servers and does not provide enterprise-grade real-time monitoring.

Possible future enhancements include:
- Live log ingestion from multiple systems.
- Additional threat detection rules.
- Automated alert notifications.
- Database integration.
- User authentication and access control.

## 12. Conclusion

SENTINEL demonstrates the fundamental workflow of a SIEM system: log analysis, rule-based threat detection, security monitoring, alert generation, and incident reporting.
