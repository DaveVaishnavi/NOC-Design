# Algorithm Design

The NOC design solution utilizes a combination of approaches to optimize the network architecture. 

## Latency and Bandwidth Measurement
The first step involves measuring the average latency and bandwidth using the provided interface monitor output. The pseudocode efficiently iterates through the monitor output, calculates latency for read transactions, and accumulates bandwidth for write transactions.

## Reinforcement Learning (RL) Optimization
To iteratively optimize NOC parameters, a reinforcement learning framework is employed. The RL agent interacts with the environment, adjusting parameters such as buffer sizes and arbiter weights to maximize performance while adhering to power constraints. The Deep Q-Network (DQN) algorithm is chosen for its ability to handle high-dimensional state spaces and efficiently explore parameter space.

