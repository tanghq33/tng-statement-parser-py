# tng-statement-parser-py

[![License](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/downloads/)

TNG Statement Parser is a Python library designed to help you parse e-wallet statements issued by TNG eWallet. It provides a simple and efficient way to extract transaction data from PDF statements.

## Installation

You can install `tngparser` using `pip`, the Python package manager. Open your terminal or command prompt and run the following command:

```bash
pip install tngparser
```

## Usage

Here's how you can use tngparser to parse a TNG eWallet PDF statement:

```python
import tngparser

# Replace the path with your actual PDF file path
pdf_path = "/path/to/pdf"

# Parse the PDF statement
df = tngparser.parse_pdf(pdf_path)

# Now `df` is a Pandas DataFrame containing the parsed transaction data
print(df)
```

## License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! If you find a bug or want to suggest an improvement, please open an issue or submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## Contact
If you have any questions or need further assistance, feel free to contact the project owner at tanghq33@outlook.com.