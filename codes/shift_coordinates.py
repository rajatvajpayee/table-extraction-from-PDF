## @package shift_coordinates

# Function to shift and rescale the detected cells, from camelot space to pdf space

def find_cells(tables,ls,plot=None):
    """
    Args:
        tables: Table class which is identified by camelot
        ls : Dictionary of top-left and bottom-right coordinates of cells
        plot : Visualize the extraction if values is True.
    
    Return:
        A list of shifted coordinates for each cell available in the table
    """
    ## Calculation the width of table in camelot space
    width_s = abs(tables[0].cells[-1][-1].rb[0]-tables[0].cells[0][0].lt[0])
    ## Calculation the length of table in camelot space
    length_s = abs(tables[0].cells[0][0].lt[1]-tables[0].cells[-1][-1].rb[1])
    
    ## Identifying the outer boundaries of the table
    temp = list(tables[0]._image[1].keys())[0]
    x1,y1,x2,y2 = temp[0],temp[3],temp[2],temp[1]
    # top-left(x1,y1) and bottom-right(x2,y2)

    ## Calculation the width of table in PDF space
    width_b = x2-x1
    ## Calculation the length of table in PDF space
    length_b = y2-y1

    ## Identifying the y coordinate of top boundary of table in camelot space
    start = tables[0].cells[0][0].y2

    # Ratio of lengths and widths for PDF and camelot space
    r_l = length_b/length_s
    r_b = width_b/width_s
    
    Cells = []
    if plot:
        plt.figure(figsize=(30,20))
    img = tables[0]._image[0].copy()
    l,w,h = img.shape
    for x in ls.values():
        left = x[0];right=x[1]
        for i in range(len(left)):
            temp_l = (x1+int(r_l*(left[i][0]-left[0][0])),y1+abs(int(r_b*(abs(l-left[i][1]) -(l-start)))))
            temp_r = (x1+int(r_l*(right[i][0]-left[0][0])),y1+abs(int(r_b*(abs(l-right[i][1]) -(l-start)))))
            Cells.append([temp_l,temp_r])
            if plot:
                cv.rectangle(img,temp_l,temp_r,(0,0,255),10)
    if plot:
        plt.imshow(img)
        cv.imwrite('../cell.png',img)
    return(Cells)