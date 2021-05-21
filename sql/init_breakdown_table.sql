IF OBJECT_ID('dbo.breakdown', 'U') IS NOT NULL
DROP TABLE dbo.breakdown;
GO

create table breakdown (
    breakdown_name char(10),
    cusip char(9),
    level_1 varchar(50),
    level_2 varchar(50),
    level_3 varchar(50),
    level_4 varchar(50)
)
go

insert into dbo.breakdown values('RATING', '00037BAB8', 'AAA', null, null, null)
go
insert into dbo.breakdown values('RATING', '00037BAC6', 'AA', null, null, null)
go
insert into dbo.breakdown values('RATING', '00037BAE2', 'AA', null, null, null)
go
insert into dbo.breakdown values('RATING', '00037BAF9', 'A', null, null, null)
go
insert into dbo.breakdown values('RATING', '001055AJ1', 'A', null, null, null)
go
insert into dbo.breakdown values('RATING', '001055AL6', 'BBB', null, null, null)
go
insert into dbo.breakdown values('RATING', '001055AM4', 'BBB', null, null, null)
go
insert into dbo.breakdown values('RATING', '001055AP7', 'BBB', null, null, null)
go
insert into dbo.breakdown values('RATING', '001055AQ5', 'B', null, null, null)
go
insert into dbo.breakdown values('RATING', '001055AR3', 'CCC', null, null, null)
go

insert into dbo.breakdown values('4P', '00037BAB8', 'Corporates', 'Financial Institutions', 'Banking', null)
go
insert into dbo.breakdown values('4P', '00037BAC6', 'Corporates', 'Financial Institutions', 'Insurance', 'Health Insurance')
go
insert into dbo.breakdown values('4P', '00037BAE2', 'Corporates', 'Financial Institutions', 'Insurance', 'Health Insurance')
go
insert into dbo.breakdown values('4P', '00037BAF9', 'Corporates', 'Financial Institutions', 'Insurance', 'Life Insurance')
go
insert into dbo.breakdown values('4P', '001055AJ1', 'Corporates', 'Industrial', 'Basic Industry', 'Paper')
go
insert into dbo.breakdown values('4P', '001055AL6', 'Corporates', 'Industrial', 'Basic Industry', 'Paper')
go
insert into dbo.breakdown values('4P', '001055AM4', 'Corporates', 'Industrial', 'Basic Industry', 'Paper')
go
insert into dbo.breakdown values('4P', '001055AP7', 'Government Related', 'Local Authority', null, null)
go
insert into dbo.breakdown values('4P', '001055AQ5', 'Government Related', 'Local Authority', null, null)
go
insert into dbo.breakdown values('4P', '001055AR3', 'Government Related', 'Supranational', null, null)
go
