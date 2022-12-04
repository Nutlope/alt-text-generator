# Alt Image Generator

This project uses an ML modal called [BLIP](https://github.com/salesforce/BLIP) to generate relevant alt text for images. You can feed it an image as a query param.

## Example

For example, try running this in your terminal. It sends a request to this python serverless function on Vercel with an image passed as a query parameter.

```bash
curl https://alt-text-generator.vercel.app/generate\?imageUrl\=https://dub.sh/confpic
curl https://alt-text-generator.vercel.app/generate\?imageUrl\=https://res.cloudinary.com/dffajvipu/image/upload/v1667421698/nextjsconf-pics/Sexton_Vercel_0574_r8iabf.jpg


```

## Running Locally

```bash
npm i -g vercel
vercel dev
```

Your Flask application is now available at `http://localhost:3000`.
