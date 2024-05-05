from abc import ABC, abstractmethod

#other hooks can be added if necessary

class Compiler(ABC):
    @abstractmethod
    def get_source_code(self):
        pass
    
    @abstractmethod
    def compile_object(self):
        pass
    
    @abstractmethod
    def execute(self):
        pass
    
    # template method - hook
    def compile_and_execute(self):
        self.get_source_code()
        self.compile_object()
        self.execute()
        
class IOSCompiler(Compiler):
    def get_source_code(self):
        print('Getting Swift source code...')
        
    def compile_object(self):
        print('Compiling Swift source code to LLVM bytecode')
        
    def execute(self):
        print('Executing program...')
        
class AndroidCompiler(Compiler):
    def get_source_code(self):
        print('Getting Kotlin source code...')
        
    def compile_object(self):
        print('Compiling Kotlin source code to JVM bytecode')
        
    def execute(self):
        print('Executing program...')
        
ios = IOSCompiler()
ios.compile_and_execute()
android = AndroidCompiler()
android.compile_and_execute()