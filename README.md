## Hacker News scraper

This is a scraper for the [Hacker News](https://news.ycombinator.com/) site.

## Getting Started

Clone the project in any path you wish

```
git clone https://github.com/LucaPaterlini/TL_LucaPaterlini.git

```

or Download the zip and extract the files in the directory.


### Installing


In order to run the project without installing it this is the prerequisite list:

1. libc-dev
2. gcc
3. libxslt-dev
4. libxml2-dev
5. python-dev
6. pip
7. lxml
8. pyquery
9. rfc3986

If you wish to install the program on your machine also bash/ash is needed.
Instead if you will install it into a container only docker is needed.

### USAGE

If you have made all the previus installation needed to run the project without a container now you are able to do.

./hackernews --posts n

Where n is the number of the lasts post you want to show in json format as STDOUT.

If you want to make the project available to every user open
the directory that has been previously downloaded.

```
./setup.sh

```
Root priviledge are required.


Then you will be able to do

```
hackernews --posts n 

```
Where n is the number of the lasts post you want to show in json format as STDOUT.

If you want to install into the container [Docker](https://docs.docker.com/engine/installation/) is require and as well Root priviledges are required.

Go into the installing dir

```
cd dockerbuild

```

Build the container

```
docker build -t hackernews .

```

Run it and also the image as well

```
docker run -ti hackernews

```

Now inside the container you are allowed to run

```
hackernews --posts n 

```
Where n is the number of the lasts post you want to show in json format as STDOUT.


## Testing 

In order to test the project before running it run the following command inside the project folder

```
python -m unittest discover -s hackernews_tests/ -p "*test.py" -v
```