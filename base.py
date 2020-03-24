import pandas as pd
import datetime
import csv
def check(output, per = 15):
    df = pd.read_csv("sub.csv")
    df1 = pd.read_csv("ent_ext.csv")
    out = output.split(',')
    time = datetime.datetime.now()
    time1 = time.hour
    out.append(time1)
    print(out)
    id = out[0]
    if id not in list(df['regno']):
        print('no')
        return (0, 0)
    else:
        if id not in list(df1['regno']):
            with open('ent_ext.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow(out)
                return (1, out)
        else:
            '''
            a = df1.loc[df1['regno'] == id]
            print('\n')
            print(a)
           '''
            for i in range(len(df1["regno"])):
                if df1["regno"][i] == id:
                    #df1.insert(i, "exit", time1, allow_duplicates = True)
                    #print(df1["entry"][i])
                    t2 = df1["entry"][i]
                    #print("Needed in this format: ", time1)
                    delta = time1 - t2
                    print(delta)
                    price = per*delta + per
    return (price, out)
            
