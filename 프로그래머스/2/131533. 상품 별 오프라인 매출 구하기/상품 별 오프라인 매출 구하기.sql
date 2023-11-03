select a.PRODUCT_CODE, SUM(a.price*b.sales_amount)as SALES
from product a
     inner join offline_sale b on a.product_id = b.product_id
group by a.product_code
order by 2 desc,1