# Udemy Course - Success Percentage Prediction of course release 
http://udemy.com/

![](https://i.ibb.co/vHJvqDc/u.png)

Udemy, Inc. adalah platform pembelajaran online Amerika yang ditujukan untuk orang dewasa dan pelajar profesional. Didirikan pada Mei 2010 oleh Eren Bali, Gagan Biyani , dan Oktay Caglar. Pada Jan 2020, platform ini memiliki lebih dari 35 juta siswa dan 57.000 instruktur yang mengajar kursus lebih dari 65 bahasa.

Pandemi covid-19 yang terjadi di Indonesia telah memberikan pengaruh baik dan buruk diberbagai sektor kehidupan. Salah satu pengaruh buruk yang terjadi ialah pada sektor pendidikan dan sektor ketenagakerjaan. Menurut situs mediaindonesia.com, kualitas pendidikan di Indonesia menurun saat diterapkannya sistem pendidikan jarak jauh berbasis teknologi (Online). Tentunya karena adanya aturan Pembatasan Sosial Berskala Besar sebagai salah satu cara menghentikan rantai penyebaran covid, sistem pendidikan di Indonesia harus diubah menjadi sistem daring. Akan tetapi ternyata hal ini memberikan dampak penurunan kualitas pendidikan karena komunikasi antara pendidik dan pelajar terhambat. Selain itu pandemi covid-19 ini juga berdampak terhadap lembaga-lembaga bimbingan belajar, dimana telah terjadi penurunan partisipan (sonora.id). 

Sedangkan pada sektor ketenagakerjaan, menurut kompas.com, berdasarkan data kemnaker per 7 April 2020 sebanyak 39.977 perusahaan memberhentikan karyawannya. Hal ini dilakukan dengan tujuan untuk menstabilkan keuangan perusahaan. Tentunya aspek skill dan kemampuan yang dimiliki karyawan dan yang dibutuhkan perusahaan menjadi aspek penting dalam memilah karyawan yang akan diberhentikan. Kondisi seperti ini menjadi peluang bagi lembaga-lembaga pembelajaran online seperti udemy untuk memasarkan courses nya kepada mereka (target) yang membutuhkan pelatihan untuk dapat mengupgrade skill atau kemampuan. Akan tetapi, menjadi tantangan tersendiri bagi Udemy untuk dapat menyediakan course yang memang dibutuhkan pasar. Masalahnya disini ialah bagaimana caranya mengetahui apakah course baru yang akan dirilis ini dapat meraih kesuksesan atau tidak, dimana biaya perilisan course baru tentunya membutuhkan modal yang tidak sedikit. 

Oleh karena itu, untuk dapat menyelesaikan permasalahan tersebut dibuatlah "Model Mesin Learning Success Percentage Prediction of course release". Sehingga Lembaga-Lembaga Pembelajaran Online dapat memprediksi persentase kesuksesan dari course yang akan dirilisnya dan menghindari terjadinya kerugian biaya produksi 
 

### 2.1 Problems
- Kualitas Pendidikan Menurun saat diterapkannya Sistem Pendidikan Jarak Jauh berbasis Teknologi (mediaindonesia.com)
- Penurunan partisipan pada Lembaga-lembaga Bimbingan Belajar akibat Covid-19 (sonora.id)
- Kesulitan dalam mencari pekerjaan akibat pandemi covid (kompas.com)
- Kesulitan untuk mengetahui course apa yang paling dibutuhkan mereka-mereka yang sedang ingin improving skill (Briyando, Boby.2020)

### 2.2 Goals
- Membuat model yang dapat memprediksi/mendeteksi sukses tidaknya suatu course yang akan dibuka oleh suatu MOOC dalam mendapatkan subscribers atau partisipan
- Mengetahui variabel apa saja yang dapat mempengaruhi sukses/tidaknya suatu course dalam mendapatkan subscribers atau partisipan

### 2.3 Limitasi
- Model dapat digunakan oleh seluruh perusahaan berbasis Platform Media Pembelajaran Online / MOOC / Bimbel dan perusahaan sejenis lainnya.
- Model hanya dapat memprediksi persentase sukses atau tidaknya course yang akan dibuka.

This dataset taken from kaggle : [https://www.kaggle.com/andrewmvd/udemy-courses]

### Sample Dataset

![](https://i.ibb.co/SPRPmvT/dataset.png)

Framework yang dilakukan dalam project kali ini ialah sebagai berikut.
> 1. Define Problem
> 2. Define Goals
> 3. Data Collect & Import
> 4. Cek Missing Value
> 5. Describe Data
> 6. EDA -- Handling Missing Value
> 7. Feature Engineering -- Handling Outliers
> 8. Export file Clean Data
> 9. Handling Imbalance Data
> 10. Train with Base Algorithm
> 11. Train with Complex Algorithm
> 12. Train Base with Hyper param
> 13. Train Complex with Hyper param
> 14. Classification Report
> 15. Confusion Matrix
> 16. Evaluation Model
> 17. Machine Learning Model Selection
> 18. Export Model
> 19. Dashboard (Joblib/Pickle)

Berdasarkan framework diatas, Model Machine Learning terpilih untuk memprediksi persentase kesuksesan perilisan course baru ialah menggunakan XGBoost Classifier dengan hasil berikut.

### Evaluation Metrics

| XGBoost |  |
| --- | --- |
| Accuracy | 0.77 |
| Precision | 0.71 |
| Recall | 0.66 |
| roc_auc | 0.75 |
| F1-Score | 0.68 |

### Dashboard Flask
**Overview**
![Overview](https://i.ibb.co/pz9H7kx/Daskboard.png)

**Data Visualization**
![Visualization](https://i.ibb.co/9rXNfyn/Daskboard-Visual.png)

**Data Prediction Result**
![Prediction](https://i.ibb.co/sjQxwJt/Daskboard-Predict.png)

### Contact Me

| Contact Method |  |
| --- | --- |
| Professional Email | fikriash24@gmail.com |
| Instagram | https://www.instagram.com/fikriash/ |
| LinkedIn | https://www.linkedin.com/in/fikri-aziz |
