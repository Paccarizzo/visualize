

def save_excel3(df):
    file_name = "my_file.xlsx"
    template = "path/to/the/excel/file/template.xlsx"
    sheetname = "my sheet"
    shutil.copy(template, file_name)

    
    with pd.ExcelWriter(file_name, engine = 'openpyxl', mode='a', if_sheet_exists = 'overlay') as writer: 
        df.to_excel(writer, sheet_name=sheetname, index = False, header = False, startrow = 1)##"Normal Distribution"
    return
