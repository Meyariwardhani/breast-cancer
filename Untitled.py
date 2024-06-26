#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import joblib
import streamlit as st
from sklearn.preprocessing import MinMaxScaler

# Membaca model prediksi breastcancer
breastcancer_model = joblib.load('svm_model.sav')

# Membaca model clustering breastcancer (hasil PCA dengan 1 komponen utama)
clustering_model = joblib.load('kmeans_model.sav')

# Membaca model scaler
scaler = joblib.load('scaler_model2.sav')

# Judul web
st.title('Prediksi Diagnosis Kanker Payudara')

# Input pengguna
diagnosis_input = st.selectbox(
    "Pilih diagnosis:",
    ('Jinak', 'Ganas')
)

# Mapping diagnosis to 0 and 1
diagnosis_mapping = {'Jinak': 0, 'Ganas': 1}
diagnosis_y = diagnosis_mapping[diagnosis_input]

# Menampilkan hasil prediksi
radius_mean_input = st.text_input('Input nilai Radius mean')
texture_mean_input = st.text_input('Input nilai Texture mean')
perimeter_mean_input = st.text_input('Input nilai Perimeter mean')
area_mean_input = st.text_input('Input nilai Area mean')
smoothness_mean_input = st.text_input('Input nilai Smoothness mean')
compactness_mean_input = st.text_input('Input nilai Compactness mean')
concavity_mean_input = st.text_input('Input nilai Concavity mean')
concave_points_mean_input = st.text_input('Input nilai Concave points mean')
symmetry_mean_input = st.text_input('Input nilai Symmetry mean')
fractal_dimension_mean_input = st.text_input('Input nilai Fractal dimension mean')


# Validasi input
if diagnosis_input.strip() and radius_mean_input.strip() and texture_mean_input.strip() and perimeter_mean_input.strip() and area_mean_input.strip() and smoothness_mean.strip() and compactness_mean.strip() and concavity_mean.strip() and concave_points_mean_input.strip() and symmetry_mean_input:
    diagnosis = float(diagnosis)
    radius_mean = float(radius_mean)
    texture_mean = float(texture_mean_input)
    perimeter_mean = float(perimeter_mean_input)
    area_mean = float(area_mean_input)
    smoothness_mean = float(smoothness_mean_input)
    compactness_mean = float(compactness_mean_input)
    concavity_mean = float(concavity_mean_input)
    concave_points_mean = float(concave points_mean_input)
    symmetry_mean_mean = float(symmetry_mean_input)

    # Code untuk prediksi
    # Membuat tombol untuk prediksi
    if st.button('Test Prediksi Diagnosis Kanker Payudara'):
        input_data = np.array([diagnosis, radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean,
        concavity_mean, concave_points_mean, symmetry_mean]).reshape(1, -1)
        breastcancer_prediction = breastcancer_model.predict(input_data)

        # Menampilkan hasil prediksi
        if breastcancer_prediction[0] == 1:
            breastcancer_diagnosis = 'Pasien terdiagnosis kanker ganas'
            st.success(breastcancer_diagnosis)
        else:
            breastcancer_diagnosis = 'Pasien terdiagnosis kanker jinak'
            st.error(breastcancer_diagnosis)

            # Melakukan clustering untuk penderita anemia
            # Scaling hanya pada variabel yang digunakan untuk pengklasteran
            clustering_data = np.array([radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean,
            concavity_mean, concave_points_mean, symmetry_mean]).reshape(1, -1)
            clustering_data_scaled = scaler.transform(clustering_data)

            # Terapkan PCA pada data yang di-scaling
            clustering_data_pca = pca_model.transform(clustering_data_scaled)

            breastcancer_severity = clustering_model.predict(clustering_data_pca)
            if breastcancer_severity[0] == 0:
                severity = 'Rendah'
            else:
                severity = 'Tinggi'
            
            st.write(f'Tingkat keparahan Kanker payudara: {severity}')
else:
    st.warning('Mohon lengkapi semua kolom input.')


# In[ ]:




