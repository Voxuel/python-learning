# Git and GitHub

Git helps you keep track of changes to files in a project. You can save a named snapshot of your work, called a **commit**, and look back at earlier commits if you need to. Git runs on your computer.

**GitHub** is a website that hosts Git repositories online. A **repository** (or repo) is a project and its tracked history. Git and GitHub work together, but they are different: Git manages the history, while GitHub stores and shares repositories online.

## Install Git

Download Git from the [official Git website](https://git-scm.com/install/), then follow the instructions for your operating system:

- **Windows:** Download and run the installer from [Git for Windows](https://git-scm.com/install/windows). The default installation choices are fine for this course.
- **macOS:** Open Terminal and run `xcode-select --install` to install Apple's command-line developer tools, which include Git. You can also use the installation options on the official Git website.
- **Linux:** Use your distribution's package manager to install Git. For Debian- or Ubuntu-based systems, open a terminal and run:

  ```sh
  sudo apt update
  sudo apt install git
  ```

  For other distributions, see the [official installation instructions](https://git-scm.com/install/linux).

After installation, open a new terminal and check that Git is available:

```sh
git --version
```

The command should print the installed Git version. If it says that `git` cannot be found, finish the installation and reopen your terminal.

## Clone this repo from GitHub

**Cloning** makes a copy of a GitHub repository on your computer, including its files and history. This course is public, so you do not need a GitHub account to clone it.

1. Open a terminal. In VS Code, select **Terminal > New Terminal**.
2. Use `cd` to move to the folder where you want to keep the course. For example, to put it in your home folder:

   ```sh
   cd ~
   ```

3. Clone the course:

   ```sh
   git clone https://github.com/Voxuel/python-learning.git
   ```

   Git creates a new folder named `python-learning`.

4. Move into the new folder:

   ```sh
   cd python-learning
   ```

5. In VS Code, select **File > Open Folder** and choose the `python-learning` folder.

You now have a local copy of the course. You can read and change files on your computer; those changes do not automatically change the copy on GitHub.

## A few useful Git commands

Run these commands in the course folder (Not add/commit/push since that is just for the owner):

```sh
git status
```

Shows which files have changed.

```sh
git add path/to/file
```

Selects a changed file to include in your next commit. Replace `path/to/file` with the file's path.

```sh
git commit -m "Describe what changed"
```

Saves the selected changes as a commit in your local Git history. A commit message should briefly describe the changes.

These commands change your local repository only. Sending commits to GitHub is called **pushing** and requires permission to write to that GitHub repository.

## Quick check

You are ready when:

- `git --version` prints a version.
- The `python-learning` folder is on your computer.
- You can open that folder in VS Code and see the course files.
