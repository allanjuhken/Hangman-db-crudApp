from Controller_db import *

class CrudApp:
    def __init__(self):
        app = Controller_db()
        app.main()
        
if __name__ == '__main__':
    appcrud = CrudApp()