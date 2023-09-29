create table if not exists genre(
	id integer primary key,
	name varchar(60) not null
	);
create table if not exists artist(
	id integer primary key,
	name varchar(120) not null
	);
create table if not exists album(
	id integer primary key,
	name varchar(120) not null,
	year integer not null
	);
create table if not exists track(
	id integer primary key,
	name varchar(120) not null,
	duration integer not null,
	album_id integer references album(id)
	);
create table if not exists collection(
	id integer primary key,
	name varchar(120) not null,
	year date not null
	);
create table if not exists genre_artist(
	id_genre integer references genre(id),
	id_artist integer references artist(id),
	constraint pk_genre_artist primary key(id_genre, id_artist)
	);
create table if not exists artist_album(
	id_artist integer references artist(id),
	id_album integer references album(id),
	constraint pk_artist_album primary key(id_artist, id_album)
	);
create table if not exists collection_track(
	id_collection integer references collection(id),
	id_track integer references track(id),
	constraint pk_collection_track primary key(id_collection, id_track)
	);