import subprocess
import time
import os
import signal

# Define the name of the main script
MAIN_SCRIPT = 'main.py'
PID_FILE = 'main.pid'

def start_script():
    """Start the main script and save its PID."""
    print("Starting main.py...")
    process = subprocess.Popen(['python', MAIN_SCRIPT])
    with open(PID_FILE, 'w') as f:
        f.write(str(process.pid))
    return process

def stop_script():
    """Stop the main script if it is running."""
    if os.path.exists(PID_FILE):
        with open(PID_FILE, 'r') as f:
            pid = int(f.read().strip())
        try:
            os.kill(pid, signal.SIGTERM)  # Send SIGTERM to the process
            print(f"Stopped main.py with PID {pid}.")
        except ProcessLookupError:
            print(f"No process found with PID {pid}.")
        except Exception as e:
            print(f"Error stopping main.py: {e}")
        finally:
            os.remove(PID_FILE)  # Remove the PID file

def run_script():
    while True:
        stop_script()  # Stop the currently running instance
        time.sleep(2)  # Wait for 2 seconds before starting again
        start_script()  # Start the main script
        print("main.py has started. Restarting in 2 minutes...")
        time.sleep(1800)  # Sleep for 30 minutes (1800 seconds)

if __name__ == "__main__":
    run_script()