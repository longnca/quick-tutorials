# Virtual Environments

## How to set up a virtual environment

### 1. Create a project directory

```bash
mkdir MyPythonProject
cd MyPythonProject
```

### 2. Set Up a Virtual Environment

Within the project directory, create a virtual environment by running:

```bash
python -m venv venv
```

Here, `venv` is the name of your virtual environment. You can name it anything, but `venv` is a standard convention.

### 3. Activate the Virtual Environment

Before using the virtual environment, you must activate it. On Windows, run:

```bash
.\venv\Scripts\activate
```

Your command line should now show the name of your virtual environment, indicating that it's activated. For example, `(venv) C:\MyPythonProject>`.

#### Note:

You might get the error `CategoryInfo : SecurityError: (:) [], PSSecurityException` when trying to activate the `venv` due to PowerShell's execution policy. If you get that error, then you should temporarily change the execution policy to allow the activation script to run:

- Open PowerShell (not Terminal or CMD in Windows) **as an Administrator**.
- Execute the following command: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`.
- There's a message to ask you to confirm about "Execution Policy Change", enter "Y" (Yes).
- After changing the execution policy, try activating your virtual environment again: `.\venv\Scripts\activate`.
- Once you are done working in the virtual environment and no longer need to run scripts, you can revert back to the default policy by running: `Set-ExecutionPolicy Restricted -Scope CurrentUser`.

### 4. Install required packages

With the virtual environment activated, you can now install any packages required for your project using `pip`, the Python package installer:

```bash
pip install numpy pandas matplotlib
```

Replace `numpy pandas matplotlib` with the actual packages you need.

