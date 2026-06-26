# Repo Push Commands

## Create a new local repository

```bash
mkdir quantum-ai-defense-uav
cd quantum-ai-defense-uav
git init
```

## Create project folders

```bash
mkdir -p docs scripts sim services results
```

## Add and commit files

```bash
git add .
git commit -m "Initial research scaffold for quantum-assisted edge AI counter-UAV defense"
```

## Set main branch

```bash
git branch -M main
```

## Connect to GitHub

```bash
git remote add origin git@github.com:drsaikrishnathota1/quantum-ai-defense-uav.git
```

## Push to GitHub

```bash
git push -u origin main
```

## Full first-time setup in one block

```bash
mkdir quantum-ai-defense-uav && cd quantum-ai-defense-uav && \
git init && \
mkdir -p docs scripts sim services results && \
git add . && \
git commit -m "Initial research scaffold for quantum-assisted edge AI counter-UAV defense" && \
git branch -M main && \
git remote add origin git@github.com:drsaikrishnathota1/quantum-ai-defense-uav.git && \
git push -u origin main
```

## If the remote repo already exists locally

```bash
cd /path/to/your/local/repo
git status
git add .
git commit -m "Add research docs and scaffold"
git push origin main
```

## If origin already exists and you need to replace it

```bash
git remote remove origin
git remote add origin git@github.com:drsaikrishnathota1/quantum-ai-defense-uav.git
git push -u origin main
```

## If you want to use HTTPS instead of SSH

```bash
git remote add origin https://github.com/drsaikrishnathota1/quantum-ai-defense-uav.git
git push -u origin main
```

## Daily workflow

```bash
git status
git add .
git commit -m "Update experiments and documentation"
git push
```

## Pull latest changes

```bash
git pull origin main
```

## Create a new feature branch

```bash
git checkout -b feature/ai-threat-scoring
```

## Push a feature branch

```bash
git push -u origin feature/ai-threat-scoring
```

## Merge feature branch into main

```bash
git checkout main
git pull origin main
git merge feature/ai-threat-scoring
git push origin main
```

## Suggested commit messages

- `Add research plan`
- `Add paper outline`
- `Add initial simulator`
- `Add AI threat scoring baseline`
- `Add quantum-inspired optimizer`
- `Add crypto-agile security layer`
- `Add experiment results`
- `Refine manuscript figures and tables`

## Recommended next commands after docs are added

```bash
touch sim/main.py
touch scripts/run_experiment.sh
chmod +x scripts/run_experiment.sh
git add .
git commit -m "Add initial simulator and run script placeholders"
git push
```
