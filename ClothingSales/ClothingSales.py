import pandas as pd
import matplotlib.pyplot as plt

# CSV dosyasını oku
data = pd.read_csv('data.csv')

# Sütun adlarındaki boşlukları temizle
data.columns = data.columns.str.strip()

# Cinsiyet ve beden bazında satış miktarını grupla
grouped = data.groupby(['Gender', 'Size'])['QuantitySold'].sum().unstack()

# Eksik değerleri 0 ile doldur
grouped = grouped.fillna(0)

# Grupları görselleştir (bar chart)
grouped.T.plot(kind='bar', figsize=(10,6))

plt.title('Cinsiyete ve Bedene Göre Satış Dağılımı')
plt.xlabel('Beden')
plt.ylabel('Satılan Miktar')
plt.xticks(rotation=0)
plt.legend(title='Cinsiyet')
plt.tight_layout()
plt.savefig("sales_by_gender_and_size.png")
plt.show()
