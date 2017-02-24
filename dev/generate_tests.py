# -*- coding:utf-8 -*-
from pyquery import PyQuery
from collections import OrderedDict
from urlparse import urlparse
from json import dumps

v,e=[],[]
v1,e1=[],[]
et=[]
# COSTANTS
URL = "https://news.ycombinator.com/newest?"
POSTS_EACH_PAGE = 30
# --*---
# LOADS
# adding a method to PyQuery class in order to create a list of elements without id
fn = lambda: this.map(lambda i, el: PyQuery(this).outerHtml())
PyQuery.fn.listOuterHtml = fn
# --*--


def sanitize_url(host, sub_url):
    # converts relative uri into absolute uri
    parsed_sub_url = urlparse(sub_url)
    parsed_host = urlparse(host)
    if not parsed_sub_url.scheme:
        parsed_sub_url = parsed_sub_url._replace(scheme=parsed_host.scheme)
    if not parsed_sub_url.netloc:
        parsed_sub_url = parsed_sub_url._replace(netloc=parsed_host.netloc)
    return parsed_sub_url.geturl()


def scrape_top(fragment_str):
    global v1; v1.append(fragment_str)
    # parse the content of the '.athing' class
    # getting the fields id,title,uri,rank
    s = PyQuery(fragment_str)
    post_id = s.attr('id')
    title = s(".storylink").text()[:256]
    title = "None" if not title else title
    uri = sanitize_url(URL, s(".storylink").attr("href"))
    try:
        rank = int(s(".rank").text()[:-1])
    except:
        rank = 0
    global v
    v.append([post_id, title, uri, rank])
    return post_id, title, uri, rank



def scrape_subtitle(fragment_str):
    global e1;
    e1.append(fragment_str)
    # parse the content of the '.subtext' class
    # getting the fields author, post, comments
    s = PyQuery(fragment_str)
    author = s(".hnuser").text()[:256]
    author = "None" if not author else author
    try:
        points = int(s(".score").text().split()[0])
    except:
        points = 0
    try:
        comments = int(PyQuery(s("a").listOuterHtml()[3]).text()[:-9])
    except:
        comments = 0
    global e
    e.append([author, points, comments])
    return author, points, comments


def scrape_article(top_str, bot_str):
    # assemble and returns the fields gotten by calling the functions for the top and
    # the bottom part of the post label
    static_dict = OrderedDict()
    post_id, title, uri, rank = scrape_top(top_str)
    author, points, comments = scrape_subtitle(bot_str)
    static_dict["title"] = title
    static_dict["uri"] = uri
    static_dict["author"] = author
    static_dict["points"] = points
    static_dict["comments"] = comments
    static_dict["rank"] = rank
    global et
    et.append([post_id,static_dict])
    return post_id, static_dict


def acquire_hakernews_list(n):
    # takes as input the number of posts to acquire and goes page to page getting 30 elements
    # each time , then return the list of static dict each containing a post with its fields
    post_list = []
    path = ""
    for z in xrange(n / POSTS_EACH_PAGE + 1):
        if (n - (z * POSTS_EACH_PAGE))>0:
            # gets the page and init PyQuery
            s = PyQuery(url=URL + path)
            # creates two different lists, the "top" contains the upper part of each post
            top = s('.athing').listOuterHtml()
            # creates two different lists, the "sub_title" contains the lower part of each post
            sub_title = s('.subtext').listOuterHtml()
            # Saves the id of first in order to be sure to have the previous n posts from the current first post
            # then create the path the get the posts in the following page during next acquisition
            id_post, message = scrape_article(top[0], sub_title[0])
            if z == 0:
                id_str = id_post
            path = "next=" + id_str + "&n=" + str((z + 1) * POSTS_EACH_PAGE + 1)
            # Appends the first message of the page to the post_list and as well
            # acquire and append the remaining posts to acuire inside the page
            post_list.append(message)
            for i in xrange(1, min(POSTS_EACH_PAGE, n - z * POSTS_EACH_PAGE)):
                _, message = scrape_article(top[i], sub_title[i])
                post_list.append(message)
    return post_list

if __name__ == "__main__":

    acquire_hakernews_list(100)
    print 100
    fd1i=open("./hackernews_tests/tests_input/scrape_top_in", "w");fd1i.write("100\n"+'\n'.join(v1).encode("UTF-8"));fd1i.close()
    fd1i=open("./hackernews_tests/tests_input/scrape_subtitle_in", "w");fd1i.write("100\n"+'\n'.join(e1).encode(
        "UTF-8"));fd1i.close()
    fd1i=open("./hackernews_tests/tests_output/scrape_top_out", "w");
    fd1i.write('100\n'+'\n'.join([' '.join(map(unicode,item)).encode("utf-8") for item in v]));fd1i.close()
    fd1i=open("./hackernews_tests/tests_output/scrape_subtitle_out", "w");
    fd1i.write('100\n'+'\n'.join([' '.join(map(unicode,item)).encode("utf-8") for item in e]));fd1i.close()
    fd1i=open("./hackernews_tests/tests_output/scrape_article_out", "w");
    fd1i.write('100\n'+'\n'.join([' '.join(map(unicode,item)).encode("utf-8")for item in et]));fd1i.close()
