# UV3-calculator
A Pretty Good Custom GPU Table Calculator

This code calculates the voltage required for a specific GPU frequency and temperature based on a predefined lookup table.

**How to Use:**

1. Run the script.
2. Enter the GPU speedo (a performance metric) when prompted.

**Output:**

The script will display a table with supported GPU frequencies and their corresponding calculated voltage (in mV).

**Important Notes:**

* This script is designed specifically for the NVIDIA Tegra X1+ GPU(Mariko). Using it with other GPUs like Tegra X1 (Erista) will not work.
* The script provides a warning for speedo values below 1400, potentially indicating compatibility limitations.
* For frequencies below 691.2 MHz, the script recommends using a user-defined minimum voltage (vmin) or the voltage value for 691.2 MHz.

**Disclaimer:**

This script is provided for informational purposes only. Its accuracy and compatibility with specific hardware configurations are not guaranteed. It is recommended to consult the Tegra GPU documentation.

**Credits:**

* **NVIDIA Corporation** for Tegra X1 manual
* **hanai3Bi/meha** for the previous calculator
* **B3711** for his UV2 table
