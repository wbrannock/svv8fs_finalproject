"""Download constitution text files into the local data directory."""

from pathlib import Path

import requests


GITHUB_API_URL = "https://api.github.com/repos/marcomorucci/Clustering-Constitutions/contents/constitutions"
DATA_DIR = Path("data")


# Save .txt files in the data folder
def main() -> None:
    DATA_DIR.mkdir(exist_ok=True)

    response = requests.get(GITHUB_API_URL, timeout=30)
    response.raise_for_status()

    files = response.json()
    text_files = [file for file in files if file["name"].endswith(".txt")]

    for file in text_files:
        download_url = file["download_url"]
        output_path = DATA_DIR / file["name"]

        file_response = requests.get(download_url, timeout=30)
        file_response.raise_for_status()

        output_path.write_text(file_response.text, encoding="utf-8")
        print(f"Downloaded {output_path}")

    print(f"Downloaded {len(text_files)} text files to {DATA_DIR}/")


if __name__ == "__main__":
    main()
