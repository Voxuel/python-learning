# Installing Visual Studio Code

Before writing Python, you need a place to write and manage your code. This lesson introduces text editors and IDEs, then walks through installing Visual Studio Code (VS Code).

## What is a text editor?

A **text editor** is an app for writing and changing text files. A code editor is a text editor with features that help when writing code, such as coloring parts of the code and pointing out some mistakes.

A code editor does not usually run your program by itself. You can run the program from a terminal or use tools added to the editor.

## What is an IDE?

An **integrated development environment (IDE)** is an app that brings several programming tools together. An IDE often includes a code editor, tools to run a program, and a debugger that helps find problems.

Visual Studio Code is a code editor that can be extended with add-ons called **extensions**. Extensions add tools and language support, so VS Code can provide many features people use in an IDE. VS Code is a different product from Microsoft's larger IDE named Visual Studio.

## VS Code and Python are separate

VS Code is where you write and organize your code. A **Python interpreter** is a separate program that runs Python code. Installing VS Code does not automatically install Python.

For Python support in VS Code, you can also install Microsoft's Python extension. The extension helps VS Code work with Python, but it does not include the Python interpreter. In a later lesson, UV will help us manage Python versions and project environments.

## Download VS Code

1. Go to the official [Visual Studio Code download page](https://code.visualstudio.com/download).
2. Choose the download for your operating system: Windows, macOS, or Linux. Download the regular **Stable** version, not Insiders.
3. Open the downloaded file and follow the installation instructions for your computer.

### Windows

Download the Windows installer, open it, accept the license, and follow the setup steps. The default choices are fine for this course. When installation finishes, open Visual Studio Code from the Start menu.

### macOS

Download the macOS version. Open the downloaded archive, then drag Visual Studio Code into the Applications folder if the installer asks you to. Open Visual Studio Code from Applications.

### Linux

Choose the package that matches your Linux distribution on the download page. Debian- and Ubuntu-based distributions generally use the `.deb` package; Fedora- and Red Hat-based distributions generally use the `.rpm` package. Open the downloaded package and follow your system's installation prompt. If neither package matches your distribution, follow the Linux instructions on the official [VS Code setup page](https://code.visualstudio.com/docs/setup/linux).

## Add Python support to VS Code

After VS Code is installed:

1. Open VS Code.
2. Open the Extensions view by selecting the Extensions icon in the sidebar, or press `Ctrl+Shift+X` on Windows/Linux or `Cmd+Shift+X` on macOS.
3. Search for **Python**.
4. Select the extension published by **Microsoft**, then select **Install**.

This extension adds Python-related editing and running tools to VS Code. You will still need a Python interpreter, which we will set up separately.

## Open this course in VS Code

Open the folder containing this course:

1. In VS Code, select **File > Open Folder**.
2. Choose the `python-learning` folder.
3. Select **Open**.

Opening the whole folder makes it easier to find and work with the lesson files. You should see the course folders in VS Code's Explorer sidebar.

## Quick check

You are ready for the next lesson when:

- Visual Studio Code opens on your computer.
- You can see the `python-learning` course folders in its Explorer sidebar.
- The Microsoft Python extension is installed.
