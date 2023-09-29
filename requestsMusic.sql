select max(duration), name
from track
group by "name" limit 1

select name from track
where duration > 210

select name from collection
where extract(year from year) between 2018 and 2020

select name from artist
where name not like '% %'

select name
from track
where name like '%My%' or name like 'мой'


select id_genre, count(distinct id_artist) from genre_artist 
group by id_genre 


select count(track.id) from track where album_id in (select album.id from album
where "year" between 2019 and 2020)

select avg(duration) , album."name" from track 
inner join album on track.album_id = album.id
group by album."name" 


select distinct id_artist from artist_album 
where id_album in (select album.id from album where album."year"  != 2020)


select distinct id_collection, collection."name"  
from collection_track 
inner join collection on collection.id = id_collection
where id_track in (select id from track where album_id in (select id_album from artist_album where id_artist = 3))





