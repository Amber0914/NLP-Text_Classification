import argparse
import json
import csv

def convert_data(my_json, my_csv):
    input_json = open(my_json, "r", encoding="utf-8")
    with open(my_csv, "w", encoding="utf-8") as output_csv:
        csv_writer = csv.writer(output_csv)
        csv_writer = csv.writer(output_csv)
        flag = 0
        for line in input_json.readlines():
            dic = json.loads(line)
            # writing headline in the beginning
            if flag == 0:
                csv_writer.writerow(dic)
                flag = 1
            csv_writer.writerow(dic.values())
    print("Convert Success")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--json',
                        default='reviews_Clothing_Shoes_and_Jewelry_5.json',
                        help='XXXX.json, XXXX is the file name')
    parser.add_argument('--csv',
                        default='output.csv',
                        help='XXXX.csv, XXXX is the file name')
    args = parser.parse_args()
    
    convert_data(args.json, args.csv)
