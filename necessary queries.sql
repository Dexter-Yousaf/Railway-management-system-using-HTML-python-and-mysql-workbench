-- SELECT * FROM schedule where schedule.arival_time > '16:00:00';
-- select * from station
-- select (count(station_ID in (1,4)) -1)*100 as fare from schedule as sh 
-- inner join train as tr
-- on sh.train_ID = tr.train_ID where tr.train_Id = 2 
 -- Select station_ID from schedule where train_ID = 2
 SELECT (COUNT(station_ID) -1) *100 as fare
FROM station
WHERE station_ID BETWEEN (
    SELECT station_ID FROM station where station_name = 'Station one'
) AND (
    SELECT station_ID FROM station WHERE station_name = 'Station four'
);

