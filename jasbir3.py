import argparse

def convertSalary(salary, country):
    conversion_rates = {
        "Canada": 1,
        "USA": 1 / 1.18,
        "Cambodia": 4847.38,
        "United Kingdom": 1 / 0.91
    }
    average_salaries = {
        "Canada": 64000,
        "USA": 56516,
        "Cambodia": 5649856,
        "United Kingdom": 35423
    }

    if country not in conversion_rates:
        return "Invalid country input. Please enter Canada, USA, Cambodia, or United Kingdom."

    converted_salary = salary * conversion_rates[country]
    currency_name = "CAD" if country == "Canada" else "USD" if country == "USA" else "Cambodian riel" if country == "Cambodia" else "Pound Sterling"
    average_salary = average_salaries[country]

    if converted_salary > average_salary:
        return f"You will be rich in {country} with a salary of {converted_salary:.2f} {currency_name}"
    else:
        return f"You will be poor in {country} with a salary of {converted_salary:.2f} {currency_name}"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert salary based on country')
    parser.add_argument('salary', type=float, help='Salary in Euros')
    parser.add_argument('country', type=str, choices=['Canada', 'USA', 'Cambodia', 'United Kingdom'], help='Country to migrate to')
    args = parser.parse_args()

    result = convertSalary(args.salary, args.country)
    print(result)
