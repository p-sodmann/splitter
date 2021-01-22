import numpy as np
from collections import defaultdict
import pickle

class Splitter:
    def __init__(self, k_splits:int):
        """
        Class to load and split into training and testing into k_splits folds.
        Can save state and add more data later.
        """
        
        # k_splits: how many folds are created
        self.k_splits = k_splits
        
        # dictionary of lists for each split
        # e.g. {0: [a,d,e], 1:[b,c,f]}
        self.splits = defaultdict(list)
        
        # keep track how many items are in each split
        self.split_lengths = np.zeros(k_splits)
    
    def add(self, item):
        # reduce probability for splits with more data
        distribution = ((sum(self.split_lengths) + 1) / (self.split_lengths + 1)) / self.k_splits
        probabilities = distribution / sum(distribution)
        
        # chose a split depending on the probabilities
        split = np.random.choice(self.k_splits, 1, p= probabilities)[0]
        
        # add item to the split
        self.splits[split].append(item)
        
        # update the split_lengths
        self.split_lengths[split] += 1
        
    def save(self, path):
        # save state to path
        with open(path, 'wb') as handle:
            pickle.dump(self.__dict__, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
    def load(self, path):
        with open(path, 'rb') as handle:
            loaded_state = pickle.load(handle)
            
        self.__dict__.update(loaded_state)