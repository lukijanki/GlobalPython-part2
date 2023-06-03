import json
from typing import List, Dict
from datetime import datetime

class TaskManager:
    def __init__(self):
        self._tasks: List[Dict[str, str]] = []
    
    def validate_day(self, prompt: str) -> str:
        """
        Walidacja dnia tygodnia.
        """
        valid_days: List[str] = [
            "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"
        ]
        while True:
            day_of_week: str = input(prompt)
            if not day_of_week:
                return "" 
            elif day_of_week.lower() in valid_days:
                return day_of_week.lower()
            else:
                print("Niepoprawny dzień tygodnia. Spróbuj ponownie.")

    def add_task(self) -> None:
        """
        Dodawanie nowe zadanie do listy.
        """
        title: str = input("Podaj nazwę zadania:")
        description: str = input("Podaj opis zadania: ")
        while True:
            deadline: str = input("Podaj deadline: (YYYY-MM-DD): ")
            try:
                datetime.strptime(deadline, "%Y-%m-%d")
                break
            except ValueError:
                print("Niepoprawny format daty. Spróbuj ponownie.")
        day_of_week: str = self.validate_day("Podaj dzień tygodnia po angielsku: Zostaw puste jeżeli bez dnia tygodnia!")
        task_ids = [int(task["id"]) for task in self._tasks]
        if task_ids:
            max_id = max(task_ids)
            available_ids = [i for i in range(1, max_id + 2) if i not in task_ids]
            task_id = min(available_ids)
        else:
            task_id = 1
        
        task: Dict[str, str] = {"id": str(task_id), "title": title, "description": description, "deadline": deadline, "day_of_week": day_of_week}
        self._tasks.append(task)
        print("Zadanie dodane!")
        
    def display_tasks(self) -> None:
        """
        Wyświetlanie zadania.
        """
        if not self._tasks:
            print("Brak zadań do wyświetlenia.")
            return
        day_of_week: str = self.validate_day("Wprowadź dzień tygodnia, aby wyświetlić zadania (zostaw puste, aby wyświetlić wszystkie zadania): ")
        found_tasks: bool = False
        for task in self._tasks:
            if not day_of_week or task['day_of_week'].lower() == day_of_week.lower():
                print(f"ID:{task['id']} Nazwa: {task['title']} (Deadline: {task['deadline']})")
                show_description: str = input("Czy chcesz zobaczyć opis? (t/n): ")
                if show_description.lower() == 't':
                    print(f"Opis: {task['description']}")
                found_tasks = True
        if not found_tasks:
            print(f"Brak zadań dla {day_of_week}.")

    def display_tasks_onenter(self) -> None:
        """
        Wyswietlanie zadania przy uruchomieniu.
        """
        self.load_tasks()
        if not self._tasks:
            print("Brak zadań do wyświetlenia.")
            return
        found_tasks: bool = False
        for task in self._tasks:
                print(f"ID:{task['id']} Nazwa: {task['title']} (Deadline: {task['deadline']})")
                show_description: str = input("Czy chcesz zobaczyć opis? (t/n): ")
                if show_description.lower() == 't':
                    print(f"Opis: {task['description']}")
                found_tasks = True
        

    def delete_task(self) -> None:
        """
        Usuwawanie zadania..
        """
        task_id: int = int(input("Podaj ID zadania: "))
        for task in self._tasks:
            if task['id'] == str(task_id):
                self._tasks.remove(task)
                print("Zadanie usunięte pomyślnie.")
                return
        print("Zadanie nie znalezione.")

    def update_task(self) -> None:
        """
        Aktualizowanie zadania.
        """
        task_id: int = int(input("Podaj ID zadania: "))
        for task in self._tasks:
            if task['id'] == str(task_id):
                title: str = input("Podaj nową nazwę (pozostaw puste, aby zachować starą): ")
                description: str = input("Podaj nowy opis (pozostaw puste, aby zachować stary): ")
                deadline: str = input("Podaj nowy deadline (pozostaw puste, aby zachować stary): ")
                day_of_week: str = input("Podaj nowy dzień tygodnia (pozostaw puste, aby zachować stary): ")
                if title:
                    task['title'] = title
                if description:
                    task['description'] = description
                if deadline:
                    task['deadline'] = deadline
                if day_of_week:
                    task['day_of_week'] = day_of_week
                print("Zadanie zaktualizowane pomyślnie.")
                return
        print("Zadanie nie znalezione.")

    def save_tasks(self) -> None:
        """
        Zapisywanie zadania.
        """
        with open("tasks.json", "w") as f:
            json.dump(self._tasks, f)
        print("Zadania zapisane do pliku.")

    def load_tasks(self) -> None:
        """
        Odczyt zadania.
        """
        try:
            with open("tasks.json", "r") as f:
                self._tasks = json.load(f)
        except FileNotFoundError:
            pass

    def get_tasks(self) -> List[Dict[str, str]]:
        """
        Lista zadań.
        """
        return self._tasks

    def menu(self) -> None:
        """
        Wyświetlanie menu.
        """
        print("""
        1. Dodaj zadanie
        2. Wyświetl zadania
        3. Usuń zadanie
        4. Zaktualizuj zadanie
        5. Zapisz zadania
        6. Wyjście
        """)

    def run(self) -> None:
        """
        Pętla programu.
        """
        self.load_tasks()

        while True:
            self.menu()
            choice: str = input("Wybierz opcję: ")
            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.display_tasks()
            elif choice == '3':
                self.delete_task()
            elif choice == '4':
                self.update_task()
            elif choice == '5':
                self.save_tasks()
            elif choice == '6':
                self.save_tasks()
                print("Do widzenia!")
                break
            else:
                print("Niepoprawny wybór, wybierz opcje od 1 do 6!")

task_manager = TaskManager()
task_manager.display_tasks_onenter()
task_manager.run()