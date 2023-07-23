---
title: Day 4
description: Day 4
author: Qusai Al Shidi
keywords: space-weather,space,python
math: mathjax
---

# What is this git thing? 🤔

---------------------------

## Review

- Git is a *version* controlling software for your code.
- You've made changes to your local repository.
- You pushed changes to your fork on GitHub.

---------------------------

## Let's go through the commands

---------------------------

# git pull

- by itself, pull commits from the remote repository 'origin' (GitHub)
- `git pull <remote> <branch>` pulls changes from a similar repository on a
    different remote (AetherModel GitHub)

---------------------------

# git push

- by itself, push commits from your computer to remote repository 'origin'
    (GitHub)
- `git push <remote> <branch>` pushes the branch to remote repository

---------------------------

# git commit <file> -m 'A message'

- *stage* changes to be pushed, before this your edits are *unstaged*.
- commit messages should be useful and typically not more than 50 characters
    long.
- commit every time you have something in a working state

---------------------------

# git add <file/folder>

- *track* a file for changes. It will still be *unstaged* until you commit it.
- be careful adding folders, it will add __all__ files in it.

---------------------------

# git merge <branch-to-merge>

- merge two branches together,

```
           A---B---C topic                                          
          /                                                         
     D---E---F---G master                                           
```

- if on `master`, `git merge topic` will combine `topic` unto `master`

---------------------------

# rebase ???

- a rebase reapply commits onto a new base in your history, this might be
    necessary if you made commits based off a different point than the remote

```
      A---B---C topic
     /
D---E---F---G master


                A'--B'--C' topic                                 
               /                                                 
  D---E---F---G master                                           
```

---------------------------

# remember `--help` 😊
## git <command> --help

---------------------------

# Let's look at the changes you've made so far
## git log

- commit history with messages

---------------------------

# git show

- show the changes of the last commit
- `git show HEAD~2` will show changes since last 2 commits.
- `HEAD` is the current commit

---------------------------

# .gitignore

- Ask git to ignore certain files.
- This might be hidden `ls -a` to list *all* files

```bash
spyder .gitignore
# maybe on windows:
Notepad .gitignore
```

---------------------------

# refer to your git cheat sheets 📃 for other things!
