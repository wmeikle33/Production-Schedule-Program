    if marker == 'O':
        if sum(total_list) < a:
            if int(sum(total_list) + int(min((df.loc[i,'Column'],new_list[i-1])))) == a:
                df.loc[i,str(day_2 + 5)] = int(min((df.loc[i,'Column'],new_list[i-1])))
                total_list.append(df.loc[i,str(day_2 + 5)])
            elif int(sum(total_list) + int(min((df.loc[i,'Column'],new_list[i-1])))) > a:
                if df.loc[i,str(day_2 + 5)] == int(min((df.loc[i,'Column'],new_list[i-1]))):
                    pass
                else:
                    df.loc[i,str(day_2 + 5)] = a - sum(total_list)
                    total_list.append(df.loc[i,str(day_2 + 5)])
    if marker_2 == 'DO':
        if sum(total_list) < a:
            if int(sum(total_list) + int(min((df.loc[i,'Column'],new_list[i-1])))) == a:
                df.loc[i,str(day_2 + 6)] = int(min((df.loc[i,'Column'],new_list[i-1])))
                total_list.append(df.loc[i,str(day_2 + 6)])
            elif int(sum(total_list) + int(min((df.loc[i,'Column'],new_list[i-1])))) > a:
                if df.loc[i,str(day_2 + 6)] == int(min((df.loc[i,'Column'],new_list[i-1]))):
                    pass
                else:
                    df.loc[i,str(day_2 + 6)] = a - sum(total_list)
                    total_list.append(df.loc[i,str(day_2 + 6)])
