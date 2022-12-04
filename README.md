# Alt Image Generator

This project uses an ML modal called [BLIP](https://github.com/salesforce/BLIP) to generate relevant alt text for images. You can feed it an image as a query param and it will return a one sentence description of that image.

## Running the demo

Try running this in your terminal or navigating to that URL in your browser. It sends a request to the serverless function in `api/index.py` with an image passed as the query parameter and returns a one sentence description of that image.

```bash
curl https://alt-text-generator.vercel.app/generate?imageUrl=https://dub.sh/confpic
```

## Running Locally

After cloning the repo, go to [Replicate](https://replicate.com/) to make an account and put your API key in `.env`.

Then, run the following in the command line and your application will be available at `http://localhost:3000`

```bash
npm i -g vercel
vercel dev
```

## Querying locally

Go to the link below in your browser or run a curl command in your terminal.

```bash
curl http://localhost:3000/generate?imageUrl=https://dub.sh/confpic
```
