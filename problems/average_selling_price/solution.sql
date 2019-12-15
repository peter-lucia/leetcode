# Write your MySQL query statement below
SELECT totals.product_id, ROUND(SUM(totals.total_spent) / SUM(totals.units), 2) as average_price FROM 
(SELECT UnitsSold.*, Prices.price, UnitsSold.units*Prices.price as total_spent #, SUM(Prices.price*UnitsSold.units) / UnitsSold.units as average_price
FROM UnitsSold
LEFT JOIN Prices ON (UnitsSold.purchase_date >= Prices.start_date 
AND UnitsSold.purchase_date <= Prices.end_date AND UnitsSold.product_id = Prices.product_id)) as totals
GROUP BY product_id