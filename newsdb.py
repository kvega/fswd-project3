#!/usr/bin/env python3

import psycopg2
import bleach

DBNAME = "news"

def get_pop_articles():
    """Returns the three articles with the highest number of views."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select title, count(*) as views " +
        "from articles join log " +
        "on '/article/' || articles.slug = log.path " +
        "group by title " +
        "order by views desc " +
        "limit 3;")
    top_articles = c.fetchall()
    db.close()
    return top_articles


def get_pop_authors():
    """Return the three authors with the highest number of views."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select name, views " +
        "from authors join topauthors " +
        "on authors.id = topauthors.author;")
    top_authors = c.fetchall()
    db.close()
    return top_authors


def get_error_days():
    """Returns the dates of days on which more than 1% of requests lead to 
    errors"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select successful.date, success, failure, " +
        "((cast (failure as decimal) / success) * 100) as percent " +
        "from successful join failures " +
        "on successful.date = failures.date " +
        "where ((cast (failure as decimal) / success) * 100) > 1;")
    high_errors = c.fetchall()
    db.close()
    return high_errors


