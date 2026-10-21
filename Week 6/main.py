from spotify import add_song, record_listen, generate_wrapped

def main_menu():
    while True:
        print("====== SPOTIFY WRAPPED ======")
        print("1. Add a song")
        print("2. Record a listen")
        print("3. Generate Spotify Wrapped")
        print("4. Exit")
        print("")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_song()

        elif choice == "2":
            record_listen()

        elif choice == "3":
            generate_wrapped()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


main_menu()
