import aiopg
from config import DB_CONFIG, QUERIES


async def fetch_orders_by_names(order_names):
    async with aiopg.create_pool(DB_CONFIG['dsn']) as pool:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(QUERIES['fetch_orders'], (order_names,))
                return await cur.fetchall()