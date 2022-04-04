
## Question 
abcdef

### Code Snippets

[main.py#L11](main.py#L11)	
````python
def less_frequent_job():
    print("I'm working... occassionally...")

def main():
    schedule.every(1).seconds.do(job)

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
````
	