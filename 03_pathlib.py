from pathlib import Path
import pandas as pd

if __name__ == '__main__':
    
    # Just using strings
    file_path = './data/test.csv'

    # Using pathlib
    # dir = Path(__file__).parent
    # file_path = dir / 'data/test.csv'
        
    df = pd.read_csv(file_path)

    print(df)

    