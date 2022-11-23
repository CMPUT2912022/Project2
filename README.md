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

## Search for articles
With two keywords k1 and k2, we will consider it a match if k1 appears in any of the fields title, authors, abstract, venue and year and k2 appears in any of the same fields. They don't have to appear in the same field for a match. [ref](https://eclass.srv.ualberta.ca/mod/forum/discuss.php?d=2123952)

