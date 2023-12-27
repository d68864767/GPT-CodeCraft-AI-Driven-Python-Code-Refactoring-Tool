```python
import traceback

def handle_error(e):
    """
    This function handles any exceptions that occur during the execution of the GPT-CodeCraft script.
    It prints a user-friendly error message and logs the full error details for debugging purposes.

    Parameters:
    e (Exception): The exception to handle.
    """

    # Print a user-friendly error message
    print("An error occurred while processing your code. Please check the error log for more details.")

    # Log the full error details for debugging purposes
    log_error(e)

def log_error(e):
    """
    This function logs the full details of an exception for debugging purposes.
    It writes the error details to a log file named 'error_log.txt'.

    Parameters:
    e (Exception): The exception to log.
    """

    # Get the full traceback of the exception
    error_details = traceback.format_exc()

    # Write the error details to the log file
    with open('error_log.txt', 'a') as f:
        f.write(error_details)
```
