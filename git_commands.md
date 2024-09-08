# Quick Guide On Git Commands

All git commands are used in the terminal, while being inside a (local) git repository. Also make sure to have installed git (<link>https://git-scm.com/downloads</link>) before using those commands!

## cd (and other useful bash commands)

First, time for some bash! This is the standard language used in most terminals (bash for Linux distros and zsh for macOS, an improved version of bash) and its main use for this guide will be to help you move inside your file system.

The main bash commands are:
- <code>pwd</code>: this command **p**rints the current or **w**orking **d**irectory (side note, directory is another name for folder)
- <code>ls</code>: this command lists all items (subdirectories and files) stored inside the current directory
- <code>cd my_folder</code>: this command will transfer the current directory status from the directory you are currently in, to the *my_folder* directory
- <code>cd ./dir1/dir2/dir3/my_folder</code>: same as before, but instead of just going down one level into the file system you are now going four levels down (side note, the dot "." is used to refer to the current directory)
- <code>cd ..</code>: we've seen we can go *down* the file system, but how do we move *up*? With <code>cd ..</code>! The double dot ".." means the parent directory of the current directory (confusing right? Don't worry! It gets easy after you try it a few times)

There are more commands that can be useful, but for now lets just stick to the most important ones.

## python my_file_name.py

In order to execute (or run) a python file, you can use the command <code>python my_file_name.py</code> inside the terminal. Be sure to be inside the directory where the python file is stored, otherwise this won't work!

If you want to execute a file from a different folder, just use <code>python my_file_path\my_file_name.py</code>. Also, depending on your version of python you may need to use <code>python3 file.py</code> instead of the command shown above.

## git init

The command <code>git init</code> is used to initialize an empty git project locally on you computer. Essentially it transforms the current folder in a git repository, which can then be pushed online on a hosting site such as GitHub.

## git clone my_git_repo_url

This is also used to initialize the current folder as a git repository, the only difference is that this project points to an already existent project!

With <code>git clone my_git_repo_url</code> you will download all the files inside the project located at that url. Isn't that great??

**IMPORTANT**: use this command only in an empty local folder otherwise you will be overwriting all the files inside!
Now, try using <code>git clone https://github.com/mittaan/programming_exercises</code> in an empty folder!

## git add .

With <code>git add my_file</code> you are adding a single file from a local git repository to be staged in the **commit area**. You can see the commit area as a staging area for files that are ready to be committed.

The command <code>git add .</code> is the quick-and-dirty way of doing it. Instead of a single file, it adds the whole current directory to the commit area. Convenient, no?? Just use this as it saves so much time.

## git commit -m "Message"

After adding the files to the commit area you need to actually commit the files! But what does this mean? Basically, you're saying that the changes you made to the files are ready to be added to the (local, for now) project.

Giving a descriptive message is useful to keep track of when a specific change was made, in case you need to revert to a previous version of the project: <code>git commit -m "This is an example of a descriptive message!"</code>

## git push

Finally, we need to *push* the changes we made to the project from our local repository to the remote repository, so that other people can *pull* the changes we made and modify them if needed!

The command can be used in two ways:
- <code>git push</code>: it's the standard way, you'll use it a lot
- <code>git push -u origin my_branch_name</code>: this is used only for new branches that aren't on the remote repository yet. You need those extra parts for the first push if the branch is new.

## git pull

Just like <code>git push</code> *pushes* changes from your local repository to the remote repository, <code>git pull</code> *pulls* changes from the remote repository to your local repository.

## git checkout my_branch_name

Before explaining this command, let's talk about branches. A branch is a copy of the project (usually kept in the *main* or *master* branch) in which you can develop all your changes without impacting others and the active project.

With that said, <code>git checkout my_branch_name</code> moves you from the current branch to the branch specified in the command (just like the cd command in bash).

## git merge my_branch_name

This command updates the current branch with all the committed changes stored in the specified branch. You'll mostly use the command <code>git merge main</code> to update your current branch with the newest project version.

**IMPORTANT**: DO NOT use the <code>git merge</code> command lightly when you are on the *main*/*master* branch, as it can disrupt the current state of the project.

There are more git commands, but for now those are more than enough!
