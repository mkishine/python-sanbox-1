IF OBJECT_ID('dbo.pos', 'U') IS NOT NULL  
   DROP TABLE dbo.pos;  
GO

create table pos (
    portfolio_name char(10),
	pos_date date,
	cusip char(9),
	amount float
)
go
-- MK-TEST-1 portfolio
insert into dbo.pos values('MK-TEST-1', '2019-09-27', '00037BAB8', 100.0)
go
insert into dbo.pos values('MK-TEST-1', '2019-09-27', '00037BAC6', 100.0)
go

-- MK-TEST-2 portfolio
insert into dbo.pos values('MK-TEST-2', '2019-09-27', '00037BAB8', 1.0)
go
insert into dbo.pos values('MK-TEST-2', '2019-09-27', '00037BAC6', 2.0)
go
insert into dbo.pos values('MK-TEST-2', '2019-09-27', '00037BAE2', 3.0)
go
insert into dbo.pos values('MK-TEST-2', '2019-09-27', '00037BAF9', 4.0)
go
insert into dbo.pos values('MK-TEST-2', '2019-09-27', '001055AJ1', 5.0)
go
insert into dbo.pos values('MK-TEST-2', '2019-09-27', '001055AL6', 6.0)
go
insert into dbo.pos values('MK-TEST-2', '2019-09-27', '001055AM4', 7.0)
go
insert into dbo.pos values('MK-TEST-2', '2019-09-27', '001055AP7', 8.0)
go
insert into dbo.pos values('MK-TEST-2', '2019-09-27', '001055AQ5', 9.0)
go
insert into dbo.pos values('MK-TEST-2', '2019-09-27', '001055AR3', 10.0)
go
