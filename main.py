from datetime import datetime
from notice_manager import NoticeManager


manager = NoticeManager()


def get_expiry_date():
    while True:
        expiry = input("Expiry date (YYYY-MM-DD): ").strip()

        try:
            datetime.strptime(expiry, "%Y-%m-%d")
            return expiry
        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD.")


def add_notice():
    print("\n--- ADD NEW NOTICE ---")

    title = input("Notice title: ").strip()
    content = input("Notice content: ").strip()
    category = input("Category (Academic/Event/General/Exam): ").strip()

    if not title or not content or not category:
        print("\nTitle, content, and category are required.")
        return

    while True:
        priority = input("Priority (Low/Medium/High): ").strip().capitalize()

        if priority in ["Low", "Medium", "High"]:
            break

        print("Please enter Low, Medium, or High.")

    expiry_date = get_expiry_date()

    manager.add_notice(
        title,
        content,
        category,
        priority,
        expiry_date
    )


def get_notice_id():
    try:
        return int(input("Enter notice ID: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return None


def menu():
    while True:
        print("\n" + "=" * 45)
        print("          DIGITAL NOTICE BOARD")
        print("=" * 45)

        print("1. Add Notice")
        print("2. View All Notices")
        print("3. Search Notice")
        print("4. Filter by Category")
        print("5. View Active Notices")
        print("6. View Expired Notices")
        print("7. Update Notice")
        print("8. Delete Notice")
        print("9. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_notice()

        elif choice == "2":
            manager.display_notices()

        elif choice == "3":
            keyword = input("Enter search keyword: ").strip()

            if keyword:
                manager.search_notice(keyword)
            else:
                print("Please enter a search keyword.")

        elif choice == "4":
            category = input("Enter category: ").strip()

            if category:
                manager.filter_category(category)
            else:
                print("Please enter a category.")

        elif choice == "5":
            manager.show_active_notices()

        elif choice == "6":
            manager.show_expired_notices()

        elif choice == "7":
            notice_id = get_notice_id()

            if notice_id is not None:
                manager.update_notice(notice_id)

        elif choice == "8":
            notice_id = get_notice_id()

            if notice_id is not None:
                manager.delete_notice(notice_id)

        elif choice == "9":
            print("\nThank you for using Digital Notice Board!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    menu()
