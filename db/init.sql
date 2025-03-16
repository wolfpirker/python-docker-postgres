-- Create users table
CREATE TABLE users (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(100),
    email NVARCHAR(100) UNIQUE NOT NULL
);

-- Create products table
CREATE TABLE products (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

-- Create orders table
CREATE TABLE orders (
    id INT IDENTITY(1,1) PRIMARY KEY,
    user_id INT FOREIGN KEY REFERENCES users(id),
    order_date DATE
);

-- Create order_items table
CREATE TABLE order_items (
    id INT IDENTITY(1,1) PRIMARY KEY,
    order_id INT FOREIGN KEY REFERENCES orders(id),
    product_id INT FOREIGN KEY REFERENCES products(id),
    quantity INT NOT NULL
);

-- Insert sample data
INSERT INTO users (name, email) VALUES
('Alice', 'alice@example.com'),
('Bob', 'bob@example.com');

INSERT INTO products (name, price) VALUES
('Laptop', 1200.00),
('Mouse', 25.00),
('Keyboard', 50.00),
('Monitor', 300.00);

INSERT INTO orders (user_id, order_date) VALUES
(1, '2023-10-01'),
(1, '2023-10-02'),
(2, '2023-10-03');

INSERT INTO order_items (order_id, product_id, quantity) VALUES
(1, 1, 1),  -- Alice's first order: 1 Laptop
(1, 2, 2),  -- Alice's first order: 2 Mice
(2, 3, 1),  -- Alice's second order: 1 Keyboard
(2, 4, 1),  -- Alice's second order: 1 Monitor
(3, 1, 1);  -- Bob's order: 1 Laptop
