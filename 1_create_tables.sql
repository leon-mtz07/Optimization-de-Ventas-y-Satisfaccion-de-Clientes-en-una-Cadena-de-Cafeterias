-- Creando las tablas

-- Tabla de productos
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(50),
    category VARCHAR(30),
    price DECIMAL(5,2),
    cost DECIMAL(5,2)
);
x   x
-- Tabla de tiendas
CREATE TABLE stores (
    store_id INT PRIMARY KEY,
    location VARCHAR(100)
);

-- Tabla de ventas
CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    product_id INT,
    store_id INT,
    sale_timestamp TIMESTAMP,
    quantity INT,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (store_id) REFERENCES stores(store_id)
);

-- Tabla de feedback
CREATE TABLE customer_feedback (
    feedback_id INT PRIMARY KEY,
    store_id INT,
    comment TEXT,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    feedback_date DATE
);