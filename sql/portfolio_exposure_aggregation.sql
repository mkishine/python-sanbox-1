SELECT sys_exposures.ftag, sum(weights.weight * sys_exposures.exp) as exposure_aggregate
from dbo.sys as sys_exposures, 
    (
        SELECT exposures.e_cusip_id as cusip_id, sum(amount)/max(total_value) as weight
        from dbo.pos positions, (SELECT sum(amount) as total_value
                from dbo.pos
                where pos_date='2019/09/27' and portfolio_name='MK-TEST-1'
            ) total, 
            dbo.exp exposures 
        where exposures.cusip = positions.cusip
            and positions.pos_date='2019/09/27' 
            and positions.portfolio_name='MK-TEST-1'
        group by exposures.e_cusip_id) as weights
where weights.cusip_id = sys_exposures.s_cusip_id
group by sys_exposures.ftag