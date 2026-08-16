QUERIES = {
    'revenue_by_category': '''
        SELECT category, SUM(revenue) AS total_revenue, SUM(quantity) AS total_quantity
        FROM sales
        GROUP BY category
        ORDER BY total_revenue DESC
    ''',
    'revenue_by_store': '''
        SELECT store, SUM(revenue) AS total_revenue
        FROM sales
        GROUP BY store
        ORDER BY total_revenue DESC
    ''',
    'monthly_trend': '''
        SELECT strftime('%Y-%m', sale_date) AS month, SUM(revenue) AS total_revenue
        FROM sales
        GROUP BY month
        ORDER BY month
    ''',
    'top_products': '''
        SELECT product, SUM(revenue) AS total_revenue, SUM(quantity) AS total_quantity
        FROM sales
        GROUP BY product
        ORDER BY total_revenue DESC
        LIMIT 10
    ''',
    'store_category_breakdown': '''
        SELECT store, category, SUM(revenue) AS total_revenue
        FROM sales
        GROUP BY store, category
        ORDER BY store, total_revenue DESC
    '''
}
