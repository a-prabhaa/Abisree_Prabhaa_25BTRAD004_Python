# Log File Reader Program
# Function to analyze log file
def read_log_file(filename):
    # Initialize counters
    error_count = 0
    warning_count = 0
    info_count = 0
    try:
        # Open the log file in read mode
        with open(filename, "r") as file:
            lines = file.readlines()
            # Check whether file is empty
            if not lines:
                print("The log file is empty.")
                return
            # Read each line
            for line in lines:
 if "ERROR" in line:
                    error_count += 1
                elif "WARNING" in line:
                    warning_count += 1
                elif "INFO" in line:
                    info_count += 1
        # Display summary
        print("\n--- Log File Analysis ---")
        print("Total Log Entries:", len(lines))
        print("ERROR occurrences:", error_count)
        print("WARNING occurrences:", warning_count)
        print("INFO occurrences:", info_count)
    except FileNotFoundError:
        print("Error: Log file not found!")
    except PermissionError:
        print("Error: Permission denied to read the file!")
# Creating a sample log file
sample_logs = """INFO: Application started successfully.
ERROR: Database connection failed.
WARNING: Memory usage is high.
INFO: User logged in.
ERROR: Invalid password.
INFO: Data saved successfully.
WARNING: Disk space is low.
ERROR: Server connection lost.
"""
with open("application.log", "w") as file:
    file.write(sample_logs)
# Calling the function
read_log_file("application.log")
