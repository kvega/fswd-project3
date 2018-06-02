# Logs Analysis

## Query to run in order to create the `topauthors` view.

```sql
create view topauthors as
    select author, count(*) as views
    from articles join log
    on '/article/' || articles.slug = log.path
    where log.status like '%200%'
    group by author
    order by views desc;
```

## Query to run in order to create the `successful` view.

```sql
create view successful as
    select cast (time as date) as date, count(*) as success
    from log
    where status like '%200%'
    group by date;
```

## Query to run inorder to create the `failures` view.

```sql
create view failures as
    select cast (time as date) as date, count(*) as failure
    from log
    where status not like '%200%'
    group by date;
```


