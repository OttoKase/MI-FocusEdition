# Mission-Impossible
This repository is made for Artificial and Natural Intelligence (LTAT.02.024) course's project. The project's main goal is to try and understand how the performance of completing logic-based task is affected by having to listen and answer questions about an unrelated text.

The colors of the screen, pause time, number of loops can be set in config.py file.

## Setup
This guide will walk you through setting up the necessary Python environment to run the PsychoPy experiment locally on a Windows machine.
### Prerequisites
This project requires **Python 3.11**. Newer versions (like Python 3.12 or 3.13) have known compatibility issues with the PsychoPy dependency.

Check your Python version using terminal. If the output is Python `Python 3.11.x` or `Python 3.10.x` then you can skip the prerquisites.
```bash
py --version
```

Go to the official Python downloads page and specifically look for the Python 3.11.x releases. (*You can find this under "Looking for a specific release" on the main Python download page: https://www.python.org/downloads/windows/*)

Download the Windows (depending on your computer) installer (64-bit) for a version of 3.11 (e.g., Python 3.11.9).

Crucially: During installation, make sure to check the box that says "Add python.exe to PATH".

### Environment Setup
It is critical to run the project inside a **Virtual Environment (.venv)** to isolate dependencies and ensure the correct Python 3.11 version is used.

Navigate to the project folder (`MI-FocusEdition`) in your terminal.

Use the `py` launcher to explicitly create the environment using your Python 3.11 installation:

```
py -3.11 -m venv .venv
```
You must **activate** the environment before installing packages or running the script.

**First-time Fix (PowerShell Security)**: If you are using PowerShell (the VS Code default), you may need to allow scripts to run. Run this command first:
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```
**Activate**: Run the activation script:
```
.\.venv\Scripts\Activate
```
You will know the environment is active when you see **(.venv)** at the start of your terminal prompt.

### Install dependencies
With the environment active, you can now install PsychoPy and all necessary packages.

Make sure you have a file named `requirements.txt` in the root directory of your project, containing the necessary dependencies (e.g., `psychopy`).

Run the installation command (this uses the pip program inside your `.venv`):
```
pip install -r etc/requirements.txt
```

### Run the Experiment
Ensure your terminal is in the project folder and the (.venv) is active.

Run the main file:
```
python main.py
```
The experiment window should now launch.

### Troubleshooting (Critical Fix)
If you encounter the error:

```
ImportError: DLL load failed while importing _core: The specified module could not be found.
```

This means you are missing core Microsoft C++ libraries needed for PsychoPy's low-level graphics.

**Solution: Install Microsoft Visual C++ Redistributable**

1) Download the latest "Visual Studio 2015, 2017, 2019, and 2022" C++ Redistributable from the official Microsoft website. (https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#latest-supported-redistributable-version)
2) Ensure you download the X64 version.
3) Run the installer and restart your computer completely before attempting to run the experiment again.
