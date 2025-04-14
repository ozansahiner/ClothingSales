import pandas as pd
import matplotlib.pyplot as plt

# CSV dosyasını oku
data = pd.read_csv('data.csv')

# Sütun adlarındaki boşlukları temizle
data.columns = data.columns.str.strip()

# Kontrol amaçlı yazdır (isteğe bağlı)
print(data.columns)

# Beden bazında satışları grupla
size_sales = data.groupby('Size')['QuantitySold'].sum().sort_values(ascending=False)

# En çok satılan bedeni yazdır
most_sold_size = size_sales.idxmax()
most_sold_quantity = size_sales.max()
print(f"En çok satılan beden: {most_sold_size} ({most_sold_quantity} adet)")

# Görselleştir
plt.figure(figsize=(8,5))
size_sales.plot(kind='bar', color='skyblue')
plt.title('Toplam Satışa Göre Beden Dağılımı')
plt.xlabel('Beden')
plt.ylabel('Satılan Miktar')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("sales_by_size.png")
plt.show()
