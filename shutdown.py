def shutdown():
    user_input = input("Do you want to shut down? (Yes/No): ").strip().lower()
    
    if user_input == "yes":
        print("Shutting down...")
    elif user_input == "no":
        print("Shutdown aborted.")
    else:
        print("Sorry, invalid input.")
        
shutdown()