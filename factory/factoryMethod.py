from abc import ABC, abstractmethod

class Section(ABC):
    @abstractmethod
    def __repr__(self):
        pass

class PersonalSection(Section):
    def __repr__(self):
        return 'Personal Section'
    
class AlbumSection(Section):
    def __repr__(self):
        return 'Album Section'
    
class ProjectSection(Section):
    def __repr__(self):
        return 'Project Section'
    
class PublicationSection(Section):
    def __repr__(self):
        return 'Publication Section'
    
class Profile(ABC):
    def __init__(self):
        self.sections = []
        self.create_profile()
    
    @abstractmethod
    def create_profile(self):
        pass
    
    def get_sections(self):
        return self.sections
    
    def add_section(self, section:Section):
        self.sections.append(section)
        
class Linkedin(Profile):
    def create_profile(self):
        self.add_section(PersonalSection())
        self.add_section(ProjectSection())
        self.add_section(PublicationSection())

class Facebook(Profile):
    def create_profile(self):
        self.add_section(PersonalSection())
        self.add_section(AlbumSection())
        
if __name__ == '__main__':
    social_media = input('Which social media would you like to create an account on? [Linkedin, Facebook] ')
    account = eval(social_media)()
    print(f'Creating an account on {type(account).__name__}')
    print(f'The account has the following sections: {account.get_sections()}')