## How to start using Git

### Installing and configuring Git: 

#### Step 1: Install Git:

- If you haven't already, the first thing you need to do is install Git on your computer.
- You can download Git for your specific operating system from the official website: https://git-scm.com/downloads. Follow the installation instructions for your platform.

#### Step 2: Configure Git:

- Once Git is installed, you need to configure Global Git account with your name and email address. 
- Note that, in order to show your contribution to GitHub commits, you have to use your GitHub's username/email. For example, my GitHub username and email are: longbytes and <my-email@example.com>. 
- Open your command prompt or terminal and enter the following commands, replacing Your Name and youremail@example.com with your GitHub's username/email
```bash
git config --global user.name "your-github-username"
git config --global user.email "your-github-email@example.com"
```

### Creating a local repo:

- Now, let's create a new directory where you want to store your project files. 
- Open your terminal and navigate to the directory where you want to create your project. You can use the `cd` (change directory) command to navigate.
- For example, to create a directory named "my_project" and navigate into it, you can use these commands:

```bash
mkdir my_project
cd my_project
```