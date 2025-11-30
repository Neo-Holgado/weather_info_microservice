# Weather Information Microservice
### A Python-based microservice with multiple services:  
`weather_state`: Returns a random weather state  
`list_weather_states`: Returns a list of multiple random weather states

## Using the `weather_state` service  
### REQUEST Format  
To use the weather_state service, you need to send a JSON-formatted message to the server, which includes:  
1. `service_key`: identifies which service to use.  For this service, use "weather_state"  

### Example Format  
```python  
message = {"service_key": "weather_state"}
```
### Sending the Request (Local Server)  
```python  
import zmq


# Connect to server
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5556")

# Send the request
socket.send_json(message)
```
### Response Format  
The response is formatted as follows:  
```python
response = {"weather_state": "Rainy"}
```

### Receiving the Response  
```python
response = socket.recv_json()
print("Received response from server:")
print(response)
```

### All Possible weather states  
1. Clear
2. Foggy
3. Rainy
4. Stormy
5. Snowy
6. Cloudy
7. Sunny

## Using the `list_weather_states` service
### REQUEST Format
To use the weather_state service, you need to send a JSON-formatted message to the server, which includes:  
1. `service_key`: Identifies which service to use.  For this service, use "list_weather_states"
2. `list_length`: Integer which describes the length of the random weather state list

### Example Format
```python
message = {
  "service_key": "list_weather_states",
  "list_length": 5
}
```

### Sending the Request (Local Server)  
```python  
import zmq


# Connect to server
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5556")

# Send the request
socket.send_json(message)
```
### Response Format  
The response is formatted as follows:  
```python
response = {"weather_list": ["Sunny", "Stormy", "Clear", "Snowy", "Snowy"]}
```

### Receiving the Response  
```python
response = socket.recv_json()
print("Received response from server:")
print(response)
```

## Author
Neo Holgado

## Tech Stack
- Python
- ZeroMQ (pyzmq) - Microservice communication
