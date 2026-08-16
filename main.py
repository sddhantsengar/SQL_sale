import os
from data.generate_data import generate
from src.report import build_report

def main():
    os.makedirs('outputs', exist_ok=True)
    if not os.path.exists('data/sales.db'):
        generate()
    build_report()

if __name__ == '__main__':
    main()
