import pandas as pd
def table_view(args):
    tabele = pd.DataFrame(args)
    print(tabele)
    
table_view({
    id:1,
    "name":"anand",
    "age": "33",
    "course": ["javascript", "Ai","python"]
}
)