import sqlite3


# Base class using encapsulation
class Database:
    def __init__(self, db_name):
        self._db_name = db_name  # Encapsulated attribute

    def _connect(self):
        return sqlite3.connect(self._db_name)


# Inheriting from Database
class InquiryHandler(Database):
    def save_inquiry(self, name, email, message):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO inquiries (name, email, message) VALUES (?, ?, ?)",
                       (name, email, message))
        conn.commit()
        conn.close()
        print("✅ Your inquiry has been saved.")


# Main logic to run from command line
def main():
    print("=== Retail Shop Inquiry Form ===")
    name = input("Enter your name: ").strip()
    email = input("Enter your email: ").strip()
    message = input("Enter your message: ").strip()

    if not name or not email or not message:
        print("⚠️  All fields are required!")
        return

    handler = InquiryHandler('retailshop.db')
    handler.save_inquiry(name, email, message)


if __name__ == '__main__':
    main()
