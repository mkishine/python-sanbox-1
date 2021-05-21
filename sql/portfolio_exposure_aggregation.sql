SELECT sys_exposures.ftag, sum(weights.weight * sys_exposures.exp) as exposure_aggregate
from dbo.exp exposures, 
    dbo.sys as sys_exposures, 
    (
        SELECT cusip, sum(amount)/max(total_value) as weight
        from dbo.pos p, (SELECT sum(amount) as total_value
                from dbo.pos
                where pos_date='2019/09/27' and portfolio_name='MK-TEST-1'
            ) t2 
        group by cusip
    ) weights 
where exposures.e_cusip_id = sys_exposures.s_cusip_id
and exposures.cusip = weights.cusip
group by sys_exposures.ftag