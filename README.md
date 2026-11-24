
# Digital Notice Board

A simple Python-based Digital Notice Board application for managing notices in schools, colleges, offices, and organizations.

## Features

- Add new notices.
- View all notices.
- Update existing notices.
- Delete notices.
- Search notices by title or content.
- Filter notices by category.
- View active notices.
- View expired notices.
- Set notice priority.
- Set notice expiry dates.
- Store notice records in JSON format.

## Technologies Used

- Python
- JSON
- File Handling
- Object-Oriented Programming
- Date and Time Module

## Project Structure

```text
Digital_Notice_Board/
│
├── main.py
├── notice_manager.py
├── storage.py
├── notices.json
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Digital_Notice_Board.git
```

### 2. Open the project folder

```bash
cd Digital_Notice_Board
```

### 3. Create a virtual environment (optional)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Run the application

```bash
python main.py
```

No external packages are required.

## How to Use

1. Run `main.py`.
2. Select Add Notice to create a notice.
3. Enter its title, content, category, priority, and expiry date.
4. Use View All Notices to display saved records.
5. Search or filter notices when required.
6. Update or delete notices using their IDs.
7. Check active and expired notices.

## Sample Notice

```text
Title: Practical Examination Notice
Content: Students must report at 10:00 AM.
Category: Exam
Priority: High
Expiry Date: 2026-12-15
```

## Learning Objectives

- Understand Python classes and objects.
- Work with JSON files.
- Perform CRUD operations.
- Use Python lists and dictionaries.
- Handle date validation.
- Organize code into multiple modules.

## Future Improvements

- Create a graphical user interface using Tkinter.
- Add administrator login.
- Add notice attachments.
- Export notices to PDF.
- Add email notifications.
- Build a web version using Django.

## Author

Python Developer

## License

This project is created for educational and learning purposes.
