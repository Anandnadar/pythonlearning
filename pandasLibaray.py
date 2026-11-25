import pandas as pd
order_detaisl = pd.read_table(filepath_or_buffer="data.tsv.txt")
order_detaisl.describe(include="all")
print(order_detaisl)