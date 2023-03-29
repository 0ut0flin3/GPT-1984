# ScrapeGPT

This Python script logs into openai.com bypassing the Cloudflare captcha, goes to chatgpt , write a prompt and print the response





To use it you will need:
1) Have Chrome installed
2) Change your email and password to yours inside the script



After that:

`git clone https://github.com/0ut0flin3/GPT-1984.git`

`cd GPT-1984/ScrapeGPT`

`pip install -r requirements.txt`

`python3 app.py "hello, what are you doing?"`

The response will be printed on the console at the end of the procedure.
It works perfectly 90% of the time, but sometimes it crashes for some reason.

Below I suggest some very simple PHP code that calls the Python crypt, takes the prompt sent by the client and sends it the response:
```php
<?php

$prompt=$_GET["prompt"];

$response=shell_exec('python3 /path/to/app.py "'.$prompt.'"');

echo $response;

?>
```

in this way a client can communicate with ChatGPT simply with : `curl www.yoursite.com/index.php?prompt=hello`

