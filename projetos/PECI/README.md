# Data Standardization and Entity Resolution for Port Logistics Records

https://github.com/user-attachments/assets/4af17b18-dea2-4252-b253-a41047bacbf1

---

## 📌 Project Overview        
This project was developed **from scratch as a complete software system**,
as the final capstone project of the Computer and Informatics Engineering degree
at the University of Aveiro, in collaboration with the Port of Sines under the
NEXUS program for sustainable digital innovation in logistics.

Over one academic year, the team designed, implemented, and tested a full data
processing application in Python, capable of handling millions of records.
The main challenge was to standardize and reconcile company records across
heterogeneous datasets, each containing:
- ~60 columns
- ~4 million rows

The focus was on the `Identification_number` and `name` fields, which contained
duplicates, typos, and inconsistent formatting caused by manual data entry.

This was an open-ended research and development problem, with no predefined solution.
The team applied the Agile OpenUP methodology, working through four iterative
phases over one academic year.

---

## 🎯 Objectives
- Design and implement an application capable of correcting and standardizing
  large-scale datasets.
- Automatically detect and merge duplicates (including those caused by typos).
- Separate sub-entities by country-specific prefixes (e.g., “Company1 PT” vs “Company1 BR”).
- Deliver a scalable software solution with a user-friendly interface.

--- 

## 🏗️ System Architecture

1. Ground Truth Creation
   - Built from standardized company IDs (NIFs)
   - Used as reference to evaluate clustering precision
2. Preprocessing
   - Convert names to lowercase
   - Remove punctuation and special characters
   - Strip legal suffixes/prefixes (e.g., “Lda.”, “S.A.”)
3. Vectorization
   - Generate multi-dimensional embeddings for each company name
4. Clustering
   - Group similar names together (typos, handwritten variations, etc.)
5. Post-Processing
   - Refine clusters using Jaccard similarity and Levenshtein distance
   - Prevents unrelated companies with common words from being merged
6. Country Prefix Separation
   - Subdivide clusters by country identifiers (e.g., PT, BR, ES)
7. Canonical Name Assignment
   - Select a central representative name for each cluster
   - Update and correct the dataset accordingly

---

## 🖥️ Implementation
- Language: Python
- Initial Prototype:
  - Pandas + MinHash (~1h30 runtime, not scalable)
- Final System:
  - Pandas + Sentence Transformers for embeddings
  - FAISS for fast indexing & clustering
  - Processing time: ~20 minutes on a laptop
  - F1-score: ~80% (balanced precision and recall)
- User Interface:
  - Text-based User Interface (TUI) with live execution status

---

## 📊 Evaluation
- Metrics:
  - Intra-cluster cohesion & inter-cluster separation (Calinski-Harabasz inspired)
  - Adjusted Rand Index (ARI) and F1-score against the ground truth
- Results:
  - ~80% F1-score
  - Runtime improvement:
    - MinHash → 1h30
    - ST + FAISS → ~20 min

---

## 👥 Stakeholders & Roles
- Stakeholders:
  - Project team (developers)
  - University supervisor (Prof. Luís Seabra Lopes)
  - APS – Administração dos Portos de Sines e do Algarve, S.A.
- My Role:
  - Project leader and primary contributor
  - Designed the final architecture and algorithms
  - Implemented the TUI system
  - Presented results to Port of Sines professionals

## 🚀 Key Learnings
- Full-cycle software development: from problem analysis to deployment
- Applied Agile OpenUP methodology in a real-world industrial context
- Gained practical experience in data cleansing, clustering, embeddings,
  and large-scale entity resolution
- Balanced automation with manual oversight (via JSON correction dictionary
  and ground truth)
- Strengthened leadership, teamwork, and problem-solving skills

## 🔧 Tech Stack
- Python
- Pandas – data processing
- Sentence Transformers – semantic embeddings
- FAISS – similarity search & clustering
- JSON dictionary – incremental corrections
- TUI framework – interactive interface

<!-- ## 📂 Suggested Repository Structure
├──  
├── data/              # Sample/anonymized datasets
├── src/               # Source code
│   ├── preprocessing/ # Cleaning functions
│   ├── vectorization/ # Sentence Transformers
│   ├── clustering/    # FAISS + post-processing
│   ├── evaluation/    # Metrics and F1-score analysis
│   ├── tui/           # Text-based user interface
│   └── utils/         # Helper scripts
├── README.md          # Project documentation
└── requirements.txt   # Python dependencies -->

## 📢 Acknowledgments
- University of Aveiro – academic support
- APS – Port of Sines – real-world datasets and collaboration
- Open-source community – libraries and frameworks

<!-- # Folder with the final code

## How to run the code?

**NOTE:** This instructions presuppose that you will be using bash.

**1. Get inside the **src/** folder**

**2. Create a virtual enviroment and run it.**
  - How to create a virtual enviroment? Use the following command:
    ```bash
    python3 -m venv venv
    ```

  - How to run the virtual enviroment created? Use the following command:
    ```bash
    source venv/bin/activate
    ```

**3. Install the necessary dependencies using the command:**
```bash 
pip install -r requirements.txt
```

**4. After having the enviroment setuped, you can try the program with the command:**
```bash
python3 main.py
```

## Project Notes

- **The Ground Truth Synonym Map has the following format**

```json
{
  Name_variant: {
    Standard_name: [
      [
        Identification_number
      ]
    ] 
  },
  ...
  Name_variant_n: {
    Standard_name_n: [
      [
        Identification_number_n
      ]
    ] 
  }
}
```

- Possible question: Why is the **Name_variant** value a dictionary and the **Standard_name** value a list of lists?
  1. Because a given **Name_variant** might have multiple **Standard_names** associated with it. In that case, it must be choosen one manually.
  2. Because a given **Standard_name** might be connected to multiple **Identification_numbers**

  **NOTE: All this problems stem from the standard table being wrong. A lot is corrected automatically, but what isn't must be alerted to the user to be manually corrected.**      


- **The Final Version Synonym Map has the following format**
```json
{
  Name_variant1: Standard_name1,
  Name_variant2: Standard_name2,
  ...
  Name_variantN: Standard_nameN
}
``` -->
