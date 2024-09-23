import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

dataset = pd.read_csv(r'D:\coding\PYTHON\TIK KELAS 12\Web_Scraping\Data-Rak.csv')
print(dataset)

NanData = pd.isnull(dataset["Nama"])
dataset[NanData]

NanData = pd.isnull(dataset["Harga"])
dataset[NanData]

NanData = pd.isnull(dataset["Rating"])
dataset[NanData]

duplicate = dataset[dataset.duplicated(["Nama"],keep=False)]

dropData = dataset.dropna()

print("Jumlah data Rak sebelum membuang data kosong : ",len(dataset))
print("Jumlah data Rak sesudah membuang data kosong : ",len(dropData))
print("Jumlah data kosong : ",len(dataset)-len(dropData))

#mencari rata-rata harga
dataset['Harga'] = dataset['Harga'].str.replace('Rp', '').str.replace('.', '')
dataset['Harga'] = dataset['Harga'].astype(float)
dataMean = dataset["Harga"].mean()
print("Rata-rata Harga barang : ", "Rp ", dataMean)

#mencari rata-rata rating
dataset['Rating'] = dataset['Rating'].astype(float)
RatingMean = dataset["Rating"].mean()
print("Rata-rata Rating barang : ", RatingMean)

#mencari rating tertinggi 
maxRating = dataset["Rating"].max()
print("Rating tertinggi: ", maxRating)

#mencari rating terendah
minRating = dataset["Rating"].min()
print("Rating terendah: ", minRating)

# Mencari korelasi pearson antara harga dan rating
corr_coef = dataset['Harga'].corr(dataset['Rating'])
print("Koefisien korelasi antara Harga dan Rating: ", corr_coef)
if corr_coef <= 0:
    print("""harga dan Rating tidak ada hubungan.
          Naiknya harga tidak memengaruhi Rating.""")
elif 0.01 <= corr_coef <= 0.09 :
    print("Harga dan Rating memiliki hubungan namun sangat lemah")
elif 0.1 <= corr_coef <= 0.29 :
    print("Harga dan Rating memiliki hubungan lemah")
elif 0.3 <= corr_coef <= 0.49:
    print("Harga dan Rating memiliki hubungan sedang")
elif 0.5 <= corr_coef <= 0.69:
    print("Harga dan Rating memiliki hubungan kuat")
elif 0.7 <= corr_coef <= 0.89:
    print("Harga dan Rating memiliki hubungan yang sangat kuat")
elif corr_coef >= 0.9:
    print("""Harga dan Rating memiliki hubungan yang sangat kuat.""")
else:
    print("No numbers")
    
# visualisasi distribusi harga
plt.figure(figsize=(16, 6))
plt.hist(dataset['Harga'], bins=50, alpha=0.7, color='skyblue')
plt.title("Distribusi Harga")
plt.xlabel("Harga (Rp)")
plt.ylabel("Frequency")
plt.xticks(dataset['Harga'].unique(), rotation=90, fontsize=6)
plt.show()

# visualisasi hubungan 'Harga' dan 'Rating'
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Harga', y='Rating', data=dataset)
plt.title("Hubungan antara Harga dan Rating")
plt.xlabel("Harga (Rp)")
plt.ylabel("Rating")
plt.xticks(dataset['Harga'].unique(), rotation=90, fontsize=6)
plt.show()

#visualisasi data dengan diagram lingkaran
rating_counts = dataset['Rating'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(rating_counts, labels=rating_counts.index, autopct=lambda p : '{:.1f}% ({:.0f})'.format(p,p * sum(rating_counts)/100), textprops={'size': '11'})
plt.title("Distribusi Rating")
plt.show()
