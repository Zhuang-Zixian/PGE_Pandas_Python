# PGE_Pandas_Python
This project utilizes the Python Pandas library for data analysis.

# Images
![Screenshot 2022-08-25 233805](https://github.com/Zhuang-Zixian/PGE_Pandas_Python/assets/61621372/6eb04326-9901-4e15-963e-eccfe9a77d6b)
![Unittest SC](https://github.com/Zhuang-Zixian/PGE_Pandas_Python/assets/61621372/0362570c-b1c5-4aff-8a18-bbb78d442b46)

# Visitor Trend Analysis

This project aims to analyze traveller trends by identifying the top 3 countries of visitors to Singapore from a specific region over 10 years. Python is the primary language used for data analysis, with Pandas serving as the key library for data manipulation.

## Project Structure

```
.
├── data
│   └── Int_Monthly_Visitor.csv
├── utils.py
├── main.py
├── tests
│   └── unit_test.py
├── README.md
└── requirements.txt
```

- `data/Int_Monthly_Visitor.csv`: Dataset containing monthly visitor numbers.
- `utils.py`: Contains the `VisitorsAnalyticsUtils` class for data loading, parsing, and analysis.
- `main.py`: Main script for running the application, which prompts user inputs and displays results.
- `tests/unit_test.py`: Unit tests for utility functions.
- `requirements.txt`: Dependencies required for the project.

## Setup Instructions

### Prerequisites

- Python 3.0 or higher
- Pandas library

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/visitor-trend-analysis.git
cd visitor-trend-analysis
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Ensure that the dataset `Int_Monthly_Visitor.csv` is placed in the `data` directory.

## Usage

To run the application, execute the `main.py` script:

```bash
python main.py
```

You will be prompted to enter the region and the year period for analysis. The script will then display the parsed data and the top 3 countries of visitors for the selected region and period.

## Running Tests

To run the unit tests, execute the following command:

```bash
python -m unittest tests/unit_test.py
```

This will run the test cases defined in `unit_test.py` to ensure the functionality of the data loading and parsing methods.
