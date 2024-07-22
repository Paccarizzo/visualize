import pandas as pd
def instructions2(args:list):
  Instruction_file_path = args[0]
  Instruction_sheet_name = args[1]
  Variable_name_column = args[2]
  Port_nr_column = args[3]
  Byte_offset_column = args[4]
  Bit_offset_column = args[5]
  Data_type_column = args[6]
  df = pd.read_excel(Instruction_file_path,
                     sheet_name=Instruction_sheet_name,
                     dtype=str)
  #since we pass a vector as sheet name the return type will be a dict with multiple dataframes
  #the sheet names are the keys: {sheet1:df1, sheet2:df2, sheet3:df3}
  df = pd.concat(df.values(), ignore_index=True)
  #combine all nested dataframes into a single one
  df = df[[
      Port_nr_column,
      Variable_name_column,
      Byte_offset_column,
      Bit_offset_column,
      Data_type_column
      ]]
  #choose the relevant columns
  
  data = df[
      pd.to_numeric(
      df[Bit_offset_column],
      errors='coerce',
      downcast='integer'
      ).notnull()
      ]
  #The first part converts all non numeric cells to NaN
  #notnull removes all NaN cells leaving only the row with relevant information
  #important here is not the numeric conversion but the detection of numeric values
  
  data.reset_index(inplace=True, drop=True)
  data = data.rename(
      columns={
          Port_nr_column: "Port Nr",
          Variable_name_column: 'Primary Text',
          Byte_offset_column: "Byte_offset",
          Bit_offset_column: "Bit_offset",
          Data_type_column: "Data Type"
          }
      )
  #for further reference it is desirable that the naming convention is standardised
  #and not reliant on the different conventions from the excel sheets
  
  data['Port Nr'] = data['Port Nr'].apply(
                      lambda x: int(x, base=16) 
                      if '0x' in x
                      else int(x, base=10)
                      )
  #this converts hexadecimals to base 10 ints
  
  return data # column names: [Port Nr, Primary Text, Byte_offset, Bit_offset, Data Type]


