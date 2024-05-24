import csv

def parse_vehicle_data(file_path):
    with open(file_path) as f:
        reader = csv.reader(f)
        data = []
        for row in reader:
            data.append({
                "model": row[0],
                "make": row[1],
                "year": int(row[2]),
                "price": int(row[3]),
                "discount": 0
            })
        return data

if __name__ == "__main__":
    print(parse_vehicle_data("vehicles.txt"))