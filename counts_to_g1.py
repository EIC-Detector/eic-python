# Calculate g1 and uncertainties from pseudodata counts in bins of (x,Q2).

# Import libraries.
import pandas as pd
import matplotlib.pyplot as plt

# Define functions.
def calc_D():
    return 1

def calc_g1( x, Q2, N ):
    return N

# Load data from .csv file.
disdata = pd.read_csv("discounts_eic_sphenix_20x250.csv")

print ( "Shape: ", disdata.shape )

# Create new column with g1 values calculated for each row in dataframe.
disdata['g1'] = disdata.apply( lambda row: calc_g1( row.x , row.Q2 , row.N ), axis=1 )

# Print head of dataframe with g1
print ( disdata.head() )
