@echo off
REM abort on errors
setlocal enabledelayedexpansion
set "errorlevel="
if not errorlevel 0 exit /b %errorlevel%

REM build
npm run build

REM navigate into the build output directory
cd dist

REM if you are deploying to a custom domain
REM echo www.example.com > CNAME

git init
git add -A
git commit -m "deploy"

REM if you are deploying to https://<USERNAME>.github.io/<REPO>
git push -f git@github.com:shyu216/bookmarks.git main:gh-pages

cd ..