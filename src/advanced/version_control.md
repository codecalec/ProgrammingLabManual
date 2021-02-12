# Version Control

Version control software allows us to store snapshots of a project while we are working on it.
Let's say we change the way we process our data which ends up breaking our plotting functions down the line.
We can revert back those changes so we have a functional analysis code.

There are many options for version control on all the major platforms (Windows, OSX, Linux) but the most common is [_git_](https://git-scm.com/).
It can be downloaded on their [website](https://git-scm.com/downloads) or using a package manager.

## Working with a local repository

I will run through the basic commands needed to get your project version controlled.
I will assume that you have already created your project directory and am able to navigate to the directory in the commandline interface of your system.
If you're not comfortable with the commandline, this [guide](https://tutorial.djangogirls.org/en/intro_to_command_line/) by Django Girls provides instructions for any platform.

Let's start by creating our _git repository_ or sometimes call a git repo.
This is the system that we will use to keep track of any changes to our project.
I will be using the source directory for this very book as an example.
``` sh
$ git init
Initialized empty Git repository in /home/alex/Documents/ProgrammingLabManual/.git/
```

Now that our git repo is setup, we can see if there are any files that we can tell git to track.
I've crated a new example file called `example.py` to the directory.
We can use `git status` to show us some information about our git repo.

```sh
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	example.py

nothing added to commit but untracked files present (use "git add" to track)
```
