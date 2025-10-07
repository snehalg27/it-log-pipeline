import os

def read_logs(file_path=None):
    # Automatically build full path no matter where you run from
    if file_path is None:
        base_dir = os.path.dirname(os.path.dirname(__file__))  # Go up from /pipeline/
        file_path = os.path.join(base_dir, "logs", "sample_logs.txt")

    with open(file_path, "r") as f:
        lines = f.readlines()
    return lines


if __name__ == "__main__":
    logs = read_logs()
    print("✅ Extracted Logs:")
    for line in logs:
        print(line.strip())

