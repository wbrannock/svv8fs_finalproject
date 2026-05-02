# DS 5001 Final Project
## Completed by William Brannock (svv8fs)

This repository contains my DS 5001 final project on a corpus of national constitutions. The public GitHub repository contains the notebooks, scripts, figures, and project configuration. Large source and derived CSV files are stored separately in Box.

## Box Data Folder

I'm going to upload my raw csvs on this box folder:

https://virginia.app.box.com/s/rio0s3eodz1db3apmut2xqlq0418y0as
ping

## File Map

- `FinalProject.ipynb`: Main final project notebook with the written responses, links, and final figures.
- `Parsed_and_Annotated_Data_Simple_OHCO.ipynb`: Builds the parsed and annotated OHCO tables, aka `LIB`, `CORPUS`, `VOCAB`, and `DOC`.
- `Derived_Tables_Simple_OHCO.ipynb`: Builds the `BOW`, `DTM`, `TFIDF`, and Reduced L2 'TFIDF' tables.
- `PCA_Analysis.ipynb`: PCA analysis notebook
- `LDA_Analysis.ipynb`: LDA analysis notebook.
- `Word2Vec_Analysis.ipynb`: Word2Vec analysis notebook and related vocabulary/visualization outputs.
- `Sentiment_Analysis.ipynb`: Sentiment analysis notebook using the project sentiment lexicon inputs.
- `Riffs.ipynb`: Riffs for Final Project
- `scripts/download_constitutions.py`: Script used to download the constitution text files into the local `data/` folder.
- `iframe_figures/`: Figures and HTML visualizations referenced by the notebooks.
- `pyproject.toml`: Python project metadata and dependency list.
- `uv.lock`: Locked dependency versions for reproducible setup with `uv`.

