#!/usr/bin/env python3

import psycopg2
import datetime

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
    print("\n")
    for article in top_articles:
        print(article[0] + " ---- " + str(article[1]) + " views")
    print("\n")    
    

def get_pop_authors():
    """Return the three authors with the highest number of views."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select name, views " +
        "from authors join topauthors " +
        "on authors.id = topauthors.author;")
    top_authors = c.fetchall()
    db.close()
    print("\n")
    for author in top_authors:
        print(author[0] + " ---- " + str(author[1]) + " views")
    print("\n")

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
    print("\n")
    for error in high_errors:
        # Extract date to format it
        fdt = error[0].strftime('%B %d, %Y')
        print(fdt + ' ---- ' + str(round(error[3], 1)) + '%')
    print("\n")        


def main():
	print("Welcome to Log Analysis!\n")
	while True:
		opt = int(input("Please select one of the following options:\n" +
        " 1 - Get list of the top three most viewed articles\n" +
        " 2 - Get list of authors sorted by popularity\n" +
        " 3 - Check days on which more than 1% of requests lead to errors\n" +
        " 4 - Exit the program\n\n" +
        "===> "))

		if type(opt) != int or opt not in [1,2,3,4]:
			print("Invalid option! Please enter a valid option.")
    
		options = {1: get_pop_articles,
               	   2: get_pop_authors,
               	   3: get_error_days}
               
		options[opt]()
	
	
if __name__ == '__main__':
    main()
