# Logs Analysis

## Prerequisites
* Python 3
* `psycopg2`
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant](https://www.vagrantup.com/downloads.html)


## Environment Setup
* Download the preconfigured [VM from Udacity](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/96869cfc-c67e-4a6c-9df2-9f93267b7be5/concepts/0b4079f5-6e64-4dd8-aee9-5c3a0db39840)
* Download SQL [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
* Extract VM configuration files
    * Navigate to the newly created directory and run `vagrant up` in terminal.
* Extract SQL data to the VM's `vagrant` directory
    * `cd` to `vagrant` directory and use the command `psql -d news -f newsdata.sql` to setup database.


## Data Preparation
* Run `psql news` to access database

### Run the following commands to create the necessary views

#### Query to run in order to create the `topauthors` view.

```sql
create view topauthors as
    select author, count(*) as views
    from articles join log
    on '/article/' || articles.slug = log.path
    where log.status like '%200%'
    group by author
    order by views desc;
```

#### Query to run in order to create the `successful` view.

```sql
create view successful as
    select cast (time as date) as date, count(*) as success
    from log
    where status like '%200%'
    group by date;
```

#### Query to run inorder to create the `failures` view.

```sql
create view failures as
    select cast (time as date) as date, count(*) as failure
    from log
    where status not like '%200%'
    group by date;
```


