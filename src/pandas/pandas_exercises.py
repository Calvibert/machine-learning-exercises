import pandas as pd

data = pd.read_csv('Salaries.csv')

#average
print(data['BasePay'].sum() / data['BasePay'].count())

#max
print(data['OvertimePay'].max())

# What is the job title of JOSEPH DRISCOLL
print(data[data['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'])

#How much does JOSEPH DRISCOLL make (including benefits)?
print(data[data['EmployeeName'] == 'JOSEPH DRISCOLL'])
print(data[data['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'])

#What is the name of highest paid person (including benefits)?
max = data['TotalPayBenefits'].max()
print(data[data['TotalPayBenefits']==max]['EmployeeName'])

#What is the name of lowest paid person (including benefits)?
min = data['TotalPayBenefits'].min()
print(data[data['TotalPayBenefits']==min]['EmployeeName'])

# What was the average (mean) BasePay of all employees per year? (2011-2014) ?
avgBasePay = data['BasePay'].mean()
print(avgBasePay)
