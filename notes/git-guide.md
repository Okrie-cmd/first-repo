

    # Git Study Notes 🚀
     
    ## 1. Local Repository Setup
    * `git init` - Initialize a new local Git repository.
    * `git status` - Check the state of the working directory and the staging area.
    * `git config --global user.name "Your Name"` - Set your identity.
    * `git config --global user.email "your@email.com"` - Set your email.
     
    ---
     
    ## 2. The Basic Workflow
    1. `git add <file>` - Add a specific file to the staging area (the "stage").
    2. `git add .` - Add **all** changed files to the staging area.
    3. `git commit -m "Commit message"` - Create a permanent snapshot of the staged changes.
    4. `git push` - Upload local commits to a remote repository (GitHub).
    5. `git pull` - Fetch and download content from a remote repository and update the local repo.
     
    ---
     
    ## 3. Branching & Merging
    * `git branch` - List all local branches.
    * `git checkout -b <branch-name>` - Create a new branch and switch to it.
    * `git checkout <branch-name>` - Switch to an existing branch.
    * `git merge <branch-name>` - Merge the specified branch into the **current** branch.
    * `git push -u origin <branch-name>` - Push a new local branch to GitHub for the first time.
     
    ---
     
    ## 4. Time Travel & Undo
    * `git log --oneline --graph --all` - View the commit history as a visual tree.
    * `git checkout <commit-hash>` - Switch the working directory to a specific commit (Detached HEAD).
    * `git stash` - Temporarily shelve (save) uncommitted changes to work on something else.
    * `git stash pop` - Restore the most recently stashed changes.
    * `git reset --hard <commit-hash>` - **Danger!** Reset the repository to a specific commit and delete all changes after it.
     
    ---
     
    ## 5. Tips
    * `git blame <file>` - See who changed each line of a file.
    * `git diff` - Show changes between commits, commit and working tree, etc.
    * `git commit --amend` - Edit the last commit (change message or add forgotten files).


