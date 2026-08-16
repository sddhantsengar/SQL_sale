SELECT category, SUM(revenue) AS total_revenue, SUM(quantity) AS total_quantity
FROM sales
GROUP BY category
ORDER BY total_revenue DESC;

SELECT store, SUM(revenue) AS total_revenue
FROM sales
GROUP BY store
ORDER BY total_revenue DESC;

SELECT strftime('%Y-%m', sale_date) AS month, SUM(revenue) AS total_revenue
FROM sales
GROUP BY month
ORDER BY month;

SELECT product, SUM(revenue) AS total_revenue, SUM(quantity) AS total_quantity
FROM sales
GROUP BY product
ORDER BY total_revenue DESC
LIMIT 10;

SELECT store, category, SUM(revenue) AS total_revenue
FROM sales
GROUP BY store, category
ORDER BY store, total_revenue DESC;
