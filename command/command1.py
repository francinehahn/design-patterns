class Installer:
    def __init__(self, source, destination):
        self.options = []
        self.destination = destination
        self.source = source
    
    def preferences(self, choice):
        self.options.append(choice)
        
    def execute(self):
        for option in self.options:
            if list(option.values())[0]:
                print(f'Copying the binary from {self.source} to {self.destination}')
            else:
                print('Operation completed.')

if __name__ == '__main__':
    installer = Installer('python3.9.1.gzip', '/usr/bin/')
    installer.preferences({'python': True})
    installer.preferences({'java': False})
    installer.execute()