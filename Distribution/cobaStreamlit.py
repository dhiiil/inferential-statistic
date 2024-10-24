import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import streamlit as st
import pandas as pd

data = []
samples = 500
st.title('Tugas 2 - Statistika Inferensial : Distribusi Data')
option = st.selectbox(
    'Pilih Distribusi yang Diinginkan:',
    ('Uniform', 'Normal', 'Poisson', 'Exponential', 'Binomial'))

if option == 'Uniform':
    data = np.random.rand(samples)
elif option == 'Poisson':
    data = np.random.poisson(2, samples)
elif option == 'Normal':
    data = np.random.randn(samples)
elif option == 'Exponential':
    data = np.random.exponential(5, samples)
elif option == 'Binomial':
    data = np.random.binomial(10, .5, samples)

df = pd.DataFrame(data, columns=['values'])
df['Binned'] = pd.cut(df['values'], bins=10)
frequency_table = df['Binned'].value_counts().sort_index()
frequency_df = frequency_table.reset_index()
frequency_df.columns = ['Interval', 'Frequency']

st.write("### Sampel Data")
st.text( ", ".join(map(str, data)))

st.write("### Tabel Distribusi Frekuensi")
st.dataframe(frequency_df)

st.write("### Visualisasi Histogram")
plt.figure(figsize=(12,4))
sns.histplot(data, kde=True)
plt.grid(True)
plt.title("Visualisasi Distribusi "+ option + " dari 500 Sampel Acak", fontsize=18)

st.pyplot(plt)

