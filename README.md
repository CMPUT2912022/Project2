# Project2
CMPUT291 Mini-project 2

## Starting database in background
```bash
mongod --port 1111 --dbpath /Users/<USER>/Desktop/db_temp
```

## Initializing database (phase 1)
```bash
python load_json.py dblp-ref-10.json 1111 
```
