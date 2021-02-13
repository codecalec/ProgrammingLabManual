# Version Control

Version control software allows us to store snapshots of a project while we are working on it.
Let's say we change the way we process our data which ends up breaking our plotting functions down the line.
We can revert back those changes so we have a functional analysis code.

There are many options for version control on all the major platforms (Windows, OSX, Linux) but the most common is [_Git_](https://git-scm.com/).
It can be downloaded on their [website](https://git-scm.com/downloads) or using a package manager.

### Working with a local repository

I will run through the basic commands needed to get your project version controlled.
I will assume that you have already created your project directory and are able to navigate to the directory in the commandline interface of your system.
If you're not comfortable with the commandline, this [guide](https://tutorial.djangogirls.org/en/intro_to_command_line/) by Django Girls provides instructions for any major platform.

We can start by creating our _Git repository_ or sometimes called a Git repo.
This is the system that we will use to keep track of any changes to our project.
We initialise our Git repo in the directory in which we want our files to be tracked.
I will be using the source directory for this very book as an example.

Once you have navigated to your project directory, we can initialise the repo.

``` sh
$ git init
Initialized empty Git repository in /home/alex/Documents/ProgrammingLabManual/.git/
```

Now that our Git repo is setup, we can see if there are any files that we can tell Git to track.
I've created a new example file called `example.py` to the directory.
We can use `git status` to show us some information about our Git repo.

``` sh
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	example.py

nothing added to commit but untracked files present (use "git add" to track)
```
This says we are on the branch `master`.
This will be explained later.
You can see that no commits have been submitted.

In order to track a file, we need to add the file to a commit.
A commit is a snapshot of a project that we can look back to or revert to if needed.
Before we can perform a commit, we need to stage the changes we want to commit.
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

Our changes are now added and our Git repo is up to date.

> __Note__: Whenever you make a noticeable change to your project, remember to commit the changes.

### Resetting Changes

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

### Branches

We now know how to move up and down the commit tree (using `git commit` and `git reset`) so let us learn about moving horizontally.
This is known as creating a branch.
This new branch can exist separate from main branch and commits can be performed on this new branch independently.
Once we feel that our new branch is worthy, it can be merged into the main branch.
The changes on the new branch will be placed into the main branch and the new branch will be removed.

Branches allow us to _sandbox_ our changes and allow separate editions of the same codebase to exist side by side.
This could be useful you want to work on a separate feature while your colleagues work on the main branch.

Let us create a branch to update our project with a new data acquisition system.
This is done through the `git branch` command.

``` sh
$ git branch new_daq
$ git branch
* master
  new_daq
```

Using the command `git branch` by itself will print the branches available in the repo.
If we append that command with a branch name, it will create our new branch.
In the example output, you can see the asterisk indicating that we are still working in the master branch.
To start working in our newly created branch, we use the command `git checkout`.

``` sh
$ git checkout new_daq
$ git branch
  master
* new_daq
```

Any commits or other changes will be performed on the `new_daq` branch, leaving the master branch unchanged.

Once the new DAQ system is implemented and the changes have been committed, we can merge the changes into the master branch.
This is done with the `git merge` command.

``` sh
$ git checkout master
$ git merge new_daq
Updating 8a3801f..30e1222
Fast-forward
 example.py | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 example.py
```

If we are done with the branch and all the changes have been merged into the master branch, we can delete the branch with the `-d` flag.
``` sh
$ git branch -d new_daq
```

### Resources

Here are a group of fantastic resources if you are still not sure on the concepts presented by me:
- [Getting started with GitHub](https://docs.github.com/en/github/getting-started-with-github) - A Git tutorial aimed at usage with Github.
- [Missing Semester - Version Control (Git)](https://missing.csail.mit.edu/2020/version-control/) - Amazing lecture series talking about the tools need in software development. Mainly aimed at a Computer Science background.
- [GitHub Git Cheatsheet](https://education.github.com/git-cheat-sheet-education.pdf) - A cheatsheet to have bookmarked.

> __Note__: Git is one of the most ubiquitous pieces of software used by developers around the world. 
> If you are having an issue, there will be tons of tutorials, guides, wikis, blogs, books and individuals able to help.
> Use the power of modern search engines to make your life easier.
