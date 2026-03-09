class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def add_password(self, site, password):
        self.passwords[site] = password
        print("Password added!")

    def get_password(self, site):
        if site in self.passwords:
            print("Password:", self.passwords[site])
        else:
            print("Site not found")

pm = PasswordManager()

pm.add_password("gmail", "abc123")
pm.add_password("facebook", "pass456")

pm.get_password("gmail")