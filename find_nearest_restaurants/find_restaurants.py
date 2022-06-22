import pandas as pd
import numpy as np
from ast import literal_eval
from find_nearest_restaurants import dataset_path

class food_truck_finder:

    def __init__(self, coordinates, k, *args):
        """
        Args:
        - coordinates: the latitude and longitude of the location, in a tuple format
        - k: the number of restaurant to be found
        """
        self.dataset_path = dataset_path
        self.dataset = pd.read_csv(self.dataset_path)
        self.coordinates = coordinates
        self.k = k
    
    def preprocess_location(self):
        """
        Add a column to the pd dataframe that transforms the location value from string to tuple
        """
        self.dataset.dropna(subset=['Location'], inplace = True)
        self.dataset['LocationFloat'] = self.dataset.Location.apply(lambda x:self.convert_string_to_tuple(x))
        self.dataset = self.dataset[self.dataset['LocationFloat'] != (0,0)]

        return self.dataset

    def convert_string_to_tuple(self, dataset):
        """
        Utility function to convert string to tuple
        """
        try:
            return literal_eval(str(dataset))   
        except Exception as e:
            print(e)
            print("Could not convert the following item {item}".format(item = str(e)))
            return []
    
    def compute_distances(self):
        """
        Compute the distances from each restaurant to the desired location
        """
        self.dataset['Distances'] = self.dataset.LocationFloat.apply(lambda x: \
                                 (np.linalg.norm(np.array(x)-np.array(self.coordinates))))

        return self.dataset

    def get_top_k_locations(self):
        """
        Get the top k restaurants by closeness
        """
        self.preprocess_location()
        self.compute_distances()
        self.dataset.sort_values(by=['Distances'])
        return self.dataset.head(self.k)

    def get_pd_dataframe_top_k(self):
        """
        Return the data in a CLI friendly format
        """
        top_k = self.get_top_k_locations()

        pd.set_option('display.max_colwidth', 120)
        
        top_k = top_k[['Applicant', 'LocationDescription', 'Distances']]
        top_k.rename(columns = {'Applicant':'Restaurant Name', 'LocationDescription': 'Address', 'Distances': 'Distance'}, inplace = True)
        top_k.reset_index(drop=True, inplace=True)

        return top_k