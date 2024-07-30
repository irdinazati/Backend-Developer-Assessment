# Task 1: Data Model Design Create a Python class for representing an investment fund.

class InvestmentFund:
    """
    A class to represent an investment fund.

    Attributes:
    fund_id (str): Unique identifier for the fund.
    fund_name (str): Name of the fund.
    fund_manager_name (str): Name of the fund manager.
    fund_description (str): Description of the fund.
    fund_nav (float): Net Asset Value (NAV) of the fund.
    fund_date_of_creation (str): Date when the fund was created.
    fund_performance (float): Performance of the fund as a percentage.
    """

    def __init__(self, fund_id, fund_name, fund_manager_name, fund_description, fund_nav, fund_date_of_creation, fund_performance):
        
        # Initializes the InvestmentFund with the provided attributes.

        self.fund_id = fund_id
        self.fund_name = fund_name
        self.fund_manager_name = fund_manager_name
        self.fund_description = fund_description
        self.fund_nav = fund_nav
        self.fund_date_of_creation = fund_date_of_creation
        self.fund_performance = fund_performance
    
    def __str__(self):
        
        # Returns a string representation of the InvestmentFund object.

        return f"Fund ID: {self.fund_id}\n" \
               f"Fund Name: {self.fund_name}\n" \
               f"Fund Manager: {self.fund_manager_name}\n" \
               f"Description: {self.fund_description}\n" \
               f"Net Asset Value (NAV): {self.fund_nav}\n" \
               f"Date of Creation: {self.fund_date_of_creation}\n" \
               f"Performance: {self.fund_performance}%"

# Example usage:
if __name__ == "__main__":
    # Creating an instance of InvestmentFund
    fund = InvestmentFund(
        fund_id="F01",
        fund_name="Global Growth Fund",
        fund_manager_name="Irdina Izzati",
        fund_description="A diversified fund focusing on global equities.",
        fund_nav=1000000,
        fund_date_of_creation="2024-07-26",
        fund_performance=10.5
    )

    # Printing the fund details
    print(fund)

