# passgen

Simple Python / Tkinter password generator.

This is obviously not packaged, but can be run from Python Shell or however you normally run python scripts.

Requires TK, which nearly all modern python packages come with, but otherwise, run "pip install tk" to get it.

This uses urllib to grab words from a webpage and pulls them into the password if desired.
You can dictate which page it is going to grab from by swapping word_url variable out for an approriate parsable page

IMPORTANT: This is not secured, everything is generated in plain text. Do not use this in production.
![dictpassgen](https://user-images.githubusercontent.com/30908995/155023164-205dbb40-12eb-4dde-8887-3fa53354517b.png)
