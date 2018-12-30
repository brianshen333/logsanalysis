#!/bin/python

import psycopg2

db = psycopg2.connect(dbname="news")
c = db.cursor()
c.execute("""select concat(title ,'-', views,'views') from
    (select a.title as title, count(b.ip) as views from
    articles as a inner join log as b on b.path like concat('%', a.slug)
     group by a.title order by views DESC limit 3) as final;""")

result1 = c.fetchall()

print "1. What are the most popular three articles of all time?"
print "---------------------------------------------------------"
for i in result1:
    print i[0]

c.execute("""select concat(author ,'-', total,' views')
    from (select c.name as author, sum(d.views) as total
    from authors as c join (select a.title as title, count(b.ip)
    as views, a.author as id from articles as a inner join log as
    b on b.path like concat('%', a.slug) group by a.title, a.author
    order by views DESC) as d on c.id = d.id group by c.name order
     by total DESC limit 5) as final""")
result2 = c.fetchall()

print "2. Who are the most popular articles authors of all time?"
print "---------------------------------------------------------"
for i in result2:
    print i[0]


c.execute("""select concat(time,'-', percent,'%')
    from (select err.time as time,
    cast(cast(err.total as float)/cast(req.total as float)*100 as
    decimal(18,2)) as percent from
     (select e.time as time, count(e.status) as total
    from fixed as e where e.status like
     '404 NOT FOUND' group by e.time) as err join
    (select l.time as time, count(l.status) as
     total from fixed as l  group by l.time)
     as req on err.time=req.time) as t where percent > 1;""")

db.commit()

result3 = c.fetchall()

print "3. On which days did more than 1% of requests lead to errors?"

print "---------------------------------------------------------"

for i in result3:
    print i[0]