#!/usr/bin/env python3
"""
Simple Todo List Manager
Save todos to todos.txt and manage them with an easy menu interface
"""

import os


TODO_FILE = "todos.txt"


def load_todos():
    """Load todos from file"""
    if not os.path.exists(TODO_FILE):
        return []

    todos = []
    with open(TODO_FILE, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                # Format: [X] or [ ] followed by the todo text
                if line.startswith('[X]'):
                    todos.append({'text': line[4:], 'completed': True})
                elif line.startswith('[ ]'):
                    todos.append({'text': line[4:], 'completed': False})
    return todos


def save_todos(todos):
    """Save todos to file"""
    with open(TODO_FILE, 'w') as f:
        for todo in todos:
            status = '[X]' if todo['completed'] else '[ ]'
            f.write(f"{status} {todo['text']}\n")


def show_todos(todos):
    """Display all todos"""
    print("\n" + "=" * 50)
    print("YOUR TODO LIST")
    print("=" * 50)

    if not todos:
        print("\nNo todos yet! Add one to get started.")
    else:
        for i, todo in enumerate(todos, 1):
            status = "✓" if todo['completed'] else " "
            text = todo['text']
            if todo['completed']:
                print(f"{i}. [{status}] {text} (completed)")
            else:
                print(f"{i}. [{status}] {text}")

    print("=" * 50)


def add_todo(todos):
    """Add a new todo"""
    print("\n" + "-" * 50)
    text = input("What do you need to do? ").strip()

    if text:
        todos.append({'text': text, 'completed': False})
        save_todos(todos)
        print(f"✓ Added: {text}")
    else:
        print("Can't add an empty todo!")


def complete_todo(todos):
    """Mark a todo as complete"""
    if not todos:
        print("\nNo todos to complete!")
        return

    show_todos(todos)
    print("\n" + "-" * 50)

    try:
        num = int(input("Which todo did you complete? (enter number): "))
        if 1 <= num <= len(todos):
            todo = todos[num - 1]
            if todo['completed']:
                print(f"\n'{todo['text']}' is already completed!")
            else:
                todo['completed'] = True
                save_todos(todos)
                print(f"\n✓ Completed: {todo['text']}")
        else:
            print("\nInvalid number!")
    except ValueError:
        print("\nPlease enter a valid number!")


def delete_todo(todos):
    """Delete a todo"""
    if not todos:
        print("\nNo todos to delete!")
        return

    show_todos(todos)
    print("\n" + "-" * 50)

    try:
        num = int(input("Which todo do you want to delete? (enter number): "))
        if 1 <= num <= len(todos):
            deleted = todos.pop(num - 1)
            save_todos(todos)
            print(f"\n✗ Deleted: {deleted['text']}")
        else:
            print("\nInvalid number!")
    except ValueError:
        print("\nPlease enter a valid number!")


def show_menu():
    """Display the main menu"""
    print("\n" + "=" * 50)
    print("MENU")
    print("=" * 50)
    print("1. View todos")
    print("2. Add todo")
    print("3. Complete todo")
    print("4. Delete todo")
    print("5. Exit")
    print("=" * 50)


def main():
    """Main program loop"""
    print("\n" + "=" * 50)
    print("📝 TODO LIST MANAGER")
    print("=" * 50)

    todos = load_todos()

    while True:
        show_menu()
        choice = input("\nWhat would you like to do? (1-5): ").strip()

        if choice == '1':
            show_todos(todos)
        elif choice == '2':
            add_todo(todos)
        elif choice == '3':
            complete_todo(todos)
        elif choice == '4':
            delete_todo(todos)
        elif choice == '5':
            print("\n" + "=" * 50)
            print("Thanks for using Todo List Manager!")
            print("Your todos are saved in todos.txt")
            print("=" * 50 + "\n")
            break
        else:
            print("\nInvalid choice! Please enter 1-5.")


if __name__ == "__main__":
    main()
