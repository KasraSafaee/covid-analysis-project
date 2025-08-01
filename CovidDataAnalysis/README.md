# 📊 تحلیل داده‌های کرونا | COVID-19 Data Analysis

🔗 English version is available below.

---

## 🧪 درباره پروژه

این پروژه یک تحلیل کامل از داده‌های جهانی بیماری کرونا (COVID-19) است که شامل پاک‌سازی، تحلیل اکتشافی، تحلیل زمانی، تحلیل مقایسه‌ای کشورها و بررسی منطقه‌ای می‌شود.

📂 **ساختار پروژه**:
- `data/`: داده‌های خام و پاکسازی‌شده
- `notebooks/`: نوت‌بوک‌های Jupyter برای مراحل مختلف تحلیل
- `charts/`: نمودارهای ذخیره‌شده به‌صورت عکس
- `main.py`: فایل اصلی برای اجرای تحلیل و ذخیره نمودارها

📊 **منبع داده‌ها**:
داده‌ها از مخزن رسمی [Our World in Data](https://ourworldindata.org/coronavirus) استخراج شده‌اند:
```
https://raw.githubusercontent.com/owid/covid-19-data/refs/heads/master/public/data/owid-covid-data.csv
```

---

## 📦 کتابخانه‌های استفاده‌شده

- `pandas` — پردازش و تحلیل داده
- `matplotlib` — رسم نمودارهای تصویری
- `seaborn` — تجسم‌های آماری زیباتر
- `os` — مدیریت مسیر و ذخیره فایل

---

## 🚀 نحوه اجرا

1. ابتدا تمام کتابخانه‌های موردنیاز را نصب کنید:

```bash
pip install pandas matplotlib seaborn
```

2. سپس فایل `main.py` را اجرا کنید:

```bash
python main.py
```

📁 خروجی نمودارها به‌صورت خودکار در پوشه‌ی `charts/` ذخیره می‌شوند.

---

## 🖼 مثال نمودار ذخیره‌شده

<img src="charts/rolling_deaths_Armenia.png" width="500">

---

## ✨ مشارکت

اگر پیشنهادی برای بهبود پروژه دارید یا می‌خواهید همکاری کنید، خوشحال می‌شویم Pull Request یا Issue ثبت کنید.

---

---

# 📊 COVID-19 Data Analysis Project

## 🧾 About

This is a complete data analysis project of the global COVID-19 dataset. It includes:

- Cleaning and preprocessing
- Exploratory analysis
- Time series analysis
- Country-wise comparison
- Regional trends

📂 **Structure**:
- `data/`: Raw and cleaned CSV files
- `notebooks/`: Jupyter notebooks for step-by-step analysis
- `charts/`: Saved charts and figures
- `main.py`: Script to generate and save all plots

📊 **Data Source**:
From [Our World in Data](https://ourworldindata.org/coronavirus):
```
https://raw.githubusercontent.com/owid/covid-19-data/refs/heads/master/public/data/owid-covid-data.csv
```

---

## 🛠 Libraries Used

- `pandas` — Data handling
- `matplotlib` — Plotting
- `seaborn` — Statistical graphics
- `os` — File system operations

---

## 🚀 How to Run

1. Install dependencies:

```bash
pip install pandas matplotlib seaborn
```

2. Run the script:

```bash
python main.py
```

📁 Charts will be saved to the `charts/` directory.

---

## ✨ Contribute

Feel free to open an issue or submit a pull request if you'd like to improve the project.

---

## 📂 محل تحلیل‌ها | Location of Notebooks

تمام تحلیل‌ها در پوشه `notebooks/` قرار دارند، از جمله پاکسازی داده، تحلیل اکتشافی، تحلیل زمانی، مقایسه کشورها، و تحلیل منطقه‌ای.

All analyses are located in the `notebooks/` folder, including data cleaning, exploratory analysis, time series analysis, country comparison, and regional insights.
