import psycopg2

db = psycopg2.connect(dbname="news")

c = db.cursor()

c.execute("select a.title as title, count(b.ip) as views from articles as a inner join log as b on  b.path like concat('%', a.slug) group by a.title order by views DESC limit 3;")
result1 = c.fetchall()
print result1
c.execute("create view totalviews as select a.title as title, count(b.ip) as views, a.author as id from articles as a inner join log as b on b.path like concat('%', a.slug) group by a.title, a.author order by views DESC;")

c.execute("select c.name as author, sum(d.views) as total from authors as c join totalviews as d on c.id = d.id group by c.name order by total DESC limit 5;")
result2 = c.fetchall()
print result2
c.execute("create view fixed as SELECT status, concat(EXTRACT(year FROM time),'-',EXTRACT(MONTH FROM time),'-',EXTRACT(DAY FROM time)) as time from log;")

c.execute("create view request as select l.time as time, count(l.status) as total from fixed as l group by l.time;")

c.execute("create view error as select e.time as time, count(e.status) as total from fixed as e join request as f on e.time = f.time where e.status like '404 NOT FOUND' group by e.time, f.time;")

c.execute("create view combine as select err.time as time, cast(err.total as flat)/cast(req.total as float)*100 as percent from error as err join request as req on err.time=req.time;")

c.execute("select concat(time,'-', percent) from combine as t where percent > 1;")
db.commit()
result3 = c.fetchall()
print result3





