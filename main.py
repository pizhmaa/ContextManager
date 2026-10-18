class ContextManager:
    def __init__(self, file_name: str, mode: str):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        try:
            self.file = open(file=self.file_name, mode=self.mode)
            return self
        except ValueError as error:
            print(f'Ошибка: {error}')
            raise

    def __exit__(self, ext_type, ext_val, ext_tb):
        self.file.close()

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            with self:
                return func(*args, **kwargs)
        return wrapper

    def read(self):
        try:
            return self.file.read()
        except ValueError as error:
            print(f'Ошибка при чтение файла: {error}')
            raise

    def write(self, text: str):
        try:
            return self.file.write(text)
        except ValueError as error:
            print(f'Ошибка при записи в файл: {error}')
            raise

with ContextManager(file_name='test.txt', mode='w') as file:
    file.write('Something text')

with ContextManager(file_name='test.txt', mode='r') as file:
    print(file.read())













