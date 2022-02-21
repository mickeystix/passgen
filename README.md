# passgen-expanded

Python / Tkinter password generator.

This is not packaged, but can be run from Python Shell or however you normally run python scripts.

Requires TK, which nearly all modern python packages come with, but otherwise, run "pip install tk" to get it.

This uses urllib to grab words from a webpage and pulls them into the password if desired.
You can dictate which page it is going to grab from by swapping word_url variable out for an appropriate parsable page

IMPORTANT: This is not secured, everything is generated in plain text. Do not use this in production if security is important to you.

Includes a basic notepad, some debug information (Length checks) further exception handling and criteria enforcement, link to Git repo



![pge](https://user-images.githubusercontent.com/30908995/155036348-eed31a5d-9371-4875-9ff9-0fd38e6c2279.png)
