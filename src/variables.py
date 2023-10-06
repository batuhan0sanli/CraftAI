class Variables(dict):
    instance = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = super(Variables, cls).__new__(cls)
        return cls.instance

    def set(self, key, value):
        self[key] = value

    def delete(self, key):
        del self[key]

    def __getattr__(self, item):
        return self[item]

    def __del__(self):
        self.clear()
