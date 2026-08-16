import pandas as pd
from src.db import get_connection
from src.queries import QUERIES

def build_report(db_path='data/sales.db', output_path='outputs/sales_report.xlsx'):
    conn = get_connection(db_path)
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        for sheet_name, query in QUERIES.items():
            df = pd.read_sql(query, conn)
            df.to_excel(writer, sheet_name=sheet_name[:31], index=False)
    conn.close()
    print(f'Report saved to {output_path}')
