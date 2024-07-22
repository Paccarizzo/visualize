def create_df_colormask(styler, df): #default for conditional formating
    n_col = len(df.columns)
    n_row = len(df)
    style_array = [['false' for x in range(n_col)] for x in range(n_row)]
    
    for col in range(1,n_col):
        for row in range(1,n_row-1):
            if df.iat[row+1,col] != df.iat[row,col]:
                style_array[row][col] = 'true'
                

                
    styler.set_table_styles([  # create internal CSS classes
    {'selector': '.true', 'props': 'background-color: #99FF99;'},
    ], overwrite=False)
    
    cell_color = pd.DataFrame(style_array,
                            index=df.index,
                            columns=df.columns)
    
    styler.set_td_classes(cell_color)
    return styler
