#CUSTOM EXCEPTION FRAMEWORK — INVENTORY SYSTEM

class InventoryError(Exception):
    """Base exception for the Inventory Management System."""
    def __init__(self, message, error_code=None):
        super().__init__(message)
        self.error_code = error_code

    def __str__(self):
        base = super().__str__()
        return f"[{self.error_code}] {base}" if self.error_code else base


class OutOfStockError(InventoryError):
    def __init__(self, product_id, requested, available):
        super().__init__(
            f"Product '{product_id}' has only {available} units "
            f"but {requested} were requested.",
            error_code="INV-001"
        )
        self.product_id = product_id
        self.requested  = requested
        self.available  = available


class InvalidProductIDError(InventoryError):
    def __init__(self, product_id):
        super().__init__(
            f"Product ID '{product_id}' does not exist in inventory.",
            error_code="INV-002"
        )
        self.product_id = product_id


class DuplicateProductError(InventoryError):
    def __init__(self, product_id):
        super().__init__(
            f"Product ID '{product_id}' already exists.",
            error_code="INV-003"
        )


class InvalidQuantityError(InventoryError):
    def __init__(self, quantity):
        super().__init__(
            f"Quantity must be a positive integer, got: {quantity}.",
            error_code="INV-004"
        )


class PriceError(InventoryError):
    def __init__(self, price):
        super().__init__(
            f"Price must be a positive number, got: {price}.",
            error_code="INV-005"
        )


class SupplierNotFoundError(InventoryError):
    def __init__(self, supplier_id):
        super().__init__(
            f"Supplier '{supplier_id}' not registered.",
            error_code="INV-006"
        )


class CategoryError(InventoryError):
    def __init__(self, category):
        super().__init__(
            f"Category '{category}' is not recognised.",
            error_code="INV-007"
        )


# ── Inventory System ──────────────────────────────────────────

VALID_CATEGORIES = {"Electronics", "Clothing", "Food", "Furniture", "Toys"}

class InventorySystem:
    def __init__(self):
        self._products  = {}   # id -> {name, price, stock, category}
        self._suppliers = {}   # id -> name

    # Suppliers
    def register_supplier(self, sid: str, name: str) -> None:
        self._suppliers[sid] = name
        print(f"  ✅ Supplier registered : {name} ({sid})")

    # Products
    def add_product(self, pid: str, name: str, price: float,
                    stock: int, category: str, supplier_id: str) -> None:
        if pid in self._products:
            raise DuplicateProductError(pid)
        if price <= 0:
            raise PriceError(price)
        if stock < 0:
            raise InvalidQuantityError(stock)
        if category not in VALID_CATEGORIES:
            raise CategoryError(category)
        if supplier_id not in self._suppliers:
            raise SupplierNotFoundError(supplier_id)

        self._products[pid] = {
            "name": name, "price": price,
            "stock": stock, "category": category,
            "supplier": supplier_id,
        }
        print(f"  ✅ Product added  : [{pid}] {name}  "
              f"₹{price}  Stock={stock}  Cat={category}")

    def restock(self, pid: str, qty: int) -> None:
        self._validate_pid(pid)
        if qty <= 0:
            raise InvalidQuantityError(qty)
        self._products[pid]["stock"] += qty
        print(f"  🔄 Restocked {pid}: +{qty}  "
              f"(total={self._products[pid]['stock']})")

    def sell(self, pid: str, qty: int) -> float:
        self._validate_pid(pid)
        if qty <= 0:
            raise InvalidQuantityError(qty)
        available = self._products[pid]["stock"]
        if available < qty:
            raise OutOfStockError(pid, qty, available)
        self._products[pid]["stock"] -= qty
        total = self._products[pid]["price"] * qty
        print(f"  💰 Sold {qty}x {self._products[pid]['name']}  "
              f"→ ₹{total:.2f}  (remaining={self._products[pid]['stock']})")
        return total

    def _validate_pid(self, pid: str) -> None:
        if pid not in self._products:
            raise InvalidProductIDError(pid)

    def list_inventory(self) -> None:
        print(f"\n  {'ID':<8} {'Name':<15} {'Price':>8} {'Stock':>6} {'Category'}")
        print(f"  {'─'*55}")
        for pid, p in self._products.items():
            print(f"  {pid:<8} {p['name']:<15} ₹{p['price']:>7.2f} "
                  f"{p['stock']:>6}  {p['category']}")


# ── Demo ──────────────────────────────────────────────────────

def demo_inventory():
    print("=" * 55)
    print("    CUSTOM EXCEPTION FRAMEWORK — INVENTORY DEMO")
    print("=" * 55)

    inv = InventorySystem()

    # Register suppliers
    print("\n--- Registering Suppliers ---")
    inv.register_supplier("S01", "TechWorld")
    inv.register_supplier("S02", "FashionHub")

    # Add products
    print("\n--- Adding Products ---")
    scenarios = [
        ("PR01", "Laptop",   55000, 10, "Electronics", "S01", "Valid product"),
        ("PR02", "T-Shirt",  499,   25, "Clothing",    "S02", "Valid product"),
        ("PR01", "Mouse",    799,    5, "Electronics", "S01", "Duplicate ID"),
        ("PR03", "Keyboard", -100,  10, "Electronics", "S01", "Negative price"),
        ("PR04", "Chips",    20,    50, "Snacks",      "S01", "Bad category"),
        ("PR05", "Chair",    3500,  8,  "Furniture",   "S99", "Unknown supplier"),
    ]

    for pid, name, price, stock, cat, sup, label in scenarios:
        print(f"\n  Scenario : {label}")
        try:
            inv.add_product(pid, name, price, stock, cat, sup)
        except InventoryError as e:
            print(f"  ❌ {e}")

    # Operations
    print("\n--- Selling & Restocking ---")
    ops = [
        ("sell",     "PR01", 3,   "Normal sale"),
        ("sell",     "PR02", 30,  "Oversell"),
        ("sell",     "PXXX", 1,   "Invalid product"),
        ("restock",  "PR02", -5,  "Bad quantity"),
        ("restock",  "PR02", 10,  "Valid restock"),
        ("sell",     "PR01", 0,   "Zero quantity"),
    ]

    for op, pid, qty, label in ops:
        print(f"\n  Scenario : {label}")
        try:
            if op == "sell":
                inv.sell(pid, qty)
            else:
                inv.restock(pid, qty)
        except InventoryError as e:
            print(f"  ❌ {e}")

    print("\n--- Final Inventory ---")
    inv.list_inventory()
    print(f"\n{'='*55}\n")


demo_inventory()