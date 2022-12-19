class Calculator:

    def calculate_income(self):
        print("\nFirst, let's talk about your monthly income.")
        rental_income = int(input("\nWhat's the monthly rental income of your property? \n\n"))
        laundry = int(input("\nHow much do you expect to make monthly from laundry appliances? \n\n"))
        storage = int(input("\nHow much do you expect to make monthly from storage facilities? \n\n"))
        misc = int(input("\nHow much do you expect to make monthly from other miscellaneous things? \n\n"))
        total_monthly_income = rental_income + laundry + storage + misc
        print(f"\nOkay, great! So your total monthly income is ${total_monthly_income} altogether.\n")
        self.total_monthly_income = total_monthly_income

    def calculate_expenses(self):
        print("\nNow let's talk about your expenses.\n")
        tax = int(input("\nHow much do you pay in taxes each month? \n\n"))
        insurance = int(input("\nHow much do you pay in insurance each month? \n\n"))
        utilities = int(input("\nHow much do you pay in utility bills each month? \n\n"))
        homeowners = int(input("\nHow much do you pay in homeowners association fees each month? \n\n"))
        lawn_snow = int(input("\nHow much do you pay in lawn and snow maintenance each month? \n\n"))
        vacancy = int(input("\nHow much money will you have to set aside for periodic rental vacancy? \n\n"))
        repairs = int(input("\nHow much money will you be paying per month in repairs? \n\n"))
        cap_ex = int(input("\nHow much will you be setting aside monthly for potential capital expenditures? \n\n"))
        property_management = int(input("\nHow much money will you be paying monthly for property management? \n\n"))
        mortgage = int(input("\nHow much is your monthly mortgage payment? \n\n"))
        total_monthly_expenses = tax + insurance + utilities + homeowners + lawn_snow + vacancy + repairs + cap_ex + property_management + mortgage
        print(f"\nYour total monthly expenses are ${total_monthly_expenses}.\n")
        self.total_monthly_expenses = total_monthly_expenses

    def calculate_cashflow(self):
        self.total_monthly_cashflow = self.total_monthly_income - self.total_monthly_expenses
        self.annual_cashflow = self.total_monthly_cashflow * 12
        print(f"\nYour total monthly cashflow is ${self.total_monthly_cashflow}, making your annual cashflow ${self.annual_cashflow}.\n")

    def calculate_ROI(self):
        print("\nWe only have a few more questions to ask.\n")
        downpayment = int(input("\nHow much is the downpayment on the property? \n\n"))
        closing_costs = int(input("\nWhat are the closing costs for the property? \n\n"))
        rehab_budget = int(input("\nWhat is your rehab budget for this property? \n\n"))
        self.total_investment = downpayment + closing_costs + rehab_budget
        ROI = self.annual_cashflow / self.total_investment
        self.ROI_percentage = ROI * 100
        print(f"\nYour cash on cash return on investment is {self.ROI_percentage}%.\n")

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

def run_calculator():
    print("\nWelcome to your own virtual real estate consultant!")
    print("\nWe're going to help you decide if the property you want to buy will give you a good return on investment.")
    username = input("\nPlease enter your name: ")
    email = input("Please enter your email: ")
    new_user = User(username, email)
    print(f"\nNice to meet you, {new_user.username.title()}. We're going to ask you a handful of questions to help determine if your investment is fiscally wise.")
    my_calculator = Calculator()
    my_calculator.calculate_income()
    my_calculator.calculate_expenses()
    my_calculator.calculate_cashflow()
    my_calculator.calculate_ROI()

run_calculator()