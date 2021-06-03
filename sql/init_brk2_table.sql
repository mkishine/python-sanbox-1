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

insert into brk2
select breakdown_name, cusip, level_1, 1 from dbo.breakdown;
go

insert into brk2
select breakdown_name, cusip, concat (level_1, '.', level_2), 2 from dbo.breakdown
where level_2 is not null;
go

insert into brk2
select breakdown_name, cusip, concat (level_1, '.', level_2, '.', level_3), 3 from dbo.breakdown
where level_3 is not null;
go

insert into brk2
select breakdown_name, cusip, concat (level_1, '.', level_2, '.', level_3, '.', level_4), 4 from dbo.breakdown
where level_4 is not null;
go