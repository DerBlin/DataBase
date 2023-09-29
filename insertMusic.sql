insert into artist 
values
(1, 'MiyaGi'),
(2, 'Andy Panda'),
(3, 'Заточка'),
(4, 'Король и шут')

insert into album
values
(1, 'HATTORI', 2022),
(2, 'YAMAKASI', 2020),
(3, 'Умшакалака', 2017),
(4, 'Как в американском фильме', 2019),
(5, 'Вынь да полож', 2021),
(6, 'Камнем по голове', 1996)

insert into artist_album
values
(1, 2),
(2, 3),
(3, 4),
(3, 5),
(4, 6),
(2, 1)

insert into collection
values
(1, 'Смешанный рок', 2019-01-01),
(2, 'Рэп о любви', 2021-01-01),
(3, 'Классика панка', 2010-01-01),
(4, 'Альтернативный рэп', 2020-01-01)

insert into collection_track
values
(1, 5),
(1, 1),
(2, 8),
(2, 9),
(3, 1),
(3, 2),
(4, 4),
(4, 10),
(4, 6)

insert into genre
values 
(1, 'Рэп'),
(2, 'Рок'),
(3, 'Панк')

insert into genre_artist
values
(1, 1),
(1, 2),
(1, 3),
(2, 3),
(3, 4)

insert into track
values
(1, 'Смельчак и ветер', 181, 6),
(2, 'Внезапная голова', 145, 6),
(3, 'Нет карманов', 235, 4),
(4, 'Белый', 249, 4),
(5, 'Этажи', 208, 5),
(6, 'Держи в курсе', 250, 5),
(7, 'Временно', 225, 1),
(8, 'Tantra', 256, 2),
(9, 'Be My Sky', 278, 3),
(10, 'I Got My Way', 247, 3)








