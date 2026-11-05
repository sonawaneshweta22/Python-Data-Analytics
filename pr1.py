
import pandas as pd


df = pd.DataFrame({
    "Patient":["Aditya","Meera","Rahul","Jiya",],
    "Age":[25,32,45,28],
    "Disease":["Fever","Cold","Diabetes","Fever"],
    "Bill":[1200,800,2500,1500]
})

print("Original Data:\n",df)

print("\nsubset(Age>30):\n",df[df["Age"]>30])

print("\nSorted by Bill(Ascending):\n",
      df.sort_values("Bill"))

print("\nSorted by Bill(Descending):\n",
      df.sort_values("Bill",ascending=False))

print("\nGrouped (Average Bill by Disease):\n",
       df.groupby("Disease")["Bill"].mean())

print("\nMean=",df["Bill"].mean())
print("Median=",df["Bill"].median())
print(df["Bill"].mode())