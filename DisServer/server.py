import socket
import threading
import json
from queue import Queue

# Dictionary data (sample)
dictionary = {
    "hello": ["used as a greeting"],
    "world": ["the earth and all people and things on it"],
    "python": ["a large constricting snake found in tropical and subtropical regions"],
    "algorithm": ["a step-by-step procedure or set of rules for solving a problem or accomplishing a task"],
    "database": ["an organized collection of structured information or data, typically stored electronically in a computer system"],
    "framework": ["a basic structure underlying a system, concept, or text"],
    "encryption": ["the process of converting information or data into a code, especially to prevent unauthorized access"],
    "artificial intelligence": ["the theory and development of computer systems capable of performing tasks that typically require human intelligence"],
    "machine learning": ["a subset of artificial intelligence that focuses on the development of algorithms and statistical models that enable computers to learn and improve from experience"],
    "big data": ["extremely large datasets that may be analyzed computationally to reveal patterns, trends, and associations, especially relating to human behavior and interactions"],
    "cloud computing": ["the delivery of computing services, including servers, storage, databases, networking, software, and analytics, over the internet (the cloud) to offer faster innovation, flexible resources, and economies of scale"],
    "cybersecurity": ["the practice of protecting computer systems, networks, and data from digital attacks, unauthorized access, and other cyber threats"]
}

# Task queue
task_queue = Queue()

def handle_client(client_socket):
    try:
        # Receive request from client
        request_data = client_socket.recv(1024).decode()
        request = json.loads(request_data)

        # Process request
        if request["type"] == "query":
            word = request["word"]
            if word in dictionary:
                response = {
                    "type": "response",
                    "status": "success",
                    "meanings": dictionary[word]
                }
            else:
                response = {
                    "type": "response",
                    "status": "error",
                    "message": "Word not found"
                }
            client_socket.send(json.dumps(response).encode())
    except Exception as e:
        print("Error:", e)
    finally:
        client_socket.close()

def worker():
    while True:
        client_socket = task_queue.get()
        handle_client(client_socket)
        task_queue.task_done()

def start_server(port, num_workers):
    # Start worker threads
    for _ in range(num_workers):
        worker_thread = threading.Thread(target=worker)
        worker_thread.daemon = True
        worker_thread.start()

    # Start server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', port))
    server_socket.listen(5)
    print("Server listening on port", port)

    while True:
        client_socket, _ = server_socket.accept()
        task_queue.put(client_socket)

if __name__ == "__main__":
    PORT = 8080
    NUM_WORKERS = 5
    start_server(PORT, NUM_WORKERS)
