import zmq


# Set up environment and sockets
context = zmq.Context()
print("Client attempting to connect to server...")
socket = context.socket(zmq.REQ)

# Connect to server socket
socket.connect("tcp://localhost:5556")

# Setup request for weather_state service
request = {"service_key": "weather_state"}

# Send Request
print("Sending Request...")
socket.send_json(request)

# Get the reply
response = socket.recv_json()

# Print response
print("Received response from server:")
print(response)

# Setup request for list_weather_states service
request = {
    "service_key": "list_weather_states",
    "list_length": 10
}

# Send Request
print("Sending Request...")
socket.send_json(request)

# Get the reply
response = socket.recv_json()

# Print response
print("Received response from server:")
print(response)
