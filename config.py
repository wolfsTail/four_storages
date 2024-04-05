import os

from dotenv import load_dotenv


load_dotenv()

DB_CONFIG = {
    'dsn': (
        f"dbname={os.getenv('DB_NAME')} "
        f"user={os.getenv('DB_USER')} "
        f"password={os.getenv('DB_PASSWORD')} "
        f"host={os.getenv('DB_HOST')}"
    ),
}

QUERIES = {
    'fetch_orders': """
        SELECT
            o.name AS order_name,
            s.name AS storage_name,
            p.name AS product_name,
            p.id AS product_id,
            oi.quantity,
            COALESCE(extra_storages, '') AS extra_storages
        FROM
            order_item oi
        JOIN
            "order" o ON oi.order_id = o.id
        JOIN
            product p ON oi.product_id = p.id
        JOIN
            order_item_storage ois ON oi.id = ois.order_item_id AND ois.is_primary = TRUE
        JOIN
            storage s ON ois.storage_id = s.id
        LEFT JOIN (
            SELECT
                order_item_id,
                STRING_AGG(s.name, ', ') AS extra_storages
            FROM
                order_item_storage ois
            JOIN
                storage s ON ois.storage_id = s.id
            WHERE
                ois.is_primary = FALSE
            GROUP BY
                order_item_id
        ) AS extras ON oi.id = extras.order_item_id
        WHERE
            o.name = ANY(%s)
        ORDER BY
            o.name, s.name, p.name;
    """,
}