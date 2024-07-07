from functools import wraps
from queue import Queue
from random import uniform
from threading import Thread, Event
from time import sleep

def interrupt_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt as e:
            print(e)
            return "Interrupted"
    return inner

# Create a queue for requests
queue = Queue()
stop_event = Event()

@interrupt_error
def generate_request() -> None:
    """
    Generates a request and adds it to the queue.
    """
    request_id = 0

    while not stop_event.is_set():
        request_id += 1
        request = f"Request {request_id}"
        queue.put(request)
        print(f"Created: {request}")
        sleep(uniform(1, 3))  # simulation of request generation time

@interrupt_error
def process_request() -> None:
    """
    Process requests from a queue.
    """
    while not stop_event.is_set():
        if not queue.empty():
            current_request = queue.get()
            print(f"Processing: {current_request}")
            sleep(uniform(1, 3))  # simulation of request processing time
            print(f"Completed: {current_request}")
            queue.task_done()
        else:
            print("Queue is empty. Waiting for requests...")
            sleep(1)  # Delay to avoid busy waiting
     
def main() -> None:
    generator_thread = Thread(target=generate_request)
    processor_thread = Thread(target=process_request)

    generator_thread.start()
    processor_thread.start()

    try:
        generator_thread.join()
        processor_thread.join()
    except KeyboardInterrupt:
        print("Interrupt received, stopping threads...")
        stop_event.set()
        generator_thread.join()
        processor_thread.join()
        print("Threads stopped. Exiting.")
    
if __name__ == "__main__":
    main()