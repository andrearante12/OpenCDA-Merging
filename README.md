# OpenCDA-Merging

A fork of the OpenCDA repo  [original documentation](BASE_README.md) that contains custom Co-Simulation scenarios running CARLA and SUMO integrated with OpenCDA.


### Users Guide
* [Installation](#Installation)
* [Creating a Custom Scenario](#Creating-a-Custom-Scenario)


### Scenarios (SUMO/CARLA)
* [Highway Ramp Merging](#highway-ramp-merging)


# Installation

TODO: Installation instructions

# Creating a Custom Scenario

TODO: Instructions

# Scenarios Descriptions

## Highway Ramp Merging

<video width="640" height="360" controls>
  <source src=".\docs\videos\Highway_Merging.mp4" type="video/mp4" alt="https://github.com/andrearante12/OpenCDA-Merging/blob/main/docs/videos/Highway_Merging.mp4">
  Your browser does not support the video tag.
</video>

Link to video of scenario: [docs\videos\Highway_Merging.mp4](docs\videos\Highway_Merging.mp4)

Here we can see an example scenario of an ego vehicle attempting to merge onto a busy freeway. 

## Important Files that Describe the Simulation - [link to official docs](https://opencda-documentation.readthedocs.io/en/latest/md_files/logic_flow.html)

## 1. SUMO Simulation (merging.rou.xml)

SUMO is utilized to generate the background traffic described by this file

[opencda\assets\Merging\Merging.rou.xml](opencda\assets\Merging\Merging.rou.xml)

## 2. Simulation Server Configuration (merging.yaml)

The user has to first write a yaml file to configure the settings of simulation server (e.g. sync mode vs async mode), the specifications of the traffic flow (e.g. the number of human drive vehicles, spawn positions), and the parameters of each Connected Automated Vehicle (e.g. lidar parameters, detection model, trajectory smoothness).


[opencda\scenario_testing\config_yaml\merging.yaml](opencda\scenario_testing\config_yaml\merging.yaml)

## 3. OpenCDA Integration (merging.py)

This python script is the main entryway to the scenario. In order to run the simulation you must run this script. 

[opencda\scenario_testing\merging.py](opencda\scenario_testing\merging.py)



## Town6 Relevant Edges

A SUMO map is made up of edges connected at junctions. The edge id is required to define a route that a vehicle will follow. A route is a sequence of edges that a vehicle will pass through. For reference the relevant edges on the Town6 map are labeled below.

![Alt text](./docs/images/sumo_town6_edge_labels.png)


