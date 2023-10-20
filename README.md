
# Bryce's Totally Legit Game Store

## Description
This is a Flask web application that allows users to manage items in a Firebase database. Users can add, edit, or delete items, each containing a name, description, price, and an image. The images are stored and retrieved from Firebase Storage.

## Setup & Installation

1. **Clone the repository:** Clone the code repository to your local machine.
2. **Navigate to the project directory:** Open a terminal and navigate to the directory where the code is located.
3. **Install dependencies:** Ensure that Flask, firebase_admin, and werkzeug are installed. If not, you can install them using pip:
    ```bash
    pip install Flask firebase_admin werkzeug
    ```

4. **Run the application:** Start the Flask application by running the following command in the terminal:
    ```bash
    python app.py
    ```

5. **Access the application:** Open your web browser and navigate to `http://127.0.0.1:5000/` to access the application.

## Usage

- **Homepage:** The homepage displays all the items with their names, descriptions, prices, and images. You can also search and sort items on this page.
- **Add Item:** Click the 'Add Game' button, fill in the details, and submit the form to add a new item.
- **Edit Item:** Click the 'Edit' button next to an item, modify the details, and submit the form to update the item's information.
- **Delete Item:** Click the 'Delete' button next to an item to remove it from the database.

## Important Notes

- This application is intended for educational purposes and is to be accessed and used by authorized personnel only.
- Ensure that your Firebase credentials are correctly set up in a `serviceAccountKey.json` file.

## Author

Bryce McLeod
Have A Blessed Day
