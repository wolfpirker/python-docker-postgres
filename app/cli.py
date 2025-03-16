class CLI:
    def __init__(self, conn):
        self.conn = conn

    def run(self):
        while True:
            print("\nChoose an option:")
            print("1. Add a new user")
            print("2. Add a new order for an existing user")
            print("3. List all users")
            print("4. List all orders for a specific user")
            print("5. List all products")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_user()
            elif choice == '2':
                self.add_order()
            elif choice == '3':
                self.list_users()
            elif choice == '4':
                self.list_orders()
            elif choice == '5':
                self.list_products()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    def add_user(self):
        name = input("Enter user's name: ")
        email = input("Enter user's email: ")
        with self.conn.cursor() as cur:
            cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
            self.conn.commit()
        print("User added successfully.")

    def add_order(self):
        user_id = input("Enter user ID: ")
        order_date = input("Enter order date (YYYY-MM-DD): ")
        with self.conn.cursor() as cur:
            cur.execute("INSERT INTO orders (user_id, order_date) VALUES (%s, %s) RETURNING id", (user_id, order_date))
            order_id = cur.fetchone()[0]
            while True:
                product_id = input("Enter product ID (or 'done' to finish): ")
                if product_id == 'done':
                    break
                quantity = input("Enter quantity: ")
                cur.execute("INSERT INTO order_items (order_id, product_id, quantity) VALUES (%s, %s, %s)", (order_id, product_id, quantity))
            self.conn.commit()
        print("Order added successfully.")

    def list_users(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM users")
            users = cur.fetchall()
            for user in users:
                print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")

    def list_orders(self):
        user_id = input("Enter user ID: ")
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT o.id, o.order_date, p.name, oi.quantity, p.price
                FROM orders o
                JOIN order_items oi ON o.id = oi.order_id
                JOIN products p ON oi.product_id = p.id
                WHERE o.user_id = %s
            """, (user_id,))
            orders = cur.fetchall()
            for order in orders:
                print(f"Order ID: {order[0]}, Date: {order[1]}, Product: {order[2]}, Quantity: {order[3]}, Price: {order[4]}")

    def list_products(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM products")
            products = cur.fetchall()
            for product in products:
                print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}")
