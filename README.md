# OpenCDA-Merging

A fork of the OpenCDA repo — see the [original documentation](BASE_README.md) — that contains custom Co-Simulation scenarios running CARLA and SUMO integrated with OpenCDA.

---

## Users Guide
* [Installation](#installation)
* [Creating a Custom Scenario](#creating-a-custom-scenario)

## Scenarios (SUMO/CARLA)
* [Highway Ramp Merging](#highway-ramp-merging)

---

# Installation

TODO: Installation instructions

---

# Creating a Custom Scenario

TODO: Instructions

---

# Scenarios Descriptions

## Highway Ramp Merging

<!-- <video width="640" height="360" controls>
  <source src="https://raw.githubusercontent.com/andrearante12/OpenCDA-Merging/main/docs/videos/Highway_Merging.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video> -->
![Demo](docs/videos/Highway_Merging.gif)


**Direct video link:**  
[docs/videos/Highway_Merging.mp4](docs/videos/Highway_Merging.mp4)

Here we can see an example scenario of an ego vehicle attempting to merge onto a busy freeway.

## Running the simulation locally

In the root directory of this repo run
```
conda activate opencda
python opencda.py -t merging  -v 0.9.12 
```

---

## Important Files that Describe the Simulation  
(See official docs: https://opencda-documentation.readthedocs.io/en/latest/md_files/logic_flow.html)

---

## 1. SUMO Simulation (`merging.rou.xml`)

SUMO is utilized to generate the background traffic for the simulation.

➡️ [opencda/assets/Merging/Merging.rou.xml](opencda/assets/Merging/Merging.rou.xml)

---

## 2. Simulation Server Configuration (`merging.yaml`)

This YAML file configures:

- Server parameters (sync vs async mode)  
- Traffic flow and human-driven vehicle configuration  
- Connected Automated Vehicle (CAV) parameters  
- Sensor settings (LiDAR, detection model, trajectory smoothing)

➡️ [opencda/scenario_testing/config_yaml/merging.yaml](opencda/scenario_testing/config_yaml/merging.yaml)

---

## 3. OpenCDA Integration (`merging.py`)

This Python script is the main entry point for running the merged SUMO–CARLA scenario.

➡️ [opencda/scenario_testing/merging.py](opencda/scenario_testing/merging.py)

---

# Town06 Relevant Edges

A SUMO map is made up of edges connected at junctions.  
The **edge ID** is required to define vehicle routes (a sequence of edges).  
The relevant edges in CARLA Town06 are labeled below.

![Town06 SUMO edges](docs/images/sumo_town6_edge_labels.png)
