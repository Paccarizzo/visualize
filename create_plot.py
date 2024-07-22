def create_plot():
    
    tempdf = []
    for key in table_var["plot"][2].keys():
        tempdf.append(pd.DataFrame({key:table_var["plot"][2][key]}))   
    df = pd.concat(tempdf, axis = 1)
    
    df_keys = [_ for _ in df.keys()]
    
    if 'Variables' in df_keys:
        timesteps = df['Variables']
        converted_ts = [datetime.strptime(ts, "%Y-%m-%d %H:%M:%S.%f") for ts in timesteps]
    else:
        converted_ts = range(len(df))
    
    plt.figure()
    for key in df_keys:
        if key != 'Variables':
            x1 = converted_ts
            x2 = [x for x in df[key]]
            
            plt.plot(
                x1, x2, 
                label = key, 
                marker= '.', 
                drawstyle='steps')

    plt.grid()
    plt.legend()
    plt.tight_layout()
    cursor(hover=True)

    plt.show()
