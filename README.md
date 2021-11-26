# Introduction
`main.py` allows you to download artifacts from https://europa-kids.com/

# Configuration
Create a file named `.env` in the same directory as `main.py` with the following contents:
```
BASE_URL=https://europa-kids.com
LOGIN_URL=https://europa-kids.com/wp-login.php
SER_URL=https://europa-kids.com/chislograd/zao/page/?ser=
LOGIN=
PASSWORD=
OUTPUT_DIR=
```

# Usage
Fill in your LOGIN, PASSWORD and OUTPUT_DIR in `.env`.
Run `main.py` using the command
```
python main.py
```