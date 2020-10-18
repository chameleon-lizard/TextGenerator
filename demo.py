import text_gen

# Creating TextGenerator object
gen = text_gen.TextGenerator()

# While cycle with all of the demo logic
while True:
    selection = int(input("To get a random quote, enter 1. To see a poem, enter 2. To enter your text, enter 3. To end this suffering, enter 0.\n"))

    # Selection
    if selection == 0:
        break
    elif selection == 1:
        # Opening the file with quotes, reading them
        with open("text/quote.txt", 'r') as f:
            text = f.read()
        
        # Splitting the text into quotes
        quotes = text.split("\n")

        # Cycling through the quotes
        for i in quotes:
            # Printing the input
            print("Input: " + i)

            # Generating quote and printing it
            print("Output: " + gen.text(text = i, simplicity=0))

            # User's choice
            selection = int(input("1 to get another one, 0 to exit submenu.\n"))
            if selection == 0:
                break

        print("No more quotes")
    elif selection == 2:
        # Opening the file with the poem
        with open("text/poem.txt", 'r') as f:
            text = f.read()

        # User's choice
        selection = int(input("0 to get text from random words, 1 to get simple text, 2 to get standart text, 3 to get hard text.\n"))
        if selection == 0 or selection == 1 or selection == 2 or selection == 3:
            # Printing the poem
            print("Input:\n\n" + text)

            # Printing the generated result
            print("Output:\n\n" + gen.text(text = text, simplicity=selection))
    elif selection == 3:
        # Getting input from user
        text = input("Enter your text.\n")

        # Printing the generated result
        print("Output:\n\n" + gen.text(text = text, simplicity=selection))
    else:
        pass
