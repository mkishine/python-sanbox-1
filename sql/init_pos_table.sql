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

insert into dbo.pos values('MK-TEST-1', '2019-09-27', '00037BAB8', 100.0)
go
insert into dbo.pos values('MK-TEST-1', '2019-09-27', '00037BAC6', 100.0)
go