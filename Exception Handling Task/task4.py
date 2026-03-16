#E-COMMERCE ORDER MANAGEMENT SYSTEM

# ============================================================
#           E-COMMERCE ORDER MANAGEMENT SYSTEM
# ============================================================

# Custom Exceptions
class InvalidCouponError(Exception):
    def __init__(self, code):
        super().__init__(f"Invalid or expired coupon code: '{code}'")

class OutOfStockError(Exception):
    def __init__(self, product):
        super().__init__(f"Product '{product}' is out of stock.")

class InvalidPaymentMethodError(Exception):
    def __init__(self, method):
        super().__init__(f"Payment method '{method}' is not supported.")

class OrderNotFoundError(Exception):
    def __init__(self, order_id):
        super().__init__(f"Order ID '{order_id}' not found.")

class RefundFailedError(Exception):
    def __init__(self, reason):
        super().__init__(f"Refund failed: {reason}")


# Sample Data
PRODUCTS = {
    "P001": {"name": "Laptop",     "price": 75000, "stock": 5},
    "P002": {"name": "Headphones", "price": 2500,  "stock": 0},
    "P003": {"name": "Mouse",      "price": 800,   "stock": 10},
}

VALID_COUPONS   = {"SAVE10": 10, "FLAT500": 500}   # code -> discount
PAYMENT_METHODS = ["credit_card", "debit_card", "upi", "net_banking"]
ORDERS          = {}                                # order_id -> order dict
order_counter   = 1


# ── Helper Functions ──────────────────────────────────────────

def validate_coupon(code: str) -> float:
    """Returns discount amount/percentage or raises InvalidCouponError."""
    if code not in VALID_COUPONS:
        raise InvalidCouponError(code)
    return VALID_COUPONS[code]


def validate_payment(method: str) -> None:
    if method not in PAYMENT_METHODS:
        raise InvalidPaymentMethodError(method)


def place_order(product_id: str, quantity: int,
                payment_method: str, coupon_code: str = "") -> dict:
    global order_counter

    # 1. Check product existence
    if product_id not in PRODUCTS:
        raise KeyError(f"Product ID '{product_id}' does not exist.")

    product = PRODUCTS[product_id]

    # 2. Stock check
    if product["stock"] < quantity:
        raise OutOfStockError(product["name"])

    # 3. Payment validation
    validate_payment(payment_method)

    # 4. Coupon (optional)
    discount = 0
    if coupon_code:
        discount = validate_coupon(coupon_code)

    # 5. Calculate total
    total = product["price"] * quantity
    total -= discount if discount > 100 else (total * discount / 100)
    total = max(total, 0)

    # 6. Deduct stock & save order
    product["stock"] -= quantity
    order_id = f"ORD{order_counter:04d}"
    order_counter += 1

    ORDERS[order_id] = {
        "order_id":      order_id,
        "product":       product["name"],
        "quantity":      quantity,
        "total":         total,
        "payment":       payment_method,
        "status":        "Confirmed",
    }

    return ORDERS[order_id]


def return_order(order_id: str) -> str:
    if order_id not in ORDERS:
        raise OrderNotFoundError(order_id)
    order = ORDERS[order_id]
    if order["status"] in ("Returned", "Refunded"):
        raise RefundFailedError("Order already returned/refunded.")
    order["status"] = "Returned"
    return f"Order {order_id} marked as returned."


def process_refund(order_id: str) -> str:
    if order_id not in ORDERS:
        raise OrderNotFoundError(order_id)
    order = ORDERS[order_id]
    if order["status"] != "Returned":
        raise RefundFailedError("Order must be in 'Returned' state before refund.")
    order["status"] = "Refunded"
    return f"Refund of ₹{order['total']:.2f} processed for Order {order_id}."


# ── Demo ──────────────────────────────────────────────────────

def demo_ecommerce():
    print("=" * 55)
    print("       E-COMMERCE ORDER MANAGEMENT DEMO")
    print("=" * 55)

    test_cases = [
        # (product_id, qty, payment, coupon,  label)
        ("P001", 1, "credit_card", "SAVE10",  "Valid order with coupon"),
        ("P002", 1, "upi",         "",        "Out-of-stock product"),
        ("P001", 1, "bitcoin",     "",        "Invalid payment method"),
        ("P001", 1, "debit_card",  "FAKE50",  "Invalid coupon code"),
        ("P003", 2, "net_banking", "",        "Valid order, no coupon"),
    ]

    placed_orders = []

    for pid, qty, pay, coupon, label in test_cases:
        print(f"\n{'─'*50}")
        print(f"  Scenario : {label}")
        try:
            order = place_order(pid, qty, pay, coupon)
            print(f"  ✅ Order Placed  : {order['order_id']}")
            print(f"     Product       : {order['product']}")
            print(f"     Total         : ₹{order['total']:.2f}")
            print(f"     Payment       : {order['payment']}")
            placed_orders.append(order["order_id"])
        except (OutOfStockError, InvalidPaymentMethodError,
                InvalidCouponError, KeyError) as e:
            print(f"  ❌ Error          : {e}")

    # Return & Refund demo
    if placed_orders:
        oid = placed_orders[0]
        print(f"\n{'─'*50}")
        print(f"  Processing Return & Refund for {oid}")
        try:
            print(f"  🔄 {return_order(oid)}")
            print(f"  💰 {process_refund(oid)}")
            # Try double-refund
            print(f"  🔄 {process_refund(oid)}")
        except (OrderNotFoundError, RefundFailedError) as e:
            print(f"  ❌ {e}")

    print(f"\n{'='*55}\n")


demo_ecommerce()