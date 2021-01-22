# splitter
K-Fold Data Splitting with persistence
  
## installation:
  
no pypi package planned so far.  
´´´
git clone https://github.com/p-sodmann/splitter/
cd splitter
pip install .
´´´

## usage:

´´´
from splitter.splitter import Splitter

splitter = Splitter(k_splits)

example_data = ["a", "b", "c", "d", "e", "f"]

for example in example_data:
    splitter.add(example)
    
splitter.splits
>>> defaultdict(list, {8: ['a'], 4: ['b'], 2: ['c', 'f'], 0: ['d'], 1: ['e']})
´´´
