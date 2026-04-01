def pipeline(day, value_list, marker, max_sum, new_values):
    if marker == 'O':
        if sum(value_list) < a:
            if int(sum(value_list) + int(min((df.loc[i,'Column'],new_values[i-1])))) == a:
                df.loc[i,str(day + 5)] = int(min((df.loc[i,'Column'],new_values[i-1])))
                value_list.append(df.loc[i,str(day + 5)])
            elif int(sum(value_list) + int(min((df.loc[i,'Column'],new_values[i-1])))) > a:
                if df.loc[i,str(day + 5)] == int(min((df.loc[i,'Column'],new_values[i-1]))):
                    pass
                else:
                    df.loc[i,str(day + 5)] = a - sum(value_list)
                    value_list.append(df.loc[i,str(day + 5)])
    if marker_2 == 'DO':
        if sum(value_list) < a:
            if int(sum(value_list) + int(min((df.loc[i,'Column'],new_values[i-1])))) == a:
                df.loc[i,str(day + 6)] = int(min((df.loc[i,'Column'],new_values[i-1])))
                value_list.append(df.loc[i,str(day + 6)])
            elif int(sum(value_list) + int(min((df.loc[i,'Column'],new_values[i-1])))) > a:
                if df.loc[i,str(day + 6)] == int(min((df.loc[i,'Column'],new_values[i-1]))):
                    pass
                else:
                    df.loc[i,str(day + 6)] = a - sum(value_list)
                    value_list.append(df.loc[i,str(day + 6)])
    return value_list

def main()
    pipeline()
