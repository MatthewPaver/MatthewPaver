# Voting Application

This project implements a distributed voting application using Java Remote Method Invocation (RMI). Clients can connect to the server, cast votes among 3 choices, and then request the voting results. The system uses a ticketing mechanism to ensure that only voting clients can view the voting results.

## Structure
The project consists of the following main components:

- `CastVote.java`: The remote interface defines the methods available for remote invocation.
- `VoteImpl.java`: The implementation of the CastVote interface, handling the voting logic.
- `Server.java`: Sets up the RMI environment, creates an instance of VoteImpl, and registers it with the RMI registry.
- `Client.java`: Connects to the RMI server, requests a voting ticket, submits votes, and retrieves voting results.

## Compilation
1. Navigate to the `server` directory.
2. Compile the server-side classes:

 ```bash
   javac Server.java VoteImpl.java CastVote.java
```
  1. Navigate to the client directory.
  2. Compile the client-side class:
  ```bash
   javac Client.java CastVote.java
```
## Running the Application

1. Start the RMI Registry
2. First, start the RMI registry in a separate terminal window:
  ```bash
   rmiregistry
```
## Start the Server
1. Navigate to the server directory.
2. Run the server:
  ```bash
   java Server
```
## Run the Client
1. Open a new terminal window.
2. Navigate to the client directory.
3. Run the client:
  ```bash
   java Server
```

Follow the prompts in the client application to vote and view the voting results.
