class User:
    # name of the parameters in the constructor not necessary match const vars name as example user_email
    def __init__(self, email, name, password, current_job_title):
        self.current_job_title = current_job_title
        self.password = password
        self.email = email
        self.name = name

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name} currently works as a {self.current_job_title}. you can contact them at {self.email}")



