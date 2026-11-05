import pandas as pd
n=int(input("Enter number of student:"))

names = []
ages = []
departments = []
dates = []

for i in range(n):
    print("\nEnter details of Student", i+1)

    name = input("Enter Name:")
    age = input("Enter age:")
    department = input ("Enter Department:")
    date = input("Enter Admission Date(DD-MM-YY):")

    names.append(name) 
    ages.append(age)
    departments.append(department)
    dates.append(date)

    Data ={
        'Name': names,
        'Age':ages,
       'Department':departments,
        'Admission_Date': dates
    }

    df = pd.DataFrame(Data)

    print("\nOriginal Data:")
    print(df)
    
    print("\nOriginal Data Types:")
    print(df.dtypes)

    df['Age'] = df['Age'].astype(int)

    df['Name'] = df['Name'].str.strip()

    df['Name'] = df['Name'].str.title()

    df['Department'] = df['Department'].str.title()

    df['Admission_Date'] = pd.to_datetime(
        df['Admission_Date'],
        format = '%d-%m-%Y'
    )

    df['Year'] = df['Admission_Date'].dt.year

    df['Month'] = df['Admission_Date'].dt.month

    df['Day'] = df['Admission_Date'].dt.day

    print("\nTransformed Data:")
    print(df)

    print("\ntransformed Data Types:")
    print(df.dtypes)
