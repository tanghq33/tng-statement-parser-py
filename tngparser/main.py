import camelot
import pandas as pd
from directory import get_files
from naming import snake_case, fix_spaces
from utility import init_logger, extract_convert_date_range

def parse_pdf(path: str) -> pd.DataFrame:
    column_separator = ['80,140,230,295,460,657,750']
    first_page = ['15,369,823,51']
    first_table = camelot.read_pdf(path, flavor='stream', pages='1', columns=column_separator, table_areas=first_page, split_text=True)

    other_page = ['15,579,823,51']
    other_tables = camelot.read_pdf(path, flavor='stream', pages='2-end', columns=column_separator, table_areas=other_page, split_text=True)

    dfs = []
    for table in first_table:
        dfs.append(table.df)

    for table in other_tables:
        dfs.append(table.df)

    df = pd.concat(dfs)

    return df

def process_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    temp_df = df.copy()
    
    temp_df.columns = temp_df.iloc[0].transform(snake_case).str.upper().astype(str) # Strip symbols and convert snake case, set as header
    temp_df = temp_df[1:] # Remove first row

    temp_df['DATE'].fillna("", inplace=True)

    temp_df.loc[temp_df['DATE'] != "", 'GROUP'] = True # Mark non empty row
    temp_df['GROUP'].fillna(False, inplace=True) # Mark empty row
    group = temp_df['GROUP'].cumsum() # Get group index
    temp_df.drop('GROUP', axis=1, inplace=True) # Drop temperory header

    temp_df = temp_df.groupby(group).agg('\n'.join)
    temp_df = temp_df.apply(lambda x: x.str.strip())

    # Data cleaning
    temp_df['TRANSACTION_TYPE'] = temp_df['TRANSACTION_TYPE'].apply(lambda x: fix_spaces(x.replace('\n', ''))).transform(snake_case).str.upper()
    temp_df['AMOUNT_RM'] = temp_df['AMOUNT_RM'].str.replace('RM', '').replace(' ', '')
    temp_df['WALLET_BALANCE'] = temp_df['WALLET_BALANCE'].str.replace('RM', '').replace(' ', '')
    temp_df['REFERENCE'] = temp_df['REFERENCE'].apply(lambda x: x.replace('\n', '').replace(' ', ''))
    temp_df['DETAILS'] = temp_df['DETAILS'].apply(lambda x: x.replace('\n', '').replace(' ', '') if '\n' in x else x)
    temp_df['DESCRIPTION'] = temp_df['DESCRIPTION'].apply(lambda x: fix_spaces(x.replace('\n', ' ')))

    return temp_df

def main():
    files = get_files('/Users/haoquantang/Downloads/statements', '*.pdf')

    dfs = []

    for file in files:
        df = parse_pdf(file)
        df = process_dataframe(df)

        df.to_csv(file.replace('.pdf', '.csv'), index=False)

        dfs.append(df.copy())

    all_df = pd.concat(dfs, ignore_index=True)
    all_df = all_df.drop_duplicates(subset='REFERENCE', keep="first")
    all_df.to_csv('all.csv', index=False)

if __name__ == "__main__":
    main()