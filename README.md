# How to build and deploy a SPA made with Next14 on Flask
This is just a quick repo that I think maybe someone can find useful one day.

## Develop your SPA as always, but remember you can only use : 
- Dynamic Routes when using getStaticPaths
- Prefetching with next/link
- Preloading JavaScript
- Dynamic Imports
- Any styling options (e.g. CSS Modules, styled-jsx)
- Client-side data fetching
- getStaticProps
- getStaticPaths

## Build your app 
1. Modify `next.config.js` on your frontend project and add :
```
const nextConfig = {
    output: "export",
};
```

2. Build the app using `npm run build`
3. Move the `out` folder to your backend entry point.

## Configure Flask

Just use the template in this repo in `back/server.py` and modify the static proxy function.

## That's all! 👻