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
I've created a new example file called `example.py` to the directory.
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

In order to track the file, we need to _commit_ the file.
A commit is a snapshot of a project that we can look back to or revert to if needed.
Before we can perform a commit, we need to stage the changes with want to commit.
This is done with the command `git add`.

```sh
$ git add example.py
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   example.py
```

Once you have added any changes that you want, we can commit our changes.

``` sh
$ git commit -m "Adding example python file"
[master (root-commit) 8a3801f] Adding example python file
 1 files changed, 167 insertions(+)
 create mode 100644 example.py
$ git status
On branch master
nothing to commit, working tree clean
```

The `-m` flag in the command provide a comment for our commit.
This is essential for telling what was added to a commit at a glance.
This will usually describe the features which have been added, changed or removed.

Our changes are now added and our git repo is up to date.

> __Note__: Whenever you make a noticeable change to your project, remember to commit the changes.

## Resetting Changes

Now that we have our repo and we know how to perform commits, we need to know how we can move back down the git tree in case issues arise.

We can see the history of our repositories using `git log`.
Let us add another commit for a more interesting example.

``` sh
$ git log
commit a9677d2ea27518fff2877a76a3ce402a5ba64a29 (HEAD -> master)
Author: Alexander Veltman <alexveltman@protonmail.com>
Date:   Fri Feb 12 12:30:51 2021 +0200

    Adding another example file

commit 8a3801fbcf2d97230877b0f46c7b0681b84b3403
Author: Alexander Veltman <alexveltman@protonmail.com>
Date:   Fri Feb 12 12:27:50 2021 +0200

    Adding example python file
```

We can see the two commits in the repo but let us assume that the file added most recently calls `rm -rf /` or deletes `System32` depending on your system.
We can undo this commit using `git reset`.
Let us undo the last commit made.

``` sh
$ git reset HEAD^
```

This will reset the repo to the commit before the `HEAD` commit.
The `HEAD` commit is the latest commit.

## Branches
