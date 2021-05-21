IF
OBJECT_ID('dbo.portfolio_sys_exp', 'IF') IS NOT NULL
DROP FUNCTION dbo.portfolio_sys_exp
    GO

CREATE FUNCTION dbo.portfolio_sys_exp(@portfolio_name CHAR(10), @date DATE)
    RETURNS TABLE AS
RETURN(
SELECT fid, sum(p.amount * s.exp / e.notional) as exp
FROM dbo.sys2 s,
     dbo.exp2 e,
     dbo.pos p
WHERE s.s_cusip_id = e.e_cusip_id
  AND e.cusip = p.cusip
  AND e.dt = p.pos_date
  AND p.portfolio_name = @portfolio_name
  AND p.pos_date = @date
GROUP BY fid
)
GO

-- SELECT top 10 * from dbo.portfolio_sys_exp('MK-TEST-1', '2019-09-27')
-- where fid < 10
-- GO
