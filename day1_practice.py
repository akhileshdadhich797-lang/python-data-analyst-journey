name='Akhilesh'
age=38
height=1.73
currently_working_fintech=True
print(f'Name: {name}, Type: {type(name)}')
print(f'Age: {age}, Type: {type(age)}')
print(f'Height: {height}, Type: {type(height)}')
print(f'Current working in fintech: {currently_working_fintech}, Type: {type(currently_working_fintech)}')
expenses=[45000, 52000, 48000, 61000, 55000, 49000]
print(max(expenses))
print(min(expenses))
print(sum(expenses))
print(sum(expenses)/len(expenses))
print(sorted(expenses,reverse=True))
for expense in expenses:
    if expense > 50000:
        print(expense)

full_name='akhilesh dadhich'
print(full_name.title())
print(full_name.upper())
print(full_name[0:8])
print(len(full_name.replace(" ","")))
num = 17
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

if num % 3 == 0 and num % 5 ==0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and 5")

a = [1, 2, 3]
b = a
b.append(4)
print(a)
print(b)
#I understand that assignment operator assigns the contents of list b to a and hence append modifies the orginal list a as well but I am not sure this is complete explaination

expenses = [45000, 52000, 48000, 61000, 55000, 49000]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
highest_expense=max(expenses)
minimum_expense=min(expenses)
total_expense=sum(expenses)
print(f'Highest: {highest_expense} in {months[expenses.index(highest_expense)]}')
print(f'Lowest: {minimum_expense} in {months[expenses.index(minimum_expense)]}')
print(f'Total: {total_expense}')
print(f'Average: {total_expense/len(expenses):.2f}')
budget=50000
over_budget=[]
for month, expense in zip(months,expenses):
    if expense > budget:
        over_budget.append(f'{month} ({expense})')
print(f'Month over the budget {budget}: {', '.join(over_budget)}')