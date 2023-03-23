Usage
-----

Each scraper will scrape a "chunk" of data.

A "chunk" is a file (see chunk0, etc) with a list of post IDs, one per line.

The chunks in this repo represent sets of files I have not yet saved.

Each chunk should take 12 hours to download at the current ratelimit on each machine.

I recommend using one process per machine on multiple machines. The outputs can be combined 
at the end by simply merging directories.
