import os
import pandas as pd

def compile_csv_files(folder_path, output_file):
    # List all CSV files in the specified folder
    csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

    # Check if there are any CSV files in the folder
    if not csv_files:
        print("No CSV files found in the specified folder.")
        return

    # Initialize an empty DataFrame to store the compiled data
    compiled_data = pd.DataFrame()

    # Loop through each CSV file and concatenate its data to the compiled DataFrame
    for csv_file in csv_files:
        file_path = os.path.join(folder_path, csv_file)
        df = pd.read_csv(file_path)
        compiled_data = pd.concat([compiled_data, df], ignore_index=True)

    # Save the compiled DataFrame to a new CSV file in the same directory
    output_path = os.path.join(folder_path, output_file)
    compiled_data.to_csv(output_path, index=False)
    print(f"Compilation complete. The compiled data is saved to {output_path}")

if __name__ == "__main__":
    folder_path = r"C:\Users\MEKARI\Desktop\bca_cc"
    output_file = "compiled_output.csv"

    compile_csv_files(folder_path, output_file)
