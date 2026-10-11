
# SENTINEL — SIEM System

## 1. Project Overview

SENTINEL is a Python-based Security Information and Event Management (SIEM) prototype. It analyzes security logs, identifies suspicious activities, generates alerts, and presents security information through an interactive dashboard.

## 2. Objectives

- Collect and analyze sample security logs.
- Detect repeated failed login attempts.
- Identify malware detection events.
- Monitor privilege changes.
- Generate incident reports.
- Visualize events and alerts using a dashboard.

## 3. Technologies Used

- Python
- Pandas
- Streamlit
- CSV
- Git and GitHub

## 4. Project Structure

```text
siem-security-monitor/
├── app.py
├── detector.py
├── generate_report.py
├── test_detector.py
├── logs.csv
├── incident_report.csv
├── README.md
└── .gitignore
```

## 5. Detection Rules

| Threat | Detection rule | Severity |
|---|---|---|
| Repeated Failed Logins | Five or more failed logins from one IP within five minutes | High |
| Malware Detection | A malware detection event in the logs | Critical |
| Privilege Change | A privilege change event in the logs | Medium |

## 6. Installation

Install Python 3 and open a terminal in the project directory.

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install streamlit==1.41.1 pandas==2.2.3
```

## 7. Running the Dashboard

```bash
streamlit run app.py
```

## 8. Generating an Incident Report

```bash
python generate_report.py
```

The report is saved as `incident_report.csv`.

## 9. Running Automated Tests

```bash
python test_detector.py
```

The tests check repeated failed login detection, malware detection, and privilege change detection.

## 10. Dashboard Features

- Security event summary
- Alert severity charts
- Threat detection results
- Searchable log explorer
- Incident details and investigation priorities
- CSV export options

## 11. Limitations and Future Enhancements

This prototype currently analyzes sample CSV logs. It is not connected to live servers and does not provide enterprise-grade real-time monitoring.

Future enhancements include live log ingestion, additional detection rules, alert notifications, user authentication, and database integration.

## 12. Conclusion

SENTINEL demonstrates the fundamental workflow of a SIEM system: log analysis, threat detection, alert generation, incident reporting, and security monitoring.
