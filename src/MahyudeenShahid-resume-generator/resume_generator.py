from faker import Faker
from tqdm import tqdm
import random
import string

class fakeResumeGenerator:


    def __init__(self, name: str, education: dict, experience: dict, kwargs: dict):

        self.name = name
        self.education = education
        self.experience = experience
        self.kwargs = kwargs


    def generateResume(self) -> str:

        lang = ', '.join(self.kwargs['languages'])
        frameworks = ', '.join(self.kwargs['frameworks'])
        databases = self.kwargs['databases']
        tools = ', '.join(self.kwargs['tools'])

        companies = list(self.experience.keys())
        companies.pop(0)
        # {comapany: [duration, title, address]}

        degrees = list(self.education.keys())
        # {degree: [university, address, graduation year]}

        content = f"""
{self.name.upper()}

Phone Number: {self.kwargs['phone']}
Email Address: {self.kwargs['email']}
LinkedIn Profile: {self.kwargs['linkedin']}
GitHub Portfolio: {self.kwargs['github']}

Professional Summary

Detail-oriented and results-driven Software Engineer with {self.experience['years']} years of experience in
developing, designing and maintaining software applications. Skilled in [{lang.rstrip(', ')}] and 
experienced with frameworks such as [{frameworks.rstrip(', ')}]. Passionate about solving complex problems
and building scalable, efficient systems.

Technical Skills

Languages: [{lang.rstrip(', ')}]
Frameworks/Libraries: [{frameworks.rstrip(', ')}]
Databases: [{databases.rstrip(', ')}]
Tools: [{tools.rstrip(', ')}]

Professional Experience

{self.experience.get(companies[0])[0]} -- {companies[0]}
{self.experience.get(companies[0])[1]} | {random.randint(3, 10)} years

Education

{degrees[0]} -- {self.education.get(degrees[0])[0]}
{self.education.get(degrees[0])[1]} | {random.randint(2005, 2024)}

"""
        
        return content
    

def selectRandomData() -> dict:

        characters = string.ascii_lowercase + string.digits

        companies_pool = ["IBM", "Intel", "AWS", "TCS", "Infosys", "AMD", "Microsoft", "Google", "Apple", "Philips", "Samsung", "Flipkart"]
        degrees_pool = ["B. Tech in Computer Science", "B. Sc in Computer Science", "M. Tech in Computer Science", "M. Tech in Computer Science"]
        languages_pool = ["Python", "Java", "JavaScript", "TypeScript", "XML", "HTML", "CSS", "C", "C++", "Rust", "C#", "Swift"]
        databases_pool = ["MySQL", "PostgreSQL", "MongoDB", "NoSQL"]
        tools_pool = ["Git", "Docker", "Replit", "Copilot", "npm"]
        frameworks_pool = ["React", "Vue", "Node", "Flask", "Django", "FastAPI", "Angular"]
        universities_pool = ["University of California", "Indian Institute of Technology", "University of Melbourne", "University of Munich", "National Institute of Technology"]
        country_domains_pool = ["in", "us", 'uk', "au", "ca", "ge"]
        company_addr_pool = ["Bengaluru, India", "Sydney, Australia", "Florida, USA", "London, UK", "Stockholm, Sweden"]

        fake = Faker()

        name = fake.name()
        name_2 = '-'.join(name.split())
        name_3 = ''.join(name.split())

        random_country_domain = random.choice(country_domains_pool)
        random_code = ''.join(random.sample(characters, 7))

        github_portfolio = f"https://github.com/{name_3.capitalize()}/{name_3}.github.io"
        linkedin_profile = f"www.linkedin.com/{random_country_domain}/{name_2.lower()}/{random_code}"
        phone = random.randint(6238451269, 9985426781)
        email = name_3 + "@" + random.choice(["gmail", "yahoo", "redditmail"]) + ".com"

        companies = list(random.choices(companies_pool, k=2))
        degrees = random.choice(degrees_pool)
        languages = list(set(random.choices(languages_pool, k=3)))
        databases = random.choice(databases_pool)
        tools = list(set(random.choices(tools_pool, k=3)))
        frameworks = list(set(random.choices(frameworks_pool, k=3)))
        universities = list(random.choices(universities_pool, k=2))

        cities = []
        for u in universities:
            if u == "Indian Institute of Technology":
                cities.append('Kharagpur, India')
            elif u == "National Institute of Technology":
                cities.append('Warangal, India')
            elif u == "University of Melbourne":
                cities.append('Melbourne, Australia')
            elif u == "University of California":
                cities.append('Berkeley, USA')
            elif u == "University of Munich":
                cities.append('Munich, Germany')

        fake_profile = {}

        experience = {}
        education = {}

        experience['years'] = random.randint(4, 12)
        for i in range(2):
            
            company_addr = random.choice(company_addr_pool)
            experience[companies[i]] = [random.choice(["Junior Developer", "Senior Developer"]), company_addr]

        education[degrees] = [universities[0], cities[0]]

        others = {}
        others['languages'] = languages
        others['databases'] = databases
        others['frameworks'] = frameworks
        others['tools'] = tools
        others['github'] = github_portfolio
        others['linkedin'] = linkedin_profile
        others['phone'] = phone
        others['email'] = email

        fake_profile['name'] = name
        fake_profile['education'] = education
        fake_profile['experience'] = experience
        fake_profile['others'] = others

        return fake_profile
    

if __name__ == "__main__":
        
    count = int(input("Enter number of sample resumes to generate: "))
    for i in tqdm(range(count)):

        profile = selectRandomData()
        gen = fakeResumeGenerator(profile.get('name'), profile.get('education'), profile.get('experience'), 
                                profile.get('others'))
        
        resume = gen.generateResume()
    
        path = f"D:\\Programs\\Hackathon\\parallel-recruition-system\\sample-data\\applicant-{i + 1}.txt"
        with open(path, 'w') as file:
            file.write(resume)

    print(f"Successfully created {count} resumes!")
