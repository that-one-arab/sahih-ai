import csv
import pandas as pd
from langchain.docstore.document import Document


def create_csv_data(quran_data_file_path: str, hadiths_data_file_path: str, data_file_path: str):
    """
    Loads and transforms csv hadith data into langchain document objects.

    Parameters:
        file_path (str): Path to csv file

    Returns:
        list[Document]: Langchain document objects
    """

    # quran_df = pd.DataFrame()
    # quran = pd.read_csv(quran_data_file_path)

    # quran_df['id'] = "quran-" + quran['ayah_no_quran'].astype(str)
    # quran_df['value'] = quran['ayah_ar']
    # quran_df['translation'] = quran['ayah_en']
    # quran_df['source'] = quran['surah_name_roman'] + " - " + quran['ayah_no_surah'].astype(str)

    hadith = pd.read_csv(hadiths_data_file_path)
    hadith_df = pd.DataFrame()

    hadith_df['id'] = "hadith-" + hadith['hadith_id'].astype(str)
    hadith_df['value'] = hadith['text_ar']
    hadith_df['translation'] = hadith['text_en']
    hadith_df['source'] = hadith['source'] + " chapter: " + hadith['chapter'].astype(str) + " " + hadith['chapter_no'].astype(str) + " -" + hadith['hadith_no'].astype(str)

    # Append the extra data to the new data
    # combined = pd.concat([quran_df, hadith_df])
    combined = pd.concat([hadith_df])

    # Write the combined data to a new CSV file
    combined.to_csv(data_file_path, index=False)

def load_hadith_csv_to_documents(file_path: str) -> list[Document]:
    """
    Loads and transforms csv hadith data into langchain document objects.

    Parameters:
        file_path (str): Path to csv file

    Returns:
        list[Document]: Langchain document objects
    """

    documents = []

    with open(file_path, newline="") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            content = row["translation"].strip()
            metadata = {
                "id": row['id'].strip(),
                "arabic": row['value'].strip(),
                "source": row['source'].strip()
            }

            doc = Document(page_content=content, metadata=metadata)
            documents.append(doc)

    return documents

