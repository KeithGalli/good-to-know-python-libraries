import pandas as pd
from pathlib import Path

# Before
# file_path = './data/test.csv'

# After
file_path = Path(__file__).parent / "data" / "test.csv"

df = pd.read_csv(file_path)

print(df)

# Get home directory path + Code directory
#print(Path().home() / "Code")