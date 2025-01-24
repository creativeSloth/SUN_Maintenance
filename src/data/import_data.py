import os

import pandas as pd

from database.queries.q_ref_data import import_articles_from_df


def import_articles_from_file(self, filename: str = None):
    """
    Determines the appropriate method to load a file based on its file extension
    and then loads the file into a pandas DataFrame.

    Parameters:
    filename (str): The path to the file to be loaded.

    Returns:
    pd.DataFrame: The loaded data as a DataFrame.

    Raises:
    ValueError: If the file extension is not supported.
    """
    # Extract the file extension and convert it to lowercase
    extension = os.path.splitext(filename)[1].lower()

    # Call the appropriate loading function based on the file extension
    if extension == ".xlsx":
        df = load_excel_to_dataframe(filename)
    elif extension == ".ods":
        df = load_ods_to_dataframe(filename)
    elif extension == ".csv":
        df = load_csv_to_dataframe(filename)
    else:
        # Raise an error if the file extension is unsupported
        raise ValueError(f"Unsupported file type: {extension}")

    import_articles_from_df(self, df)


def load_excel_to_dataframe(file_path: str = None, sheet_name: int = 0) -> pd.DataFrame:
    """
    Loads data from an Excel (.xlsx) file into a pandas DataFrame.

    Parameters:
    file_path (str): The path to the Excel file to be loaded.
    sheet_name (int): The sheet index to load (default is 0 for the first sheet).

    Returns:
    pd.DataFrame: The loaded data as a DataFrame.
    """
    # Load the Excel file with the 'openpyxl' engine, which supports .xlsx files
    df = pd.read_excel(file_path, sheet_name=sheet_name, engine="openpyxl")
    return df


def load_ods_to_dataframe(file_path: str = None, sheet_name: int = 0) -> pd.DataFrame:
    """
    Loads data from an OpenDocument Spreadsheet (.ods) file into a pandas DataFrame.

    Parameters:
    file_path (str): The path to the ODS file to be loaded.
    sheet_name (int): The sheet index to load (default is 0 for the first sheet).

    Returns:
    pd.DataFrame: The loaded data as a DataFrame.
    """
    # Load the ODS file with the 'odf' engine, which supports .ods files
    df = pd.read_excel(file_path, sheet_name=sheet_name, engine="odf")
    return df


def load_csv_to_dataframe(file_path: str = None) -> pd.DataFrame:
    """
    Loads data from a CSV file into a pandas DataFrame.

    Parameters:
    file_path (str): The path to the CSV file to be loaded.

    Returns:
    pd.DataFrame: The loaded data as a DataFrame.
    """
    # Load the CSV file using pandas' read_csv function
    df = pd.read_csv(file_path)
    return df
