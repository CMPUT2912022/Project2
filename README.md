# Project2
CMPUT291 Mini-project 2


## Starting MongoDB as a background process (MacOS)
```bash
# Intel
mongod --config /usr/local/etc/mongod.conf --fork
```
```bash
# M1
mongod --config /opt/homebrew/etc/mongod.conf --fork
```

## Starting MongoDB on a specific port
```bash
mongod --port 27012 --dbpath ~/mongodb_data_folder &
```
