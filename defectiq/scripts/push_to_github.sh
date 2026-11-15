#!/usr/bin/env bash
# Run AFTER creating an empty repo named "defectiq" on github.com/DeepthiGardas
set -e
git init
git add .
git commit -m "Initial scaffold: DefectIQ project structure"
git branch -M main
git remote add origin https://github.com/DeepthiGardas/defectiq.git
git push -u origin main
