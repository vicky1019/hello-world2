## 1. create a new repository
echo "# doc_summary" >> README.md

`$ git init`

`$ git add README.md`

`$ git commit -m "first commit"`

`$ git branch -M main`

`$ git remote add origin https://github.com/[your_username]/[repository_name].git` 

`$ git push -u origin main`

## 2. push an existing repository from the command line

add your files to your repository`$ git add requirements.txt main.py .gitignore`

`$ git commit -m"first commit"`

or open your github, login your profile, and create a new repository called [your repository name-practice]. create an empty repository without a README or license file,once you created the repository, return to the command line and push your local files to github

`$ git remote add origin https://github.com/[your_username]/[repository_name].git `

rename the default branch main, to match what github expects: 

`$ git branch -M main` (rename branch)

`$ git push -u origin main`(push your main branch to github`s main branch) 

## 3. push local branch to repository branch

- before you push you local branch you need to pull the latest code from the repository 

`cd pii_us_api(your project)` 

`git checkout -b dev(branchname) ` 

`git add ./git add filename.py` 

`git status` (check the file status) 

`git reset HEAD your_file_name`(to undo a git add eg:git reset HEAD .idea) 

`git commit -m"your comments on this push"` 

`git push origin dev`

## 4. merge former-version with current version code

- after git commit use 

`git rebase -i HEAD~2`(# handle twice update currently)

  insert module:replace pick with squash

  then quit with :wq(twice)

`git log`(check the log)

`git push origin branch_name`(if error occurs,you can change to the following code)

`git push origin branch_name -f` (-f means force，please be cautious when handling)
  
- if you do close pull request, and want to push you modify code again, in this situation you must use `git rebase`

## 5. how to delete a git branch both locally and remotely

- delete a git branch locally

  `$ git branch -D your_branch_name`(implement this command you need to switch to master)


## 6.git reset


## 7.how to change remote git repository

- list your existing remote repositories

  `$ git remote -v`
- Change a remote Git repository

  `$ git remote set-url origin https://github.com/[your_username]/[repository_name].git `

- then check the remote repository list

## 8. when modification on a branch if you need to switch to another branch and keep the changes

- `git stash`(remember the stash note)

- `git stash list`(check the list you stashed and pick the right {number} you want to get back)
  
- 'git stash apply stash@{number}'

## 9. change branch name

- git branch -m [oldBranchName] [newBranchName]

## 10.git tag

- git create tag
  
  - The tag should been created in the master branch
  
   git checkout master
   
  - create the tag
  
  git tag release-jp-fix-v1 -m "The release of the fix for jp"
   
  - push the tag to origin registry
  
  git push origin release-jp-fix-v1

- git checkout tags/[tag_name] -b [branchname]
   
   first git pull(pull the tag code)
  
  `git checkout tags/release-jp-fix-v2 -b release-jp-fix-v2-branch`







  

