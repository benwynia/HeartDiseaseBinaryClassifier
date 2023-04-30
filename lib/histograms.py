#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""
Variable Histograms
Function: Create Histogram
This function creates a matrix of histograms for all numeric columns of the input dataframe. It calculates the optimal set of rows and columns for the histogram matrix based on the number of numeric columns in the dataframe. It uses the Seaborn library to plot histograms of each numeric variable in the dataframe.

Parameters:

df: Pandas DataFrame Input data frame containing numeric variables for which histograms are to be plotted. figsize: tuple, default=(15, 15) The figure size of the histogram matrix. bins: int, default=20 The number of bins to use for the histogram. color: str, default='steelblue' The color of the bars in the histogram. Output:

Displays a matrix of histograms for all numeric columns of the input dataframe. Required Libraries:

numpy matplotlib.pyplot seaborn

Example Usage:

python import pandas as pd import numpy as np import seaborn as sns import matplotlib.pyplot as plt

df = pd.DataFrame({'var1': [1,2,3,4,5], 'var2': [2,4,6,8,10], 'var3': [3,6,9,12,15], 'var4': [4,8,12,16,20]}) create_histogram(df)

Note: The function assumes that the input dataframe only contains numeric columns.
"""

def create_histogram(df, figsize=(15, 15), bins=20, color='steelblue'):
    # DOCUMENTATION: I asked ChatGPT to help write me this function, and then modified the output to meet my needs. 
    """
    Input:
    1. dataframe
    2. histogram resolution, figure size, and color (all defaults)
    
    Function:
    1. Caluclates the optimal set of rows and columns for the histogram matrix
    2. Creates a histogram matrix of each variable in the dataset
    3. Displays the histogram matrix 
    
    Outputs:
    None (future use could be to output this, cleanly formatted, to a PDF. This capability was beyond the scope of this project)
    
    
    """
    # Select only the numeric columsn for a histogram 
    num_columns = df.select_dtypes(include=['int', 'float']).columns

    # Calculate the number of rows and columns for the subplots, rounding up as necessary using np.ceil
    num_vars = len(num_columns)
    num_cols = int(np.ceil(np.sqrt(num_vars)))
    num_rows = int(np.ceil(num_vars / num_cols))

    # Create the figure and subplots
    fig, axes = plt.subplots(int(np.ceil(num_vars / num_cols)), int(np.ceil(np.sqrt(num_vars))), figsize=figsize)
    axes = axes.flatten()

    # Plot histograms for each numeric variable
    for idx, col in enumerate(num_columns):
        sns.histplot(data=df, x=col, kde=False, bins=bins, color=color, ax=axes[idx])
        axes[idx].set_title(col, fontsize=12)
        axes[idx].set_xlabel('')
        axes[idx].set_ylabel('')

    # Remove empty subplots
    for idx in range(num_vars, num_rows * num_cols):
        fig.delaxes(axes[idx])

    # Set a tight layout and show the plot
    plt.tight_layout()
    plt.show()


# In[ ]:


if __name__ == '__main__':
    print("Hello World")

