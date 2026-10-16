# Python virtual environments with UV

## What is a virtual environment?

A virtual environment is a separate place for one Python project to keep its Python version and extra packages (also called libraries) organized.

Imagine each project has its own toolbox. One project can use one version of a package, while another project uses a different version. The tools stay separate, so changing one project's packages is less likely to break another project.

A virtual environment does not contain your program files. It is a folder of tools and packages that Python uses to run your program.

## What is UV?

UV is a command-line tool that can find or install Python versions, create virtual environments, manage packages, and run Python programs. You can use `uv run` to run a program without activating its virtual environment by hand.

First, install UV by following the [official installation guide](https://docs.astral.sh/uv/getting-started/installation/). Then open a terminal and check that it works:

```sh
uv --version
```

The terminal is a place where you type commands for your computer. In VS Code, open it with **Terminal > New Terminal**.

## Create a project with a specific Python version

The following command creates a new project named `hello-python` and sets it to use Python 3.12:

```sh
uv init --python 3.12 hello-python
```

Move into the new project folder:

```sh
cd hello-python
```

UV creates project files, including:

- `.python-version`, which tells UV which Python version to use by default for this project.
- `pyproject.toml`, which describes the project and its dependencies (extra packages it needs).
- `.venv`, the virtual environment. UV creates it the first time it needs to run or install something for the project.

If Python 3.12 is not already available, UV can download it for you. You can also ask UV to install it ahead of time:

```sh
uv python install 3.12
```

To see the Python versions UV knows about, run:

```sh
uv python list
```

## Run a Python file from the terminal

In the `hello-python` folder, create a file named `hello.py` with this code:

```python
print("Hello from Python!")
```

Run it from the terminal:

```sh
uv run hello.py
```

You should see:

```text
Hello from Python!
```

When you use `uv run` inside the project, UV selects the project's Python version, creates or updates `.venv` if needed, and runs the script in that environment. The first run may take a little longer while UV sets things up.

You can check which Python version the project is using with:

```sh
uv run python --version
```

Run commands from the project folder, or give the script's path, such as `uv run lessons/hello.py`.

## Change the project's Python version

To choose a different default version, update the project's `.python-version` file with:

```sh
uv python pin 3.13
```

The next `uv run` uses the newly selected version and updates the project environment if needed. Use a version that is installed or let UV download it when asked.

## Activate the environment yourself (optional)

Usually, `uv run hello.py` is the simplest way to run a project script. You can also activate `.venv` and use Python directly. Activation commands depend on your operating system and terminal.

On macOS or Linux, in the project folder, run:

```sh
source .venv/bin/activate
python hello.py
deactivate
```

On Windows PowerShell, run:

```powershell
.venv\Scripts\Activate.ps1
python hello.py
deactivate
```

When the environment is active, `python` means the Python inside `.venv`. `deactivate` turns it off. Closing the terminal also ends the activation.

## Run a single script with UV

For a small script that is not part of a project, you can ask UV to prepare it for a particular Python version:

```sh
uv init --script hello.py --python 3.12
```

Then run it with:

```sh
uv run hello.py
```

UV records the script's Python requirement in the file and uses that version when it runs the script. This is useful when you just have one script; for a project with several files, use a project and its `.venv` instead.

## Remember

- Use one virtual environment per project to keep project packages separate.
- Use `uv run your_file.py` to run a script with the project's Python version and packages.
- `.venv` is created and managed for you; you normally do not need to edit files inside it.
- The `.venv` folder is local to your computer. Share the project files and UV configuration, not the `.venv` folder.
