import pandas as pd
from sqlalchemy import create_engine, text
import sqlalchemy.exc

# Create database connection
engine = create_engine("mysql+pymysql://root:leon1824@localhost/coffee_insights_db")

try:
    # Check if tables exist and drop them in reverse order of dependencies
    with engine.connect() as connection:
        # First check if tables exist to avoid errors when dropping non-existent tables
        result = connection.execute(text("SHOW TABLES"))
        existing_tables = [row[0] for row in result]

        # Drop tables in reverse order of dependencies
        if 'customer_feedback' in existing_tables:
            connection.execute(text("DROP TABLE customer_feedback"))
            print('Dropped customer_feedback table')

        if 'sales' in existing_tables:
            connection.execute(text("DROP TABLE sales"))
            print('Dropped sales table')

        if 'stores' in existing_tables:
            connection.execute(text("DROP TABLE stores"))
            print('Dropped stores table')

        if 'products' in existing_tables:
            connection.execute(text("DROP TABLE products"))
            print('Dropped products table')

    # Now create and load tables in the correct order

    # 1. First load products (no foreign key dependencies)
    products = pd.read_csv('data/products.csv')
    products.to_sql('products', con=engine, if_exists='append', index=False)
    print('Products data loaded successfully')

    # 2. Then load stores (no foreign key dependencies)
    stores = pd.read_csv('data/stores.csv')
    stores.to_sql('stores', con=engine, if_exists='append', index=False)
    print('Stores data loaded successfully')

    # 3. Then load sales (depends on products and stores)
    sales = pd.read_csv('data/sales.csv')
    sales.to_sql('sales', con=engine, if_exists='append', index=False)
    print('Sales data loaded successfully')

    # 4. Finally load customer feedback (depends on stores)
    feedback = pd.read_csv('data/customer_feedback.csv')
    feedback.to_sql('customer_feedback', con=engine, if_exists='append', index=False)
    print('Customer feedback data loaded successfully')

    print('All data loaded successfully! You can now aggregate data in your database.')
except sqlalchemy.exc.IntegrityError as e:
    print(f"Error: Database integrity error - {e}")
    print("This might be due to foreign key constraints or duplicate primary keys.")
except Exception as e:
    print(f"Error: {e}")
