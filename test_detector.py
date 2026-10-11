
import pandas as pd
from detector import detect_threats


def test_repeated_failed_logins():
    logs = pd.DataFrame([
        {
            "timestamp": f"2026-10-11 10:0{i}:00",
            "source": "test-server",
            "username": "test-user",
            "src_ip": "192.0.2.50",
            "event_type": "login",
            "status": "failed",
        }
        for i in range(5)
    ])

    alerts = detect_threats(logs)

    assert "Repeated Failed Logins" in alerts["threat"].values
    print("PASS: Repeated failed login detection")


def test_malware_detection():
    logs = pd.DataFrame([{
        "timestamp": "2026-10-11 10:00:00",
        "source": "test-server",
        "username": "test-user",
        "src_ip": "192.0.2.60",
        "event_type": "malware_detected",
        "status": "detected",
    }])

    alerts = detect_threats(logs)

    assert "Malware Detection Event" in alerts["threat"].values
    print("PASS: Malware detection")


def test_privilege_change():
    logs = pd.DataFrame([{
        "timestamp": "2026-10-11 10:00:00",
        "source": "test-server",
        "username": "admin",
        "src_ip": "192.0.2.70",
        "event_type": "privilege_change",
        "status": "success",
    }])

    alerts = detect_threats(logs)

    assert "Privilege Change" in alerts["threat"].values
    print("PASS: Privilege change detection")


if __name__ == "__main__":
    test_repeated_failed_logins()
    test_malware_detection()
    test_privilege_change()
    print("\nAll tests passed!")

