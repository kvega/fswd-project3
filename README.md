# Logs Analysis

## Query to run in order to create the `topauthors` view.

```postgresql
create view topauthors as
    select author, count(*) as views
    from articles join log
    on '/article/' || articles.slug = log.path
    where log.status like '%200%'
    group by author
    order by views desc
    limit 3;
```
