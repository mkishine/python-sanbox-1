IF OBJECT_ID('dbo.brk2', 'U') IS NOT NULL
DROP TABLE dbo.brk2;
GO

create table brk2 (
    name char(10)
    ,cusip char(9)
    ,level_tag varchar(65)
    ,lvl int
);
go
