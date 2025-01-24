class ApplicationContext:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ApplicationContext, cls).__new__(cls, *args, **kwargs)
            cls._instance.main_window = None
        return cls._instance

    def set_main_window(self, main_window):
        self.main_window = main_window

    def get_main_window(self):
        if not self.main_window:
            raise ValueError("Main window has not been set yet!")
        return self.main_window
