# Sales Data Analysis & Power BI Dashboard

## Included
- `data/sales.csv`: small practice retail dataset.
- `clean_sales.py`: checks, cleans and exports `data/cleaned_sales.csv`.
- `analysis.py`: answers common business questions and saves charts in `outputs/`.
- `powerbi/DAX_measures.txt`: measures to create in Power BI.
- `powerbi/dashboard_guide.md`: suggested report layout.

## Run with Python
```bash
pip install -r requirements.txt
python clean_sales.py
python analysis.py
```

Then open Power BI Desktop:
1. Get Data > Text/CSV > select `data/cleaned_sales.csv`.
2. Check data types in Power Query, then Close & Apply.
3. Create the measures in `powerbi/DAX_measures.txt`.
4. Build visuals using the guide.

The included dataset is synthetic practice data, not a Kaggle dataset. Replace it with a permitted public retail dataset for a portfolio version, and update your project description to match the work actually completed.
