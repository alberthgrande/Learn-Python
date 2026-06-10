class UserSession:
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.auth_token = token
        self.temp_counter = 0

session = UserSession(101, 'a1b2c3d4e5')

# List of attributes of remove dynamically before "saving"
attributes_to_clean = ['auth_token', 'temp_counter']

# Dynamically remove specified attributes
for attr in attributes_to_clean:
    if hasattr(session, attr):
        delattr(session, attr)
        print(f"Removed attributes: {attr}")

print("\nFinal attributes remaining:")

# Loop through the remaining attributes with dir()
for attr in dir(session):
    # Ignore dunder methods like __init__ or __str__ and regular methods
    if not attr.startswith("__") and not callable(getattr(session, attr)):
        print(f" - {attr}: {getattr(session, attr)}")
