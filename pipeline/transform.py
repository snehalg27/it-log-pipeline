import re
import pandas as pd
from extract import read_logs

def transform_logs(log_lines):
    """
    Transform raw log lines into a structured DataFrame
    """
    pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)"
    data = []

    for line in log_lines:
        match = re.match(pattern, line.strip())
        if match:
            timestamp, level, message = match.groups()
            # Split component and message if possible
            if " " in message:
                parts = message.split(" ", 1)
                component = parts[0]
                msg = parts[1]
            else:
                component = "General"
                msg = message
            data.append((timestamp, level, component, msg))

    df = pd.DataFrame(data, columns=["timestamp", "level", "component", "message"])
    return df


if __name__ == "__main__":
    logs = read_logs()
    df = transform_logs(logs)
    print("✅ Transformed Logs:")
    print(df)

