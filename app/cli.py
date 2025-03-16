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
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        self.conn.commit()
        print("User added successfully.")

    def add_order(self):
        user_id = input("Enter user ID: ")
        order_date = input("Enter order date (YYYY-MM-DD): ")
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO orders (user_id, order_date) VALUES (?, ?)", (user_id, order_date))
        order_id = cursor.execute("SELECT SCOPE_IDENTITY()").fetchval()
        while True:
            product_id = input("Enter product ID (or 'done' to finish): ")
            if product_id == 'done':
                break
            quantity = input("Enter quantity: ")
            cursor.execute("INSERT INTO order_items (order_id, product_id, quantity) VALUES (?, ?, ?)", (order_id, product_id, quantity))
        self.conn.commit()
        print("Order added successfully.")

    def list_users(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        for user in users:
            print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")

    def list_orders(self):
        user_id = input("Enter user ID: ")
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT o.id, o.order_date, p.name, oi.quantity, p.price
            FROM orders o
            JOIN order_items oi ON o.id = oi.order_id
            JOIN products p ON oi.product_id = p.id
            WHERE o.user_id = ?
        """, (user_id,))
        orders = cursor.fetchall()
        for order in orders:
            print(f"Order ID: {order.id}, Date: {order.order_date}, Product: {order.name}, Quantity: {order.quantity}, Price: {order.price}")

    def list_products(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        for product in products:
            print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}")
