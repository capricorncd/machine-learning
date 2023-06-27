import { createServer } from 'http'
import { URL } from 'url'

const PORT = 3000

const app = createServer((req, res) => {
  const url = new URL(req.url, `http://localhost:${PORT}`)
  console.log(url.pathname, url.searchParams, url.searchParams.get('keyword'))

  res.end(JSON.stringify([
    'Salmon', 
    'Xiao Long Bao', 
    'Twice Cooked Pork',
    url.searchParams.get('keyword') || 'Lanzhou noodles'
  ]))
})

app.listen(PORT, (err, res) => {
  console.log(`http://localhost:${PORT}`)
})