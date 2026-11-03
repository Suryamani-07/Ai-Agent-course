from agents import function_tool

@function_tool
def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculate final price after applying discount."""

    discount = price * discount_percent / 100
    final_price = price - discount

    return round(final_price, 2)