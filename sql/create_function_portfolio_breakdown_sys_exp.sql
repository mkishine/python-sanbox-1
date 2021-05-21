IF
OBJECT_ID('dbo.portfolio_breakdown_sys_exp', 'IF') IS NOT NULL
DROP FUNCTION dbo.portfolio_breakdown_sys_exp
    GO

CREATE FUNCTION dbo.portfolio_breakdown_sys_exp(@portfolio_name CHAR(10), @date DATE, @breakdown_name char(10))
    RETURNS TABLE AS
RETURN(
SELECT distinct s.fid, b.level_1, b.level_2, b.level_3, b.level_4, sum(p.amount * s.exp / e.notional) as exp
FROM dbo.sys2 s,
     dbo.exp2 e,
     dbo.pos p,
     dbo.breakdown b
WHERE s.s_cusip_id = e.e_cusip_id
  AND e.cusip = p.cusip
  AND e.dt = p.pos_date
  AND p.cusip = b.cusip
  AND p.portfolio_name = @portfolio_name
  AND p.pos_date = @date
  AND b.breakdown_name = @breakdown_name
GROUP BY ROLLUP(s.fid, b.level_1, b.level_2, b.level_3, b.level_4)
)
GO

-- select * from dbo.portfolio_breakdown_sys_exp('MK-TEST-1', '2019-09-27', '4P')
-- where fid < 3