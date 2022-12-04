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

## Todo

- [ ] Add an examples section to the README with some actual examples with what it returns
- [ ] Add a clone and deploy button to Vercel
- [ ] Make a quick video where I simply show my terminal and curling two images
- [ ] Write a tweet to post this: "I built an image to text API! It takes in an image and outputs a 1 sentence description of it. Very useful for things like generating alt tags. Second link with a GitHub link to the examples to clone & deploy it, and mention we're going to use with image gallery"
- [ ] [Maybe] Make a "how I built an alt image generator API in 60 seconds" or "how I built an image -> text API in 2 minutes"
