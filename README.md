# Description
This repository is a comprehensive collection of essential concepts and algorithms that form the foundation of reinforcement learning (RL). Whether you're a beginner seeking a solid understanding of RL or an experienced practitioner looking to refresh your knowledge, this repository serves as a valuable resource.

Key Features:

- **Tree-Search Algorithm**: Dive into tree search techniques, which form an integral part of RL. Explore algorithms like Backtracking Search, and variants such as Dynamic Programming (DP) to efficiently explore and exploit the state-action space.

- **Policy Evaluation**: Gain a deep understanding of policy evaluation methods that enable agents to assess the quality of their actions and optimize their decision-making processes. Explore algorithms like iterative policy evaluation to estimate the value function of a given policy.

- **Value Iteration**: Delve into the world of value iteration algorithms, a powerful family of methods for solving Markov Decision Processes (MDPs). Learn how to compute the optimal value function by iteratively updating the value estimates for each state based on the Bellman equation.

- **Temporal Difference Learning**: Discover one of the most popular and widely used reinforcement learning algorithms, Q-learning. Uncover the principles behind temporal difference learning, where agents learn to maximize their long-term rewards by estimating the action-value function (Q-values). Explore techniques such as epsilon-greedy exploration and experience replay for efficient learning.

Each algorithm and concept within the repository is accompanied by explanations, pseudocode, and implementation examples in Python. This ensures that learners can grasp the underlying theory while also gaining hands-on experience with practical implementations.

Additionally, the repository provides a curated selection of supplementary resources such as online tutorials, to further deepen your understanding and keep you up-to-date with the latest advancements in RL.

Whether you are an academic researcher, a student, or an industry practitioner, the Reinforcement Learning Fundamentals repository equips you with the necessary knowledge and tools to master the fundamental concepts and algorithms of RL and apply them to a wide range of real-world problems. Start your journey into the fascinating world of RL today!


# Get start
Inside the repository execute the following commands:
```
python3 -m venv venv
source venv/bin/activate
```

Install the necessary packages using the command below:

```
pip install -e .
```

To test some examples run:
```
python get_start.py
```

## Mujoco (***under development***)
The primary focus of this repository is to implement reinforcement learning algorithms using various engines such as Mujoco and Unity3D.

Simulating, rendering, and controlling objects in Mujoco presents some challenges and complexities.

The simulation application is written in C/C++, but there are limitations when working with Mujoco in Python.

To address this, I have created a script for this repository that handles the process of simulating and controlling objects using the Mujoco and GLFW libraries. Currently, the simulation can be executed successfully, but the controlling functionality is still a work in progress.

To run the simulation, navigate to the 'src/envs/mujoco' directory and execute the following command:

```
python box.py
```

it will display a interactive window such as ilustrated in figure bellow.

![Box simulation](/images/box.png)

References are in the script.
