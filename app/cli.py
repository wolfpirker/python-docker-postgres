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
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
				print ("-> add a user.")
                self.add_user()
            elif choice == '2':
				print ("-> add order for an user.")
                self.add_order()
            elif choice == '3':
				print ("-> list all users.")
                self.list_users()
            elif choice == '4':
				print ("-> list all orders of specific users.")
                self.list_orders()
            elif choice == '5':
				print ("-> exit the app")
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
        amount = input("Enter order amount: ")
        order_date = input("Enter order date (YYYY-MM-DD): ")
        with self.conn.cursor() as cur:
            cur.execute("INSERT INTO orders (user_id, amount, order_date) VALUES (%s, %s, %s)", (user_id, amount, order_date))
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
            cur.execute("SELECT * FROM orders WHERE user_id = %s", (user_id,))
            orders = cur.fetchall()
            for order in orders:
                print(f"ID: {order[0]}, User ID: {order[1]}, Amount: {order[2]}, Order Date: {order[3]}")
