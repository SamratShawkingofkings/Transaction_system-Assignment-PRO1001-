cat > README.md <<EOF
# Office Transactions Management System

A simple web application to manage daily office cash transactions including credit and debit entries, with a running balance calculation. Built with Python Flask for the backend and HTML/CSS for the frontend.

## Features

- Add new transactions with date, description, credit, and debit amounts.
- Display all transactions in a table with running balance.
- Clean and user-friendly interface.
- Button to add new transactions positioned on the right side.

## Technologies Used

- Python 3
- Flask web framework
- HTML5 & CSS3

## Getting Started

### Prerequisites

- Python 3 installed on your system
- \`pip\` package manager

### Installation and Setup

1. **Clone the repository**

   \`\`\`bash
   git clone https://github.com/your-username/office-transactions.git
   cd office-transactions
   \`\`\`

2. **Create and activate a virtual environment (optional but recommended)**

   - On Linux/macOS:

     \`\`\`bash
     python3 -m venv venv
     source venv/bin/activate
     \`\`\`

   - On Windows:

     \`\`\`bash
     python -m venv venv
     venv\Scripts\activate
     \`\`\`

3. **Install required dependencies**

   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Run the Flask application**

   \`\`\`bash
   flask run
   \`\`\`

5. **Access the app**

   Open your web browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Project Structure

\`\`\`
Assignment/
│
├── app.py                 # Main Flask application file
├── templates/
│   └── index.html         # Main HTML page for transactions
├── static/
│   └── style.css          # CSS stylesheet
├── requirements.txt       # Python dependencies
└── README.md              # This documentation file
\`\`\`

## Usage

- Click the **+ Add Transaction** button located at the top-right of the page to add a new transaction.
- Fill in the transaction details and submit.
- The transaction list will update with the new entry, showing the running balance.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with improvements or bug fixes.

## License

This project is licensed under the MIT License.

EOF
