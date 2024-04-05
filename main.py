import sys
import asyncio
from database import fetch_orders_by_names
from utils import organize_data, print_grouped_data

async def main():
    if len(sys.argv) > 1:        
        order_names = sys.argv[1].split(',')
        order_names = [name.strip() for name in order_names]
    else:
        print("Укажите номера интересующих Вас заказов через запятую без пробелов!")
        sys.exit(1)    
    
    orders = await fetch_orders_by_names(order_names)

    grouped_data = organize_data(orders)

    print_grouped_data(grouped_data, order_names)


if __name__ == "__main__":
    asyncio.run(main())