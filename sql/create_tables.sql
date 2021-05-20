/*
This script creates all tables for POC

Implementation Notes.
Char is faster than varchar for join: https://www.sqlshack.com/sql-varchar-data-type-deep-dive/
*/

IF OBJECT_ID(N'dbo.exp2', N'U') IS NOT NULL  
   DROP TABLE [dbo].[exp2];  
GO

IF OBJECT_ID(N'dbo.sys2', N'U') IS NOT NULL  
   DROP TABLE [dbo].[exp2];  
GO

CREATE TABLE exp2
	(
	 [e_cusip_id] int,
	 [cusip] char(9),
	 [dt] date,
	 [purpose] char(10),
	 [base_ccy] char(3),
	 [mkt_value] float,
	 [notional] float
	)
GO

CREATE TABLE sys2
	(
	 [s_cusip_id] int,
	 [fid] int,
	 [exp] float
	)
GO
