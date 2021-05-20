/*
Run this in Synapse Analytics
*/

COPY INTO exp2
(e_cusip_id 1, cusip 2, dt 3, purpose 4, base_ccy 5, mkt_value 6, notional 7)
FROM 'https://portrisksynapseaccount.dfs.core.windows.net/portrisksynapsefilesystem/upload-20210517/Exp.csv'
WITH
(
	FILE_TYPE = 'CSV'
	,MAXERRORS = 0
	,FIRSTROW = 2
	,ERRORFILE = 'https://portrisksynapseaccount.dfs.core.windows.net/portrisksynapsefilesystem/upload-20210517/'
	,IDENTITY_INSERT = 'OFF'
)
GO

COPY INTO sys2
(s_cusip_id 1, fid 2, exp 3)
FROM 'https://portrisksynapseaccount.dfs.core.windows.net/portrisksynapsefilesystem/upload-20210517/Sys.csv'
WITH
(
	FILE_TYPE = 'CSV'
	,MAXERRORS = 0
	,FIRSTROW = 2
	,ERRORFILE = 'https://portrisksynapseaccount.dfs.core.windows.net/portrisksynapsefilesystem/upload-20210517/'
	,IDENTITY_INSERT = 'OFF'
)
GO
