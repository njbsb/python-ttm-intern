import pandas as pd
import time
import sys
import os
import datetime


def logDuration(start, end):
    totaltime = int(end - start)
    return str(datetime.timedelta(seconds=totaltime))


def reindex_column(df):
    colname = list(df.columns)
    colnames = [i.replace(i, str(colname.index(i))) for i in colname]
    df.columns = colnames
    return df


def reindex_row(df):
    rowlength = df.shape[0]
    newindex = pd.Series([i for i in range(rowlength)])
    df = df.set_index(newindex)
    return df


def getGroup(df):
    # list contain index of new group of data, detects 'zhpla report' from column 0/A
    listofindex = []
    for i, row in df.iterrows():
        if type(row[0]) == str and 'ZHPLA' in row[0]:
            listofindex.append(i)
    return listofindex, len(listofindex)


def getDFGroup(df):
    starttime = time.time()
    listofindex, count = getGroup(df)
    dflist = []
    gap = 3
    dropaxis = [1]
    for i in range(count):
        start = listofindex[i]
        if i < count-1:
            end = listofindex[i + 1]
            df_ = df.iloc[start + gap: end]
        else:
            df_ = df.iloc[start + gap:]
        for axis in dropaxis:
            df_ = df_.dropna(how='all', axis=axis)
        dflist.append(df_)
    print('group =', len(dflist))
    endtime = time.time()
    print('getDFGroup,', logDuration(starttime, endtime))
    return dflist


def getCleanDF(dflist):
    start = time.time()
    count = 0
    print("Adjusting columns...")
    for i, df in enumerate(dflist):
        df = reindex_row(df)

        df = reindex_column(df)
        for colname, column in df.iteritems():
            if not pd.isna(column[1]):  # if row 1 has value/column name
                if pd.isna(column[0]):  # if row 0 already has column name
                    df[colname] = df[colname].shift(-1)
                else:
                    newcol = str(len(df.columns) + 1)
                    df[newcol] = column
                    df[newcol] = df[newcol].shift(-1)  # shift the sunken
                    for dfcol in [df[colname], df[newcol]]:
                        # print("dfcol ", dfcol)
                        for index, row in dfcol.iteritems():
                            if not index == 0:
                                if index in (1, 2) or index % 2 == 0:
                                    dfcol[index] = float('nan')
        df = df.dropna(how='all')

        df.columns = df.iloc[0]
        df = df[1:]
        dflist[i] = df
        count += len(df)
    cleandf = pd.concat(dflist).reset_index(drop=True)
    print('\ncount =', count)
    end = time.time()
    print('dataframe cleaned, ', logDuration(start, end))
    return cleandf


def addcolumn_possum(df):
    start = time.time()
    possum_column = ['Position', 'Section', 'Department',
                     'Division', 'Sector', 'Comp. Position', 'Business']
    df['Pos SUM'] = df[possum_column].apply(
        lambda x: ', '.join(x.dropna().astype(str)), axis=1)
    end = time.time()
    print('added pos SUM, ', logDuration(start, end))
    return df


def addcolumn_superior(df):
    start = time.time()
    df_staff = df[['Pos ID', 'Staff No', 'Staff Name']].drop_duplicates()
    df_staff.rename(columns={'Pos ID': 'Superior Pos ID',
                             'Staff No': 'Superior ID', 'Staff Name': 'Superior Name'}, inplace=True)
    newdf = pd.merge(df, df_staff, on='Superior Pos ID', how='left')
    end = time.time()
    print('added column superior: ', logDuration(start, end))
    return newdf


def addcolumn_consoJG(df):
    start = time.time()
    column_consoJG = []
    jg_head = ['', 'Est. ', 'Eqv. ']
    df_jg = df[['JG', 'Est.JG', 'EQV JG']].fillna('-')
    for i, eachrow in df_jg.iterrows():
        for index, val in enumerate(list(eachrow)):
            if not val == '-':
                conso = jg_head[index] + str(val)
                column_consoJG.append(conso)
                break
            else:
                if(index == 2 and val == '-'):
                    column_consoJG.append('No JG')
                else:
                    continue
    df['Conso JG'] = column_consoJG
    end = time.time()
    print('added column consoJG, ', logDuration(start, end))
    return df


def arrange_column(df):
    start = time.time()
    col_order = ['Staff No', 'Staff Name', 'SG', 'Lvl', 'Tier', 'JG', 'Est.JG', 'EQV JG',
                 'Conso JG', 'OLIVE JG', 'Pos ID', 'Pos SUM', 'Superior Pos ID', 'Superior ID', 'Superior Name',
                 'Position', 'Sec ID', 'Section', 'Dept ID', 'Department', 'Division ID', 'Division', 'Sector ID',
                 'Sector', 'Comp. ID Position', 'Comp. Position', 'Buss ID', 'Business', 'C.Center', 'Gender', 'Race',
                 'Zone', 'Home SKG', 'Pos.SKG', 'JobID(C)', 'Level', 'NE Area', 'Loc ID', 'Location Text', 'Vac Date',
                 'Start Date', 'End Date', 'Vacancy Status', 'Email Address', 'Mirror Pos ID', 'Mirror Position', 'EG Post. ID',
                 'EG Position', 'ESG Post. ID', 'ESG Position', 'PT1', 'PT2', 'Overseas Staff No', 'Overseas Staff Name', 'Overseas Staff Comp. ID',
                 'Overseas Staff Comp.', 'Staff Comp. ID', 'Staff Comp.', 'Staff EG ID', 'Staff EG', 'Staff ESG ID', 'Staff ESG', 'Staff Work Contract ID', 'Staff Work Contract'
                 ]
    colname_date = ['End Date', 'Vac Date', 'Start Date']
    for colname in colname_date:
        df[colname] = df[colname].str.replace('.', '/', regex=False)
    df['Email Address'] = df['Email Address'].str.lower()
    df = df.reindex(columns=col_order)
    end = time.time()
    print('arranged columns, ', logDuration(start, end))
    return df


def preProcess():
    output = input('Please insert output file name\nOutput file name: ')
    outputfile = output + '.xlsx'
    return outputfile


def mainProcess(zhplapath, outputname):
    dfRaw = pd.read_excel(zhplapath)
    dflist = getDFGroup(dfRaw)
    cleandf = getCleanDF(dflist)

    df = addcolumn_possum(cleandf)
    df = addcolumn_superior(df)
    df = addcolumn_consoJG(df)
    df = arrange_column(df)
    print('FINAL\n', df)
    # df.to_excel(outputname, index=None)
    return df


zhplapath = r'D:\Documents\Python\project-2\database\input\ZHPLA_July2020.xlsx'
outputname = 'zhpla_clean.xlsx'
# zhplapath = r'D:\Documents\Python\project-2\database\input\ZHPLA_June2020_raw.xlsx'
# zhplapath = r'D:\Documents\Python\project-2\database\input\zhplac.xlsx'

# outputname = preProcess()
df = mainProcess(zhplapath, outputname)
