# Git tutorial: https://www.youtube.com/watch?v=RGOj5yH7evk

## index of commands of this file:
1. ssh-keygen -t rsa -b 4096 -C "altalmas.abdallah@gmail.com"  
1. git pull
1. git add .
1. git commit -m "msg title" -m "msg description"
1. git commit -am "msg title"
1. git push -u origin <branch name>
1. git push
1. git reset <commit hash>
1. git reset --hard <commit hash>
1. git reset HEAD~1
1. git status
1. git merge
1. git merge --squash
1. git rebase
1. git log
1. git log --oneline

## Vocab:
1. CLI : command line interface


## Git Commands:
git clone    : bring a repo from online to local machine

git add      : tell git to track your files and change

git commit   : git saves your files

git push     : upload git commits to a remote repo

git pull     : update local repo from online

git merge    : (see tutorial)

git rebase   : (see tutorial)

## being a repo from local machine
1. on github.com
    * create a new repo
    * name it
    * copy the <ssh link>


1. on the local machine

        $ mkdir ~/myRepo

        $ cd ~/myRepo

        $ vim README.md

        $ git init

        $ git status

        $ git remote add origin <ssh link>

        $ git remote -v

        $ git add .

        $ git commit -m "init commit"

        $ git push -u origin master
            -u : --set-upstream

-----------
### ssh-keygen for a new machine
    $ ssh-keygen -t rsa -b 4096 -C "altalmas.abdallah@gmail.com"  
        -t : type
        -b : strength

    * name your key something like "testkey.pub"
        .pub : make it public to everyone

    $ cd ~/.ssh
    $ cat testkey.pub
        the key starts with ssh-rsa .......... ends with your email

    $ pbcopy < ~/.ssh/testkey.pub
        copy the key

    * now, add the key to you github account settings

-----------
### git add 

    $ git add .

    $ git add <file name>

    $ git add -p <file name>
        -p  : patch
            will go through all chunks of changes in that file and ask you (y/n) whether you want to add (stage) this change to make a single commit.

-----------
### git commit

    $ git commit -m "msg title" -m "msg description"
        -m : messege

    $ git commit -am "msg title"
        used when modifications are done on already existing files (no need to do git add <file>)

-----------
### git push

    $ git push origin master
        origin : remote name
        master : branch name

-----------
### git branching

    $ git branch                                    : see branches available

    $ git checkout -b feature-readme-instructions   : switched to a new branch

    $ git checkout master                           : switch back to master

    $ git checktout feature-readme-instrucitons
        make some changes

    $ git add .

    $ git commit -m "updated readme"
        now I would like to merge my new feature to master
        I can do that in 2 ways : 

        1st method:
            $ git checkout master

            $ git diff feature-readme-instructions
                shows what changes have been made in a branch that I plan to merge

            $ git merge

        2nd method:
            $ git checkout feature-readme-instructions

            $ git status
                push the commits to the public repo and then make a pull request online

            $ git push -u origin feature-readme-instructions

-----------
### git pull 
    $ git checkout master

    $ git pull origin master        : if you did not have an upstream

    $ git pull                      : if you already have an upstream

-----------
### delete a branch
    $ git branch -d feature-readme-instructions

-----------
### git conflicts
    $ git checkout master

    $ git checkout -b quick-test
        make some changes in README.md file , line 2

    $ git status

    $ git diff

    $ git commit -am "added something in branch"
        -am : add and commit (works for modified files and not newly created files)

    $ git checkout master
        update README.md file, line 2 (conflict)

    $ git commit -am "added something in master"

    $ git checkout quick-test

    $ git diff master

    $ git merge master  : to keep the branch up-to-date with whats going on in master
        it will say that there is a conflict
        we need to fix the merge conflicts

    $ git commit -am "updated with master and fixed the conflict"


    ### undo added (staged) files
    $ git checkout master
        modify README.md

    $ git status
        this will show that your modifications are not staged and not committed

    $ git add .
    $ git status
        now your modifications are staged but not commited

    $ git reset README.md       : un-stage a specific file
    $ git reset                 : un-stage everything added

    $ git status
        this will show that your modifications are now staged


### undo added and committed files
    $ git checkout master
        modify something

    $ git status
        this will show that your modifications are not staged and not committed

    $ git add .

    $ git commit -m "modified README.md"

    $ git status
        this will say that there is nothing to commit

    $ git reset HEAD~1      :   here we basically undo the commit we did before
        HEAD : a pointer to the last commit
        ~1   : point to 1 commit before

    $ git status
        this will show that your modifications still there but not staged and not committed

    $ git diff

    $ git log
        see all commits done before unique with their <commit hashes>

    $ git reset <commit hash that I want to go back to>

    $ git status
        this will show that your modifications still there but not staged and not committed

    $ git reset --hard <commit hash that I want to go back to>
        this gets rid of the commits and the changes

    $ git status
        this will say that there is nothing to commit


    # Git tutorial: https://www.youtube.com/watch?v=Uszj_k0DGsg

    $ git add -p README.md
        -p  : patch
        will go through all chunks of changes in that file and ask you (y/n) whether you want 
        to add (stage) this change to make a single commit.

### git conflicts
    $ git merge <branch name>
        if there is any conflicts, it will tell you the name of the file

        in that file:
            <<<<<<<<< HEAD
            
                    <part from my branch that I want to merge>
            
            =========

                    <part from  develop>

            >>>>>>>>> develop


# Git tutorial: https://www.youtube.com/watch?v=CRlGDDprdOQ

### git merge vs. rebase
    Problem statement:
        master  :    m1 ---- m2 ---- (m3)
                             |
        feature :            m2 ---- f1 ---- (f2)

        combined:    m1 ---- m2 ---- m3 ---- (?)


    Solutions: 
        method 1: (git merge)
            $ git checkout master
            $ git log
                m1 ---- m2 ---- (HEAD: m3)
            $ git merge --squash feature
                --squash : combines all the commits done in feature branch to 1 commit
                           and puts that commit at the HEAD of master
            $ git commit -m "feature and master merged"
            $ git log    : I am still in the master branch
                m1 ---- m2 ---- m3 ---- (HEAD: feature and master merged)


        *WARNING: do NOT use git rebase the commits that are published*
        *WARNING: do NOT use git rebase in big projects unless you are sure
        no one has used your published commits yet -with is hard to know-*
        *Notes:
            - git rebase re-writes the history
            - git rebase results in a linear history
        method 2: (git rebase)
            $ git checkout feature
            $ git log
                m2 ---- f1 ---- (HEAD: f2)
            $ git rebase master
            $ git log   : I am still in the feature branch
                m3 ---- f1 ---- (HEAD: f2)
                note that commits f1 and f2 here have different commit hashes than
                the previous f1 and f2 commits.
                and this is the reason why rebasing the already published commits
                is not advisable, because you are changing your published commits hashes
                (changing the history)
            $ git checkout master
            $ git log
                m1 ---- m2 ---- (HEAD: m3)
            $ git rebase feature
            $ git log
                m1 ---- m2 ---- m3 ---- f1 ---- (HEAD:f2)


# Git tutorial: https://www.youtube.com/watch?v=7Mh259hfxJg
notes of this are added in the previous tutorial notes


# Git submodule tutorial (series of videos): https://www.youtube.com/watch?v=RgIAXF53a8U&list=PL_RrEj88onS-jN7dZb-tYz0cpsxuA23Cm

## create submodules locally (manually)
    $ mkdir myRepo
    $ cd myRepo
    $ git init
    $ touch hello.txt
    $ git add .
    $ git commit -m "init myRepo with hello.txt"
    $ git log --oneline 
        has only 1 commit
    $ mkdir mySub
    $ cd mySub
    $ git init
    $ touch moin.txt
    $ git add .
    $ git commit -m "init mySub with moin.txt"
    $ git log --oneline
        has only 1 commit
    $ cd ..
        go back to myRepo folder
    $ git submodule add ./mySub
    $ git status
        new file: .gitmodules
        new file: submarines
    $ git add .
    $ git commit -m "added submodule mySub with .gitmodules"
    $ git log --oneline
        has 2 commits


## create submodules from online

Assume you have 2 online repos: 1. surface 2. submarine

    $ git clone <surface url>
    $ git log --oneline
        1 commit
    
    $ git submodule add <submarine url>
        I do this while being in /surface directory
    
    $ git status
        new file: .gitmodules
        new file: submarine

    $ git add .
    $ git commit -m "add submarine submodule"

    I am still in surface
    $ touch my.txt

    $ cd submarine
    $ touch name.txt
    $ git add .
    $ git commit -m "added name.txt"

    $ cd ..
        go back to surface
    
    $ git push origin
        will push to the remote repo surface only and will not push to submarine
        we will only see a reference of the remote repo submarine

    $ cd submarine
    $ git push
        will push to the remote repo submarine

## delete a git submodule

Assume you have 2 dependent repos : surface and inside of it is submarine

    $ cd surface
    $ git rm submarine
    $ git rm --cached submarine		: sometimes you need this
    $ rm -rf .git/modules/submarine
    
    go to .git/config and delete the parts related to submarine

    $ git add .
    $ git commit -m "removed submarine submodule"

    $ git push origin

    

