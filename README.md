# Console Chat with Python

## Description

This project implements a basic console chat system that allows communication between two clients through a server, using Python and sockets. The server acts as an intermediary, receiving messages from one client and forwarding them to the other, thus enabling bidirectional real-time communication within the same network.

## Features

- **Real-Time Communication:** Messages are sent and received in real-time between clients.
- **Support for Multiple Clients:** Although primarily designed for two clients, the server can be easily adapted to support multiple connections.
- **Ease of Use:** Simple console user interface for easy interaction.
- **Flexible Configuration:** Ability to configure the server's IP address and port for execution in different network environments.

## Requirements

Python 3.6 or higher.

## Installation

Clone this repository to your local machine using:

```bash
git clone https://github.com/smezag/LocalNetChat.git
````
## Usage

To use this chat system, you'll need to start both the server and the clients.

### Starting the Server

Navigate to the project folder and run the following command in the console:

```bash
python server.py
````

### Starting the Client

Open a new console for each client, navigate to the project folder, and execute:

```bash
python client.py
````

Follow the on-screen instructions to connect to the server and start chatting

### Important Configuration Note:

Before starting the client, you must update the client.py file to use the IP address of the machine running server.py. Locate the line in client.py where the connection is established 

```` python
def start_client(server_host='127.0.0.1', server_port=12345): 
````

and replace server_host with the server machine's IP address.

This ensures that your client knows where to send and receive messages from. If you're not sure how to find your server's IP address, you can usually find it by running ipconfig (on Windows) or ifconfig (on Linux/Mac) in your terminal.

Follow the on-screen instructions to connect to the server and start chatting.

## Contributions

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make will be **greatly appreciated**.

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License

Distributed under the MIT License. See `LICENSE` file for more information.

## Contact

[Sergio Meza] - serangu18@gmail.com

Project Link: [https://github.com/semezag/LocalNetChat](https://github.com/smezag/LocalNetChat)
