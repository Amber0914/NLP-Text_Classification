# [NLP: Text-Classification Tutorial](https://medium.com/@qempsil0914/machine-learning-nlp-text-classification-with-amazon-review-data-using-python3-step-by-step-3fb0cc0cecc1)
The relative concept and step-by-step tutorial can be obtained from [here](https://medium.com/@qempsil0914/machine-learning-nlp-text-classification-with-amazon-review-data-using-python3-step-by-step-3fb0cc0cecc1).

## [Amazon Dataset](http://jmcauley.ucsd.edu/data/amazon/)
We take the [Clothing, Shoes and Jewelry dataset](http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Clothing_Shoes_and_Jewelry_5.json.gz) for demonstration, and you can choose any dataset for practice.

## Command for converting json to csv
```
python3 convert_json_to_csv.py --json=json_file_name.json --csv=csv_file_name.csv
```

## Command for training & testing model
```
python3 text_classification.py --dataset=file_name.csv
```

## Requirements.txt
```
pandas==0.23.4
scikit-learn==0.19.2
```

**Command for install**
```
pip3 install -r requirements.txt
```
