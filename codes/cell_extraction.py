## @package cell_extraction
# Function to extract the cell coordinates and save these into a dictionary. 
# These are top-left and bottom-right coordinates of each cell.

def end_points(tables):

    """
    Args : 
        tables: Tables list detected by camelot
    
    Returns:
        It returns a dictionary of top-left and bottom-right coordinates of cells, where keys are the row numbers of the table.
    """
    ls = {}
    for i,x in enumerate(tables[0].cells):

        temp = []
        left = [];right=[]
        for y in x:
            if y.left:                          ## Checks if there is a boundary in left 
                left.append(y.lt)               ## top-left coordinate 
            if y.right:                         ## Checks if there is a boundary in right
                right.append(y.rb)              ## bottom-right coordinate

        temp = [left,right]    
        ls[str(i)] = temp
    return(ls)