import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

def azureml_main(df = None, dataframe2 = None):

    # Execution logic goes here
    # using KMeans function to form 5 clusters based on lift
    def kmeans_clustering(df, metric):
    
        df = df.sort_values(by=[metric])

        metric_kmeans = KMeans(n_clusters=5, random_state=0).fit(np.reshape(df[metric].values, (-1,1)))

        # get the labels
        labels = metric_kmeans.labels_
        print(labels)

        # match category names to labels 
        label_names = []
        for label in labels:
            if str(label) not in label_names:
                label_names.append(str(label))
        category_names = ["very low", "low", "medium", "high", "very high"]
        
        # predicting the metric column from the original unsorted array to 
        # maintain original order of records
        metric_kmeans.predict(np.reshape(df[metric].values, (-1,1)))     
        labels = metric_kmeans.predict(np.reshape(df[metric].values, (-1,1))) 

        # assigning the correct category name to records 
        metric_category = []

        for label in labels:
            for i in range(5):
                if str(label) == label_names[i]:
                    metric_category.append(category_names[i])
                    break
                
        df[str(metric+'_category')] = metric_category
        
        return df
    
    df = df.loc[((df['lift']<0.8) | (df['lift']>1.2))]
    df = kmeans_clustering(df, 'confidence')
    df = kmeans_clustering(df, 'support')
    
    confidence_tier_mapping = {'very low': 5, 'low': 4, 'medium': 3, 'high': 2, 'very high': 1}
    support_tier_mapping = {'very low': 0.5, 'low': 0.4, 'medium': 0.3, 'high': 0.2, 'very high': 0.1}
    
    confidence_tiers = [confidence_tier_mapping[i] for i in df['confidence_category'].values]
    support_tiers = [support_tier_mapping[i] for i in df['support_category'].values]
    
    tiers = [x + y for x, y in zip(confidence_tiers, support_tiers)]
    df['tiers'] = tiers
    df.tiers = df.tiers.round(decimals=1)
    
    return df,