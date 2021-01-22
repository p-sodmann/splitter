import numpy as np
from collections import defaultdict
import pickle

class Splitter:
    def __init__(self, k_splits:int=10, verbose=True, seed=None):
        """
        Class to load and split into training and testing into k_splits folds.
        Can save state and add more data later.
        """
        
        # k_splits: how many folds are created
        self.k_splits = k_splits
        
        # dictionary of lists for each split
        # e.g. {0: [a,d,e], 1:[b,c,f]}
        self.splits = defaultdict(list)
        
        # keep track of already processed items to avoid duplicates
        self.processed = []

        # keep track how many items are in each split
        self.split_lengths = np.zeros(k_splits)

        # if you want me to be silent init with verbose = False
        self.verbose = verbose

        # dont forget to optimize the seed ;D
        self.seed = seed
        self.rng = np.random.default_rng(seed = self.seed)
    
    def add(self, item):
        if item not in self.processed:
            # reduce probability for splits with more data
            distribution = ((sum(self.split_lengths) + 1) / (self.split_lengths + 1)) / self.k_splits
            probabilities = distribution / sum(distribution)
            
            # chose a split depending on the probabilities
            split = self.rng.choice(self.k_splits, 1, p=probabilities)[0]
            
            # add item to the split
            self.splits[split].append(item)
            
            # update the split_lengths
            self.split_lengths[split] += 1

            self.processed.append(item)

        else:
            if self.verbose:
                print(f"item {item} already processed.")

    def get_split(self, group_indices=[[0,1,2,3,4,5,6,7],[8],[9]]):
        """
        group_indices: List(List(split_index))
        
        example: [[0,1,2,3,4,5,6,7],[8],[9]]
        for the first 8 splits in the first list, then 1 for training and 1 for testing
        
        returns a list with the corresponding splits inside.
        """
        return_data = []

        for group in group_indices:
            split_data = []
            
            for split in group:
                split_data += self.splits[split]
                
            return_data.append(split_data)

        return return_data


    def save(self, path):
        # save state to path
        with open(path, 'wb') as handle:
            pickle.dump(self.__dict__, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
    def load(self, path):
        with open(path, 'rb') as handle:
            loaded_state = pickle.load(handle)
            
        self.__dict__.update(loaded_state)