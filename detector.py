
import pandas as pd


def detect_threats(logs):
    alerts = []

    required_columns = {
        "timestamp",
        "source",
        "username",
        "src_ip",
        "event_type",
        "status",
    }

    missing_columns = required_columns - set(logs.columns)
    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )

    logs = logs.copy()
    logs["timestamp"] = pd.to_datetime(
        logs["timestamp"], errors="coerce"
    )
    logs = logs.dropna(subset=["timestamp"])

    failed = logs[
        (logs["event_type"] == "login")
        & (logs["status"] == "failed")
    ].sort_values("timestamp")

    # Detect 5 failed logins within any 5-minute window.
    for ip, events in failed.groupby("src_ip"):
        events = events.reset_index(drop=True)

        for i in range(len(events)):
            start = events.loc[i, "timestamp"]
            end = start + pd.Timedelta(minutes=5)

            window = events[
                (events["timestamp"] >= start)
                & (events["timestamp"] <= end)
            ]

            if len(window) >= 5:
                alerts.append({
                    "timestamp": end,
                    "src_ip": ip,
                    "threat": "Repeated Failed Logins",
                    "severity": "High",
                    "count": len(window),
                    "details": (
                        f"{len(window)} failed logins from {ip} "
                        "within a 5-minute window"
                    ),
                })
                break

    malware = logs[logs["event_type"] == "malware_detected"]

    for _, event in malware.iterrows():
        alerts.append({
            "timestamp": event["timestamp"],
            "src_ip": event["src_ip"],
            "threat": "Malware Detection Event",
            "severity": "Critical",
            "count": 1,
            "details": f"Malware event reported by {event['source']}",
        })

    privilege = logs[logs["event_type"] == "privilege_change"]

    for _, event in privilege.iterrows():
        alerts.append({
            "timestamp": event["timestamp"],
            "src_ip": event["src_ip"],
            "threat": "Privilege Change",
            "severity": "Medium",
            "count": 1,
            "details": (
                f"Privilege change recorded for {event['username']}"
            ),
        })

    return pd.DataFrame(
        alerts,
        columns=[
            "timestamp",
            "src_ip",
            "threat",
            "severity",
            "count",
            "details",
        ],
    )
