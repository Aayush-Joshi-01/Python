def get_investment_overview(investments):
    total_value = sum(investment['value'] for investment in investments)
    total_return = sum(investment['value'] * investment['return'] for investment in investments)
    average_return = total_return / sum(investment['value'] for investment in investments)
    highest_return_investment = max(investments, key=lambda x: x['return'])
    return {
        'total_value': total_value,
        'average_return': average_return,
        'highest_return_investment': highest_return_investment,
    }


def search_investments_by_type(investments, investment_type):
    return [investment for investment in investments if investment['type'] == investment_type]


if __name__ == '__main__':
    investments = [
        {'type': 'Stock', 'name': 'Apple Inc.', 'value': 10000, 'return': 0.05},
        {'type': 'Bond', 'name': 'US Treasury Bond', 'value': 5000, 'return': 0.02},
        {'type': 'Mutual Fund', 'name': 'Vanguard 500 Index Fund', 'value': 20000, 'return': 0.07},
        {'type': 'Real Estate', 'name': 'Apartment Building', 'value': 150000, 'return': 0.03},
    ]
    investment_overview = get_investment_overview(investments)
    print(f"Total value of investments: {investment_overview['total_value']:,.2f}")
    print(f"Average return per investment: {investment_overview['average_return']:.2%}")
    print(
        f"Investment with the highest return: {investment_overview['highest_return_investment']['name']} ({investment_overview['highest_return_investment']['type']}) with return {investment_overview['highest_return_investment']['return']:.2%}")
    stock_investments = search_investments_by_type(investments, 'Stock')
    print(f"Stock investments: {[investment['name'] for investment in stock_investments]}")
