from cargills import CargillsDataset
from utils_base import Console

def main():
    dataset = CargillsDataset()
    idx = dataset.description_to_date_to_price
    for description in idx:
        date_to_price = idx[description]
        if len(date_to_price) == 1:
            continue
        
        print(Console.note(description))
        for date_id in idx[description]:
            price = idx[description][date_id]
            print(Console.normal(f'\t{date_id}\t{price:.2f}'))  

if __name__ == '__main__':
    main()
