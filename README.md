# AlphaLink

AlphaLink is a Python-based program designed to help users visualize and manage memory usage in Windows systems to improve performance. By providing insights into memory consumption by various processes, users can make informed decisions to optimize their system's performance.

## Features

- **Visualize Memory Usage**: Displays a list of running processes and their memory usage.
- **Plot Memory Usage**: Graphically plots memory consumption for a quick visual overview.
- **Refresh Data**: Easily refresh the data to get the latest memory usage statistics.

## Requirements

- Python 3.x
- `psutil` library for process and system utilization information.
- `matplotlib` library for plotting memory usage.
- `tkinter` for GUI.

## Installation

1. Clone this repository to your local machine.
2. Install the required Python packages using pip:
   ```bash
   pip install psutil matplotlib
   ```

## Usage

Run the script using Python:

```bash
python alphalink.py
```

- **Refresh**: Click the "Refresh" button to update the list of processes and their memory usage.
- **Plot Memory Usage**: Click the "Plot Memory Usage" button to view a bar chart of memory usage by process.

## Note

- This tool is intended for use on Windows operating systems.
- Administrator privileges may be required to access all process information.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [psutil](https://github.com/giampaolo/psutil) for providing an interface for retrieving information on system utilization.
- [matplotlib](https://matplotlib.org/) for creating static, interactive, and animated visualizations in Python.