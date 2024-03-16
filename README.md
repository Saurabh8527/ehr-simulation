# EHR Simulation Project

## Overview

This project simulates the process of fetching patient information from Electronic Health Record (EHR) systems (Cerner and Epic), processing the information with basys.ai, and sending the processed information to Unified Medical (UM).

## Folder Structure

- `ehr_client.py`: Contains the `EHRClient` class for simulating API calls to Cerner and Epic EHR systems.
- `basys_ai_processor.py`: Contains the `BasysAIProcessor` class for simulating data processing with basys.ai.
- `um_client.py`: Contains the `UMClient` class for simulating API calls to Unified Medical.
- `main.py`: The main script that orchestrates the simulation flow.
- `util.py`: Contains utility functions required for the simulation.

## Setup and Running the Simulation

1. Clone or download this repository to your local machine.
2. Navigate to the directory containing the project files.
    ```bash
        cd ehr-simulation
    ```
3. Run the simulation using the following command:
   ```bash
       python3 main.py
   ```
4. The output of each step in the simulation will be printed to the console.
5. Try a few times to check error handling with simulated error(change the error_chance if required from the simulation functions)
