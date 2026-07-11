import json
from pathlib import Path


def test_report_exists():
    """The agent produced a report file."""
    assert Path("/app/report.json").exists(), "no report.json found"


def test_report_schema():
    """report.json contains the required keys."""
    data = json.loads(Path("/app/report.json").read_text())
    assert {"total_requests", "unique_ips", "top_path"} <= data.keys()
