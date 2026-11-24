from datetime import datetime
from storage import load_notices, save_notices


class NoticeManager:

    def __init__(self):
        self.notices = load_notices()

    def generate_id(self):
        if not self.notices:
            return 1

        return max(notice["id"] for notice in self.notices) + 1

    def add_notice(self, title, content, category, priority, expiry_date):
        notice = {
            "id": self.generate_id(),
            "title": title,
            "content": content,
            "category": category,
            "priority": priority,
            "created_at": datetime.now().strftime("%Y-%m-%d"),
            "expiry_date": expiry_date
        }

        self.notices.append(notice)
        save_notices(self.notices)

        print("\nNotice added successfully!")

    def display_notices(self, notices=None):
        if notices is None:
            notices = self.notices

        if not notices:
            print("\nNo notices found.")
            return

        for notice in notices:
            print("\n" + "-" * 45)
            print(f"ID       : {notice['id']}")
            print(f"Title    : {notice['title']}")
            print(f"Content  : {notice['content']}")
            print(f"Category : {notice['category']}")
            print(f"Priority : {notice['priority']}")
            print(f"Created  : {notice['created_at']}")
            print(f"Expires  : {notice['expiry_date']}")
            print(f"Status   : {self.get_status(notice)}")

    def get_status(self, notice):
        expiry = datetime.strptime(
            notice["expiry_date"], "%Y-%m-%d"
        ).date()

        if expiry < datetime.today().date():
            return "Expired"

        return "Active"

    def search_notice(self, keyword):
        results = [
            notice for notice in self.notices
            if keyword.lower() in notice["title"].lower()
            or keyword.lower() in notice["content"].lower()
        ]

        self.display_notices(results)

    def filter_category(self, category):
        results = [
            notice for notice in self.notices
            if notice["category"].lower() == category.lower()
        ]

        self.display_notices(results)

    def show_active_notices(self):
        results = [
            notice for notice in self.notices
            if self.get_status(notice) == "Active"
        ]

        self.display_notices(results)

    def show_expired_notices(self):
        results = [
            notice for notice in self.notices
            if self.get_status(notice) == "Expired"
        ]

        self.display_notices(results)

    def update_notice(self, notice_id):
        notice = self.find_notice(notice_id)

        if not notice:
            print("\nNotice not found.")
            return

        print("\nLeave a field empty to keep its current value.")

        title = input("New title: ").strip()
        content = input("New content: ").strip()
        category = input("New category: ").strip()
        priority = input("New priority (Low/Medium/High): ").strip()
        expiry = input("New expiry date (YYYY-MM-DD): ").strip()

        if title:
            notice["title"] = title

        if content:
            notice["content"] = content

        if category:
            notice["category"] = category

        if priority:
            if priority.lower() not in ["low", "medium", "high"]:
                print("Invalid priority. Keeping existing priority.")
            else:
                notice["priority"] = priority.capitalize()

        if expiry:
            try:
                datetime.strptime(expiry, "%Y-%m-%d")
                notice["expiry_date"] = expiry
            except ValueError:
                print("Invalid date. Keeping existing expiry date.")

        save_notices(self.notices)
        print("\nNotice updated successfully!")

    def delete_notice(self, notice_id):
        notice = self.find_notice(notice_id)

        if not notice:
            print("\nNotice not found.")
            return

        self.notices.remove(notice)
        save_notices(self.notices)

        print("\nNotice deleted successfully!")

    def find_notice(self, notice_id):
        for notice in self.notices:
            if notice["id"] == notice_id:
                return notice

        return None
