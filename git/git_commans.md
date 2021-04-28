## 1. create a new repository on the command line
echo "# files_usage" >> README.md\
`git init` \
`git add README.md` \
`git commit -m "first commit"` \
`git branch -M main` \
`git remote add origin https://github.com/pactera-vicky/files_usage.git` \
`git push -u origin main`\

## 2. push an existing repository from the command line
`git remote add origin https://github.com/pactera-vicky/files_usage.git `\
`git branch -M main` \
`git push -u origin main` 

## 3. push local branch to repository branch
- before you push you local branch you need to pull the latest code from repository\
`cd pii_us_api(your project)` \
`git checkout -b dev(branchname) ` \
`git add ./git add filename.py` \
`git status` (check the file status) \
`git reset HEAD .idea`(untracked .idea) \
`git commit -m"your comments on this push"` \
`git push origin dev`

## 4. merge former-version with current version code
- after git commit use 
`git rebase -i HEAD~2`(# handle twice update currently)\
  insert module:replace pick with squash\
  then quit with :wq(twice)\
`git log`(check the log)\
`git push origin branch_name`(if error occurs,you can change to the following code)\
`git push origin branch_name -f` (-f means force，please be cautious when handling)
  
- if you do close pull request, and want to push you modify code again, in this situation you must use `git rebase`

  

