from crewai_tools import tool

@tool("Travel Cost Calculator")
def calculate_travel_cost(flight_cost: float, hotel_cost: float, daily_budget: float, days: int) -> str:
    """
    Calculates the estimated total cost of a trip based on flight, hotel, and daily expenses.

    Args:
        flight_cost (float): The cost of the flight.
        hotel_cost (float): The nightly hotel cost.
        daily_budget (float): The daily spending budget.
        days (int): Number of days for the trip.

    Returns:
        str: A formatted string showing the total trip cost.
    """
    if days <= 0 or flight_cost < 0 or hotel_cost < 0 or daily_budget < 0:
        return "Error: Invalid input values. Costs must be non-negative, and days must be at least 1."

    total_cost = flight_cost + (hotel_cost * days) + (daily_budget * days)
    return f"Total estimated trip cost: ${total_cost:.2f}"
