import zmq
import json
import time
import random


# Environment and socket initialization
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")
print("Server running")

# Possible Weather States
WEATHER_STATES = [
    "Clear",
    "Foggy",
    "Rainy",
    "Stormy",
    "Snowy",
    "Cloudy",
    "Sunny"
]

try:
    while True:
        # Receive Message
        message = socket.recv_string()
        print(f"Received request: {message}")
        try:
            request = json.loads(message)
        except json.JSONDecodeError:
            socket.send_json({"error": "Invalid JSON"})
            continue

        response = {}

        # Route Request
        service_key = request.get("service_key")
        if not service_key:
            response = {"error": "Missing service key"}

        elif service_key == "weather_state":
            response = {"weather_state": random.choice(WEATHER_STATES)}

        elif service_key == "list_weather_states":
            # Unpack requested list length
            length = request.get("list_length")

            if not isinstance(length, int) or length <= 0:
                response = {
                    "error": "Length of list must be an integer and greater than 0"
                }
            else:
                response = {
                    "weather_list": random.choices(WEATHER_STATES, k=length)
                }

        else:
            response = {"error": f"Unknown service_key: {service_key}"}

        time.sleep(0.5)
        print(f"sending response: {response}")
        socket.send_json(response)

except KeyboardInterrupt:
    print("Server shutting down...")

finally:
    socket.close()
    context.term()
    print("Exit confirmed")
