import os
import requests
from docx import Document
from io import BytesIO

file_path = "../datasets/word_files/2023_Jan_7_Feature_Engineering_Techniques.docx"

def readplain_doc():
    doc = Document(file_path)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    full_text = "\n".join(text)
    print(full_text)

def readstructured_doc():
    from unstructured.partition.docx import partition_docx
    import os
    import pandas as pd

    # elements = partition_docx(filename=file_path)
    elements = partition_docx(filename=file_path)

    list_of_elements = []

    for element in elements:
        element_dict = {
            "element_id": element.id,
            "file_path": file_path,
            "category": element.category,  # e.g. "Title", "NarrativeText", "ListItem"
            "text": element.text,
            "last_modified": element.metadata.last_modified,
        }

        list_of_elements.append(element_dict)

    elements_df = pd.DataFrame(list_of_elements)
    print(elements_df.head())

def read_pdf():
    import PyPDF2
    import os
    import pandas as pd

    file_path = "../datasets/pdf_files/2023_Jan_7_Feature_Engineering_Techniques.pdf"

    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        # Initialize an empty string to store the extracted text
        list_of_pages = []
        page_counter = 1

        for page in reader.pages:
            page_dict = {
                "file_name": reader.metadata.get("/Title"),
                "producer": reader.metadata.get("/Producer"),
                "page_number": page_counter,
                "text": page.extract_text(),
                "images": page.images,
            }

            list_of_pages.append(page_dict)

            page_counter += 1

    # Convert the list of pages to a pandas DataFrame
    pages_df = pd.DataFrame(list_of_pages)
    print(pages_df.head())

def read_xls():
    import os
    import pandas as pd

    file_path = "../datasets/csv_files/census-income.xlsx"
    df_excel = pd.read_excel(io=file_path)

    def create_text_description_of_row(row):
        row["text_description"] = (
            f"""The candidate {row['age']} years old is working in the
                {row['workclass']} sector. The candidate was born in
                {row['native-country']}, is {row['marital-status']}
                and has a {row['relationship']} relationship.
                The candidate has a {row['education']} degree
                and is working as a {row['occupation']}.
                The income of the candidate is {row['income']}."""
        )

        return row

    # Apply the function create_text_description_of_row to each row of the data frame
    df_extended = df_excel.apply(create_text_description_of_row, axis=1)

    print(df_extended.head())

def main():
    # readplain_doc()
    # readstructured_doc()
    # read_pdf()
    read_xls()


if __name__ == "__main__":
    main()
