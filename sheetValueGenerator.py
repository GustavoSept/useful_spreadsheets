# Automatically generate mock-values for a budget spreadsheet
def generate_monthly_budget_float(month):
    # Random Monthly transactions 
    num_transactions = np.random.randint(10, 30)
    
    # Date, Spending Category, Value, Obs, Payer ID
    data = []
    for _ in range(num_transactions):
        day = np.random.randint(1, 29)
        expense_type = np.random.choice(expense_types)
        value = np.random.uniform(10, 575)
        observation = f"{expense_type} {month} {day}"
        payer = f"Pessoa {np.random.randint(1, 3)}"
        
        data.append([f"{day}/{month[:3]}/2023", expense_type, value, observation, payer])
    
    # Guaranteeing at least one investment per month
    day = np.random.randint(1, 29)
    value = np.random.uniform(100, 575)
    observation = f"Investimento {month} {day}"
    payer = f"Pessoa {np.random.randint(1, 3)}"
    data.append([f"{day}/{month[:3]}/2023", "Investimento (aporte)", value, observation, payer])
    
    df = pd.DataFrame(data, columns=["Data", "Tipo de Gasto", "Valor", "Observação", "Quem Pagou"])
    return df

# Monthly Generation
monthly_budgets_float = {}
for month in months:
    monthly_budgets_float[month] = generate_monthly_budget_float(month)

# Exporting each month to a CSV
file_paths_float = []

for month, budget in monthly_budgets_float.items():
    file_path = f"/mnt/data/Orçamento_Float_{month}.csv"
    budget.to_csv(file_path, index=False, encoding="utf-8-sig")
    file_paths_float.append(file_path)

file_paths_float
