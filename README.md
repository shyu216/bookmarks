Use this project to build a bookmark page from your browser's bookmark export file. The page was built with Vue.js.

## Preparation
This part lacks of testing, please try your best to debug and fit your case by yourself.

1. Go to 'bookmark_helper' folder.
2. Export your bookmark from browser as html and put it here.
3. Install the required packages by running `pip install -r requirements.txt`.
4. Run the collect_data.py following by analyse_data.py.
5. Move sites.json to 'public' folder.

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```

### Deploy to GitHub Pages

Run either deploy.bat or deploy.sh to deploy the project to GitHub Pages.

For mac, you may need to run `chmod +x deploy.sh` to make it executable.

The branch of gh-pages could be `master` or `main`, please check the script before running.

