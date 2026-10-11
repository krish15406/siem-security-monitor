
import pandas as pd
from pathlib import Path
from detector import detect_threats

# Find the project folder
project_folder = Path(__file__).parent

# Read security logs
logs = pd.read_csv(project_folder / "logs.csv")

# Detect suspicious events
alerts = detect_threats(logs)

# Save the incident report
report_path = project_folder / "incident_report.csv"
alerts.to_csv(report_path, index=False)

print("SIEM Incident Report Generated Successfully!")
print(f"Total alerts: {len(alerts)}")
print(f"Report saved to: {report_path}")
print()
print(alerts.to_string(index=False))
