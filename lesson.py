import json

class Lesson:
    def __init__(self, date, subject, teacher, topic):
        self.date = date
        self.subject = subject
        self.teacher = teacher
        self.topic = topic

class SchoolTracker:
    def __init__(self):
        self.lessons = []

    def add_lesson(self, date, subject, teacher, topic):
        lesson = Lesson(date, subject, teacher, topic)
        self.lessons.append(lesson)
        print(f"Added lesson: {date}, {subject}, {teacher}, {topic}")

    def display_lessons(self):
        print("\nLesson Tracker:")
        for lesson in self.lessons:
            print(f"Date: {lesson.date}, Subject: {lesson.subject}, Teacher: {lesson.teacher}, Topic: {lesson.topic}")

    def save_to_file(self, filename="school_lessons.json"):
        data = [{"date": lesson.date, "subject": lesson.subject, "teacher": lesson.teacher, "topic": lesson.topic} for lesson in self.lessons]
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Lessons saved to {filename}")

if __name__ == "__main__":
    tracker = SchoolTracker()

    while True:
        print("\n1. Add Lesson\n2. Display Lessons\n3. Save to File\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            subject = input("Enter subject: ")
            teacher = input("Enter teacher's name: ")
            topic = input("Enter topic: ")
            tracker.add_lesson(date, subject, teacher, topic)
        elif choice == '2':
            tracker.display_lessons()
        elif choice == '3':
            tracker.save_to_file()
        elif choice == '4':
            break
        else:
            print("Invalid option, please try again.")
