const express = require('express');
const port = 8080;

const app = express();

app.route('/')
  .get((req, res) => res.send([
    'I think you look weird.',
    'Your leg very ugly.'
  ]))
  .post((req, res) => {
    console.log(`Emotion rating received`);
  })
app.listen(port);