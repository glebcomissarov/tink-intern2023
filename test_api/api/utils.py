import duckdb


def create_database(save_to_json=False):
    """
    Create purchases database
    """
    con = duckdb.connect(database="./test_api/purchases_data.duckdb", read_only=False)

    con.execute(
        """
        DROP TABLE IF EXISTS purchases;

        CREATE TABLE IF NOT EXISTS purchases (
            purchase_id INTEGER,
            purchase_date TIMESTAMP,
            bank_id INTEGER,
            category_id INTEGER,
            product_id INTEGER,
            product_price REAL,
        );

        INSERT INTO purchases
        VALUES
            (1, '2023-03-20 10:00:00', 1, 100, 1, 2500.30),
            (2, '2023-03-20 10:30:00', 1, 25, 17, 5700.00),
            (3, '2023-03-20 11:35:00', 1, 25, 20, 3500.00),
            (4, '2023-03-20 11:40:00', 1, 100, 1, 2500.30),
            (5, '2023-03-20 15:05:00', 1, 100, 5, 200.00);
        """
    )
    print("Database './test_api/purchases_data.duckdb' has been created")
    print(con.sql("SHOW TABLES;"))

    if save_to_json:
        con.execute("COPY (SELECT * FROM purchases) TO './test_api/purchases.json';")


def get_json():
    con = duckdb.connect(database="./test_api/purchases_data.duckdb", read_only=True)
    # con.sql("SELECT * FROM purchases").df().to_json(orient="records")
    return con.sql("SELECT * FROM purchases").df().to_json(orient="records")


if __name__ == "__main__":
    create_database()
