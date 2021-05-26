IF OBJECT_ID('dbo.portfolio_sys_exposures', 'IF') IS NOT NULL
    DROP FUNCTION dbo.portfolio_sys_exposures
GO
 
CREATE FUNCTION dbo.portfolio_sys_exposures(@portfolio_name CHAR(10), @date DATE)
    RETURNS TABLE AS RETURN(
        SELECT sys_exposures.ftag, sum(weights.weight * sys_exposures.exp) as exposure_aggregate
        from dbo.sys as sys_exposures, 
            (
                SELECT exposures.e_cusip_id as cusip_id, sum(amount)/max(total_value) as weight
                from dbo.pos positions, (SELECT sum(amount) as total_value
                        from dbo.pos
                        where pos_date=@date and portfolio_name=@portfolio_name
                    ) total, 
                    dbo.exp exposures 
                where exposures.cusip = positions.cusip
                    and positions.pos_date=@date
                    and positions.portfolio_name=@portfolio_name
                group by exposures.e_cusip_id) as weights
        where weights.cusip_id = sys_exposures.s_cusip_id
        group by sys_exposures.ftag
    )

GO
SELECT * FROM dbo.portfolio_sys_exposures('MK-TEST-1', '2019/09/27')