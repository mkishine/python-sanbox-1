SELECT cusip, sum(amount)/max(total_value) as weight
from dbo.pos p, (SELECT sum(amount) as total_value
        from dbo.pos
        where pos_date='2019/09/27' and portfolio_name='MK-TEST-1'
    ) t2 
group by cusip