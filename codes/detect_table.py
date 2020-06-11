## @package detect_table
# This function performs two operations -
# 1. Identify the optimal parameter value at which we can extract the maximum number of tables from a pdf
# 2. Returns the tables in a list which are extracted from the pdf
def optimize(file,mm,nn):
    """
    Args:
        file = path of the pdf file
        mm = minimum line_scale value
        nn = maximum line_scale value

        ## line_scale : It is the threshold value of a line segment which can be considered as a line. 
        As this value increases, algorithm will also be able to detect the shorter line segements.
        A large value (1000) and a smaller value (2) will give more false positives. It means that higher value will even consider a letter
        as a table while a lower value may not be able to extract any table from the pdf.
    
    Returns:
        Return the tables obtained from the pdf
    """
    xx = [] ; yy = []
    print('Finding Optimal Solution ...')
    for i in tqdm_notebook(range(mm,nn,20)):
        try:
            tables = myfun(file,i)
            xx.append(i)
            yy.append(len(tables))
            
        except:
            print('GhostscriptError')
            break
    k = max(yy)
    np.where(np.asarray(yy) == int(k))
    kk = xx[np.where(np.asarray(yy) == int(k))[0][0]]
    final = myfun(file,kk)
    print('Total number of tables found {}'.format(len(final)))
    boxess = final[0]._image[1]
    plt.figure(figsize=(30,20))
    img = final[0]._image[0].copy()
    for x in range(len(final)):
        temp = list(boxess.keys())[x]
        x1,y1,x2,y2 = temp[0],temp[3],temp[2],temp[1]
        cv.rectangle(img,(x1,y1),(x2,y2),(255,0,255),10)
        i = i+1
    plt.imshow(img)

    return(final)