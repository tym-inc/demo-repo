
## Question 
wowzers sdfa sdfas dfa

### Code Snippets

[main.py#L14](main.py#L14)	
````python
def main():
    schedule.every(1).seconds.do(job)
    schedule.every(5).seconds.do(less_frequent_job)

    while True:
        schedule.run_pending()
        time.sleep(1)

````

### Terminal Output
````
❯ git status
On branch yo
Your branch is up to date with 'origin/yo'.

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md
        modified:   main.py
        deleted:    test

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        abc.js

no changes added to commit (use "git add" and/or "git commit -a")
~/repo/demo-repo yo !3 ?1 ❯    
````
	