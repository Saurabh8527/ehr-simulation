import random
import time


def retry(operation, retries=5, initial_delay=2, backoff_factor=2, max_jitter=1):
    """Retry wrapper for operations that might fail with exponential backoff and jitter."""
    delay = initial_delay
    for attempt in range(1, retries + 1):
        try:
            return operation()
        except Exception as e:
            print(f"Attempt {attempt} failed with error: {e}")
            if attempt < retries:
                jitter = random.uniform(0, max_jitter)
                final_delay = delay + jitter
                print(f"Retrying in {final_delay} seconds...")
                time.sleep(final_delay)
                delay *= backoff_factor
            else:
                raise


def simulate_error(error_chance=0.1):
    if random.random() < error_chance:
        raise Exception("Simulated error")
