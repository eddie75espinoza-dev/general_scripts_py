from datetime import datetime, timedelta

def date_range_category(dates_list):
    current_date = datetime.now().date()
    one_month_ago = current_date - timedelta(days=30)
    
    result_list = []
    for date_str in dates_list:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        
        if date_obj == one_month_ago:
            category = 'day'
        elif date_obj >= one_month_ago and date_obj <= current_date:
            category = 'next_day'
        
        result_list.append({'date': date_str, 'category': category})
    
    return result_list

# Ejemplo de lista de fechas
dates_list = ['2023-08-01', '2023-07-03', '2023-07-25', '2023-07-31', '2023-06-30', '2023-08-02', '2023-07-03', '2023-07-04', '2023-07-02', '2023-07-04', '2023-07-20']

# Llamada a la función
results = date_range_category(dates_list)

# Imprimir el resultado
for result in results:
    print(result)
