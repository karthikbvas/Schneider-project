import camelot
import os

def extract_tables(pdf_path, output_dir):
    manual_name = os.path.splitext(os.path.basename(pdf_path))[0]
    tables = camelot.read_pdf(pdf_path, pages="all")
    for i, table in enumerate(tables):
        table.df.to_csv(f"{output_dir}/{manual_name}_table_{i}.csv", index=False)
    print(f"Extracted {len(tables)} tables for {manual_name}")

# Example usage
extract_tables("D:\\Schneider project\\manuals\\washing_machine.pdf", "D:\\Schneider project\\extracted")

