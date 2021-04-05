import importlib.util
import os

package_name = 'mlxtend'
spec = importlib.util.find_spec(package_name)
if spec is None:
    os.system(f"pip install mlxtend")

package_name = 'dask'
spec = importlib.util.find_spec(package_name)
if spec is None:
    os.system(f"pip install dask")
os.system(f'pip install "dask[dataframe]" --upgrade')

# imports
import pandas as pd
import dask.dataframe as dd
from mlxtend.frequent_patterns import apriori, association_rules
def azureml_main(dataframe1 = None, dataframe2 = None):

    # Execution logic goes here
    print(f'Input pandas.DataFrame #1: {dataframe1}')

    ddf = dd.from_pandas(dataframe1, npartitions=1435)
    print("finding freq items")
    freq_items = apriori(ddf.compute(), min_support = 0.005, use_colnames = True)
    print(freq_items)
    print(freq_items.at[10, 'itemsets'])
    print("finding association rules")
    
    rules = association_rules(freq_items, metric="confidence", min_threshold=0)
    rules['antecedents']=rules['antecedents'].apply(lambda x: ','.join(set(list(x))))
    rules['consequents']=rules['consequents'].apply(lambda x: ','.join(set(list(x))))
    filtered_rules = rules.loc[rules['consequents'].isin(['fair_poor_pc-1','fair_poor_pc-2','fair_poor_pc-3','fair_poor_pc-4','fair_poor_pc-5'])]
    filtered_rules = filtered_rules.sort_values(['support', 'confidence', 'lift'], ascending =[False, False, False])

    return filtered_rules[['antecedents','consequents','support','confidence','lift']], rules