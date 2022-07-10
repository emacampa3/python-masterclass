# function
def banner_text(text):
  screen_width = int(banner_width)
  if len(text) > screen_width - 4:
    # crashes the program when text is too long
    raise ValueError(
        "String {0} is larger than specified width {1}".format(text, screen_width))

  if text == "*":
    print("*" * screen_width)
  else:
    centered_text = text.center(screen_width - 4)
    output_string = "**{0}**".format(centered_text)
    print(output_string)


banner_width = input("Enter a banner width: ")
banner_text("*")
banner_text("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
banner_text("Maecenas ornare lacus lacus, vitae luctus enim ultricies auctor.")
banner_text("Ut eget sollicitudin nunc, quis mattis est. Morbi.")
banner_text("*")


# function
def banner_text(text, screen_width=80): # default value added
  if len(text) > screen_width - 4:
    # crashes the program when text is too long
    raise ValueError(
        "String {0} is larger than specified width {1}".format(text, screen_width))

  if text == "*":
    print("*" * screen_width)
  else:
    centered_text = text.center(screen_width - 4)
    output_string = "**{0}**".format(centered_text)
    print(output_string)


banner_text("*")
banner_text("Lorem ipsum dolor sit amet, consectetur adipiscing elit.") 
banner_text("Maecenas ornare lacus lacus, vitae luctus enim ultricies auctor.")
# overriding the default value of 80
banner_text("Ut eget sollicitudin nunc, quis mattis est. Morbi.", 50)
banner_text("*")
