create table movies(id integer primary key, name text,
year integer, genre text, score integer);
.separator ","
.import Q3_movies.csv movies

create table actors(id integer primary key, name text);
.separator ","
.import Q3_actors.csv actors

create table cast(movie_id integer, actor_id integer, character_name text,
primary key (movie_id, actor_id));
.separator ","
.import Q3_cast.csv cast

create index movies_name_index on movies(name);
create index movies_score_index on movies(score); 

select genre, avg(score) from movies group by genre;
select '';
select id, name, year, score from movies where year >= 2011 and year <= 2014  order by score desc, name asc limit 10 ;
select actor_id, a.name, count(movie_id) as roles from cast c , actors a
        where c.actor_id = a.id   GROUP BY actor_id having roles >= 10 order by a.name ;
select actor_id, a.name, avg(score) as s, count(score)  from cast c , actors a, movies m where c.actor_id = a.id  and c.movie_id = m.id and score > 0  group by actor_id having count(score) >= 3 order by s desc limit 10 ;
select c1.actor_id as actor_id1 ,c2.actor_id as actor_id2, avg(m.score),count(m.id) from cast c1, cast c2 , movies m 
where c1.movie_id = c2.movie_id
and c1.actor_id != c2.actor_id
and  m.id = c1.movie_id 
and  m.id = c2.movie_id 
group by m.id having count(m.id) >= 2 and avg(m.score)  >= 75

create view good_collaboration as
select c1.actor_id as actor_id1 ,c2.actor_id as actor_id2, avg(m.score) as avg_movie_score ,count(m.id) as count_movie from cast c1 inner join cast c2 on( c1.movie_id = c2.movie_id and c1.actor_id != c2.actor_id) inner join movies m 
on( m.id = c1.movie_id )
group by m.id having count(m.id) >= 2 and avg(m.score)  >= 75;

select actor_id1 , name , avg(avg_movie_score) from good_collaboration, actors where actor_id1 = id group by actor_id1 order by avg(avg_movie_score) desc limit 5  ;
