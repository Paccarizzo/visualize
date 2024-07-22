def log_input_reader(lines:list[str]) -> list[list[str], list[str], list[str]]:
    mystr = ''
    for x in lines:
        mystr += x
    lines = mystr.split('mvbMON>')[1:]
    lines = [x.split('\n') for x in lines]

    port = []
    freshness = []
    values = []
    for x in lines:
        temp_p = ''
        temp_f = ''
        temp_v = ''
        stop = len(x)
        i = 0
        while i < stop:

            if 'dsg' in x[i].split(' ')[0]:
                temp_p += x[i].split(' ')[1]
                    
            if 'freshness timer:' in x[i]:
                i += 2
                temp_f += x[i]

            if 'dataset values:' in x[i]:
                i += 2
                while i < stop and x[i] != '':
                    temp_v += x[i]
                    i += 1
                i -=1
            i +=1
            
        port.append(temp_p)
        freshness.append(temp_f)
        values.append(temp_v)
    
    return [port, freshness, values]

def log_input_preparer(x:list[str, str, str]) -> list[str, str, str]:#[port,freshness,values]
    if '0x' in x[0]:
        port = str(int(x[0], 16))
    else:
        port = str(x[0])
    freshness = ''
    value = ''

    
    temp_f = x[1].split('0x')
    if len(temp_f) == 2:
        temp_f = temp_f[1]
        freshness = int(temp_f[:4],16)
    
    
    temp_v = x[2]
    temp_v = [x for x in temp_v.split(' ') if '0x' in x]
    

    for x in temp_v:
        value += format(int(x,16),'08b')
    return [port, freshness, value]

def log_reader(filepath: str, loaded_instructions: pd.DataFrame, Name_csv: str) -> None:
    my_file = open(filepath,"r")
    lines = my_file.readlines()
    my_file.close()

    inp = log_input_reader(lines) # [port, freshness, values]
    arranged_input = []
    for x in range(len(inp[0])):
        temp = log_input_preparer([inp[0][x], inp[1][x], inp[2][x]])
        arranged_input.append(temp)

## fix the to csv
    for x in arranged_input:
        temp = pd.DataFrame(mydict[x][1:], columns = mydict[x][0])
        mydict[x] = temp
        temp.to_csv(f'{Name_csv}_{x}.csv', header = 1) # INPUT: Name of csv file
    
    return
