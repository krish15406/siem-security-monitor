from pathlib import Path

import pandas as pd
import streamlit as st

from detector import detect_threats


# Dashboard configuration
st.set_page_config(
	page_title="SIEM Security Monitor",
	page_icon="🛡️",
	layout="wide",
)

st.title("🛡️ SIEM Security Monitoring System")
st.write(
	"Log Analysis | Threat Detection | Security Monitoring"
)

# Load and process the sample logs
log_file = Path(__file__).parent / "logs.csv"

try:
	logs = pd.read_csv(log_file)

	required_columns = {
		"timestamp", "source", "username",
		"src_ip", "event_type", "status",
	}

	missing = required_columns - set(logs.columns)

	if missing:
		st.error(f"Missing log columns: {sorted(missing)}")
		st.stop()

	logs["timestamp"] = pd.to_datetime(
		logs["timestamp"], errors="coerce"
	)
	logs = logs.dropna(subset=["timestamp"])

	alerts = detect_threats(logs)

except (OSError, ValueError, KeyError) as error:
	st.error(f"Could not process security logs: {error}")
	st.stop()


# Summary metrics
st.subheader("Security Overview")

total_events = len(logs)
total_alerts = len(alerts)

critical_count = (
	int((alerts["severity"] == "Critical").sum())
	if not alerts.empty else 0
)

high_count = (
	int((alerts["severity"] == "High").sum())
	if not alerts.empty else 0
)

medium_count = (
	int((alerts["severity"] == "Medium").sum())
	if not alerts.empty else 0
)

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Events", total_events)
c2.metric("Total Alerts", total_alerts)
c3.metric("Critical Alerts", critical_count)
c4.metric("High Alerts", high_count)


# Event charts
st.divider()
left, right = st.columns(2)

with left:
	st.subheader("Events by Source")
	st.bar_chart(logs["source"].value_counts())

with right:
	st.subheader("Alerts by Severity")

	if not alerts.empty:
		st.bar_chart(alerts["severity"].value_counts())
	else:
		st.info("No alerts detected.")


# Log explorer
st.divider()
st.subheader("Security Event Explorer")

sources = sorted(logs["source"].unique().tolist())

selected_sources = st.multiselect(
	"Filter by source system",
	options=sources,
	default=sources,
)

filtered_logs = logs[
	logs["source"].isin(selected_sources)
]

st.dataframe(
	filtered_logs,
	use_container_width=True,
	hide_index=True,
)


# Alert explorer and incident report
st.divider()
st.subheader("Detected Security Alerts")

if alerts.empty:
	st.success("No alerts triggered by the current rules.")
else:
	severities = ["Critical", "High", "Medium"]

	selected_severities = st.multiselect(
		"Filter by severity",
		options=severities,
		default=severities,
	)

	filtered_alerts = alerts[
		alerts["severity"].isin(selected_severities)
	]

	st.dataframe(
		filtered_alerts,
		use_container_width=True,
		hide_index=True,
	)

	report = filtered_alerts.to_csv(index=False).encode("utf-8")

	st.download_button(
		label="Download Incident Report (CSV)",
		data=report,
		file_name="siem_incident_report.csv",
		mime="text/csv",
	)

st.caption(
	"Educational prototype using synthetic logs and "
	"rule-based threat detection."
)
