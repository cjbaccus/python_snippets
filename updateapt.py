import subprocess


def check_for_updates():
    try:
        result = subprocess.run(
            ["sudo", "apt-get", "update"], check=True, text=True, capture_output=True
        )
        print("Update check completed:\n", result.stdout)
    except subprocess.CalledProcessError:
        print("Failed to check for updates.")


def apply_updates():
    try:
        subprocess.run(["sudo", "apt-get", "upgrade", "-y"], check=True)
        print("System updates applied successfully.")
    except subprocess.CalledProcessError:
        print("Failed to apply updates.")


# Example usage
check_for_updates()
apply_updates()
