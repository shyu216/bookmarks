@echo off
cd C:\Users\LMAPA\Documents\GitHub\a-bookmark\dist
git init
git add -A
git commit -m "deploy"
git push -f git@github.com:shyu216/bookmarks.git master:gh-pages
cd C:\Users\LMAPA\Documents\GitHub\a-bookmark\