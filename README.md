# Dynamic System Plot

## What is a discrete dynamical system?

Dynamical systems are about the evolution of some quantities over time. This evolution can occur smoothly over time or in discrete time steps. Here, we introduce dynamical systems where the state of the system evolves in discrete time steps.

When we model a system as a discrete dynamical system, we imagine that we take a snapshot of the system at a sequence of times. 
The snapshots could occur once a year, once every millisecond, or even irregularly, such as once every time a new government is elected.

When we take these snapshots, the idea is that we are recording whatever variable determine the state of the system: our chosen state variables that evolve through the state space. 
To complete the description of the dynamical system, we need to specify a rule that determines, given an initial snapshot, what the resulting sequence of future snapshots must be.

## Summary

This proyect consists of a script written in Python 3, which uses Matplotlib to plot a simple dynamical system:

x = x² + 1

Running the following initial conditions:

x_1 = 0.1

x_2 = 1

x_3 = 10

## Execution

To execute this project, please run:

bash testing.sh

## Bibliography

https://mathinsight.org/discrete_dynamical_system_introduction
