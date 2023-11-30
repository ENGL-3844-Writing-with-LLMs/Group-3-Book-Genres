# ENTER TITLE OF PROJECT HERE

Enter basic description of project here in 1-2 sentences.

## TOC

1. `data`: Add all data sets in this folder.
2. `models`: Save all model files `.pkl` in here with the `pickle` module

## Style Guide

**Filenaming**: Be sure to use all lowercase lettering and hyphens in between all words.

## Basic Architecture

```
|__ data
    |__ .keep
    |__ original-dataset.csv
    |__ processed-dataset.csv
|__ figures
    |__ .keep
    |__ eda-distribution-dates.png
    |__ eda-distribution-headline-word-count.png
    |__ fp-tp-heatmap.png
    |__ ...
|__ models
    |__ .keep
    |__ trained-model-1.pkl
    |__ trained-model-2.pkl
    |__ ...
|__ cleaning-and-eda.ipynb
|__ ml-project-name-here.ipynb
|__ model-card.pdf
|__ reflective-memo.pdf
|__ README.md
```

## Team Workflow Process

### Project KanBan Board

Be sure to create tasks for the team to complete. Update the tasks as well, when appropriate.

### Coding on new branches

Every pair/programming session should conduct the following process to ensure that you do not create `git` conflicts:

1. Create new branch with a meaningful, goal-driven name.
2. Switch to the new branch.
    - ***WARNING***: Be sure to make this switch!
3. Work on code / content.
4. After completing the goal, `commit` and `push` changes made on new branch.
5. Create a `pull request` and ...
    - Write an overview of your new changes/additions for your other team members to review. You can use a bulleted list to do so.
    - Tag/request your peers to review it.
6. Team members should review it in a timely manner and use the discussion features to coordinate their thoughts and ideas.
7. Once everyone thinks the changes are good, `merge` changes to main branch
