
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?"

name = raw_input(prompt)
print "\nHello, %s!" % (name.title())
