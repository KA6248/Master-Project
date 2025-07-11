# /content/nlp_project/data_loader.py

import pandas as pd

# Label encoding (English)
LABEL_MAP = {
    "Unbiased": 0,
    "Biased against Palestine": 1,
    "Biased against Israel": 2,
    "Biased against Muslims": 3,
    "Biased against Jews": 4
}

# Explicit type mapping
EXPLICIT_MAP = {
    "explicit": "Explicit",
    "implicit": "Implicit",
    "": "Unknown",
    "nan": "Unknown"
}

def standardize_text(s):
    return str(s).strip().lower()

def load_and_merge_datasets(csv_path, excel_path):
    # Load political bias data
    df1 = pd.read_csv(csv_path, encoding="utf-8")
    df1["bias_domain"] = "Political"
    df1.rename(columns={"bias_type": "explicit_type"}, inplace=True)

    # Load religious bias data
    df2_raw = pd.read_excel(excel_path)
    df2 = pd.DataFrame()
    df2["text"] = df2_raw["text"]
    df2["label"] = df2_raw["bias_religious"]
    df2["explicit_type"] = df2_raw["type"]
    df2["bias_domain"] = "Religious"

    # Standardize labels and types
    for df in [df1, df2]:
        df["label"] = df["label"].apply(standardize_text)
        df["explicit_type"] = df["explicit_type"].apply(standardize_text)

        df["label"] = df["label"].replace({
            "unbiased": "Unbiased",
            "biased against palestine": "Biased against Palestine",
            "biased against israel": "Biased against Israel",
            "biased against muslims": "Biased against Muslims",
            "biased against islam": "Biased against Muslims",
            "biased against jews": "Biased against Jews",
            "biased against judaism": "Biased against Jews"
        })

        df["explicit_type"] = df["explicit_type"].replace(EXPLICIT_MAP)

    # Merge both datasets
    df = pd.concat([df1, df2], ignore_index=True)

    # Encode label
    df["label_id"] = df["label"].map(LABEL_MAP)

    # Drop incomplete rows
    df = df.dropna(subset=["text", "label", "explicit_type"])
    df = df[df["label"].isin(LABEL_MAP.keys())]

    # Save final cleaned dataset
    final_path = "/content/merged_bias_data_cleaned.csv"
    df.to_csv(final_path, index=False, encoding="utf-8")
    print(f"✅ Cleaned merged dataset saved to: {final_path}")

    return df.reset_index(drop=True)

def dashboard_eda(df):
    print("📊 Dataset Shape:", df.shape)
    print("\n🧾 Columns:", df.columns.tolist())
    print("\n🧹 Missing Values:\n", df.isnull().sum())

    print("\n📋 Label Counts:\n", df["label"].value_counts())
    print("\n📋 Bias Domain Counts:\n", df["bias_domain"].value_counts())
    print("\n📋 Explicit Type Counts:\n", df["explicit_type"].value_counts())

    df["word_count"] = df["text"].apply(lambda x: len(str(x).split()))
    print("\n📈 Word Count Stats:\n", df["word_count"].describe())

    print("\n📊 Label × Bias Domain:\n", pd.crosstab(df["label"], df["bias_domain"]))
    print("\n📊 Label × Explicit Type:\n", pd.crosstab(df["label"], df["explicit_type"]))

# Run
if __name__ == "__main__":
    csv_path = "/content/combined_bias_data_with_type_utf8BOM.csv"
    excel_path = "/content/extended_religious_bias_dataset_complete_merged_300.xlsx"
    df = load_and_merge_datasets(csv_path, excel_path)
    dashboard_eda(df)
