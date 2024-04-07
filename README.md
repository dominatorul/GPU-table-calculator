# Custom GPU UV3 Table Calculator

## Please use this **ONLY** as a reference; your actual values may be 5 to 20 mV (for Mariko) or 5 to 50 mV (for Erista) lower than the table indicates due to various factors.

This script calculates the voltage required for a specific GPU frequency based on a predefined lookup table. It is designed specifically for NVIDIA Tegra X1 (Erista) and NVIDIA Tegra X1+ (Mariko) GPUs.

## Disclaimer

This script is provided for informational purposes only. Its accuracy and compatibility with specific hardware configurations are not guaranteed. Please consult the Tegra GPU documentation for more information.

### Instructions to run the Python code locally:

1. **Install Python**: If you haven't already, install Python on your system. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/).

2. **Download the Script**: Obtain the script files `UV3_calculator.py` and `UV3_calculator_erista.py` from the GitHub repository.

3. **Open Terminal or Command Prompt**:
   - For Windows: Press `Win + R`, type `cmd`, and press Enter.
   - For macOS: Press `Cmd + Space`, type `Terminal`, and press Enter.
   - For Linux: Press `Ctrl + Alt + T` to open Terminal.

4. **Navigate to the Directory**: Use the `cd` command to navigate to the directory where the script files are located. For example:
   ```
   cd path/to/directory
   ```

5. **Run the Script**: Once you're in the directory containing the script files, execute the script by typing:
   ```
   python UV3_calculator.py
   ```
   or
   ```
   python UV3_calculator_erista.py
   ```

6. **Follow Prompts**: When prompted, enter the GPU speedo value, which is a performance metric.

7. **View Output**: The script will process the input and provide the desired output based on the entered GPU speedo value.

### Using Online Python Compiler:

If you prefer not to install Python locally, you can also use online Python compilers like [Programiz](https://www.programiz.com/python-programming/online-compiler/). Simply copy the script contents and paste them into the online compiler's editor. Then, follow the instructions provided by the compiler to run the script.

## Output

The script will display a table with supported GPU frequencies and their corresponding calculated voltage (in mV).

## Notes

- The script provides warnings for frequencies that may hit the PMIC limit.
- For frequencies below 691.2 MHz, the script recommends using a user-defined minimum voltage (vmin) or the voltage value for 691.2 MHz.

**Credits:**

* **NVIDIA Corporation** for Tegra X1 manual
* **[hanai3Bi/meha](https://github.com/hanai3Bi)** for the previous calculator
* **B3711** for his UV2 table
