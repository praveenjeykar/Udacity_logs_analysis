# Udacity Logs Analysis Project
This project is a simple CLI reporting tool based on tables in a PostgreSQL database.

The tool runs three reports for answers to the following questions:
- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?

## Quick start

First you must have the PostgreSQL newsdata.sql database running from the FSND virtual machine.

- From the 'vagrant' directory, run ```vagrant up```.
- SSH to the virtual machine with ```vagrant ssh```.
- Connect to the psql database with ```psql -d news```
- We'll need to create two database views for the reporting tool to work properly:

```sql
CREATE view fourohfours as
  SELECT date_trunc('day', time) "day", count(status) as totals
  FROM log
  WHERE status = '404 NOT FOUND'
  GROUP by day;

CREATE view request_totals as
  SELECT date_trunc('day', time) "day", count(status) as totals
  FROM log
  GROUP by day;
```
- Provided the above views are created, you should be able to run the reporting tool as:
```bash
python reporter.py
```
- Win!

## What's what
The repo has only a few files:

- `reporter.py`: this is the main entrypoint for the application
- `db.py`: this encapsulates the database connection logic

## Example output
```bash
--- Three most popular articles of all time ---
Candidate is jerk, alleges rival -- 338647 views
Bears love berries, alleges bear -- 253801 views
Bad things gone, say good people -- 170098 views


--- Most popular authors of all time ---
Ursula La Multa -- 507594 views
Rudolf von Treppenwitz -- 423457 views
Anonymous Contributor -- 170098 views
Markoff Chaney -- 84557 views


--- More than 1% of requests lead to errors ---
07/17/2016 -- 2.26%
```
