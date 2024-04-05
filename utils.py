def organize_data(records):
    grouped_data = {}
    for record in records:        
        order_name, storage_name, product_name, product_id, quantity, extra_storages = record
        if storage_name not in grouped_data:
            grouped_data[storage_name] = []
        grouped_data[storage_name].append((product_name, product_id, order_name, quantity, extra_storages))
    return grouped_data

def print_grouped_data(grouped_data, order_names):
    print("\n=+=+=+=\nСтраница сборки заказов", ",".join(order_names))
    for storage, products in grouped_data.items():
        print(f"\n===Стеллаж {storage}")
        for i, product in enumerate(products):
            product_name, product_id, order_name, quantity, extra_storages = product
            extra_storages_str = f"доп стеллаж: {extra_storages}" if extra_storages else ""
            print(f"{product_name} (id={product_id})\nзаказ {order_name}, {quantity} шт \n{extra_storages_str}".strip())
            if i < len(products) - 1:
                print()
