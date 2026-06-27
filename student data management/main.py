while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        import add_student

    elif choice == "2":
        import view_students

    elif choice == "3":
        import search_student

    elif choice == "4":
        import update_student

    elif choice == "5":
        import delete_student

    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice.")