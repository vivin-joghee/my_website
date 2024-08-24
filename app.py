from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Configuring the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resume2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initializing the database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define models
class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    start_date = db.Column(db.String(50), nullable=False)
    end_date = db.Column(db.String(50), nullable=True)

class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    degree = db.Column(db.String(100), nullable=False)
    institution = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    start_date = db.Column(db.String(50), nullable=False)
    end_date = db.Column(db.String(50), nullable=True)

class Certification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    issuing_organization = db.Column(db.String(100), nullable=False)
    issue_date = db.Column(db.String(50), nullable=False)

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Award(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    organization = db.Column(db.String(100), nullable=False)
    year = db.Column(db.String(50), nullable=False)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resume')
def resume():
    experiences = Experience.query.all()
    educations = Education.query.all()
    certifications = Certification.query.all()
    skills = Skill.query.all()
    awards = Award.query.all()
    return render_template('resume.html', experiences=experiences, educations=educations, certifications=certifications, skills=skills, awards=awards)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # Add some sample data to the database (only if no data exists)
        if not Experience.query.first():
            experience1 = Experience(
                title="SENIOR FINANCIAL SERVICES INDUSTRY CONSULTANT",
                company="Swift Terminal Services",
                description='''1. AMH ISO20022 Migration – MEPS L4L, TH Bahtnet, ZA Samos, CBPR+, AU HVPS, PH Phil Pass, JO RTGS, BN RTGS and ISO Accelerated Pack for other Market Infrastructures
                               2. Dev Lead for Continuous Integration - AMH Docker image maintenance / Server provisioning using Ansible scripts / Cloudbess jobs configuration''',
                start_date="Dec 2021",
                end_date="Present"
            )
            db.session.add(experience1)

        if not Education.query.first():
            education1 = Education(
                degree="Bachelor of Science in Computer Science",
                institution="University of Technology",
                description="Studied computer science, focusing on software development.",
                start_date="Sep 2015",
                end_date="May 2019"
            )
            db.session.add(education1)

        if not Certification.query.first():
            certification1 = Certification(
                name="Certified Python Developer",
                issuing_organization="Python Institute",
                issue_date="Jun 2020"
            )
            db.session.add(certification1)

        if not Skill.query.first():
            skill1 = Skill(name="Ansible")
            skill2 = Skill(name="Docker")
            skill3 = Skill(name="Cloudbees/Jenkins")
            skill4 = Skill(name="Python")
            skill5 = Skill(name="ISO20022")
            skill6 = Skill(name="Alliance Messaging Hub")
            skill7 = Skill(name="Swift Translator")
            skill8 = Skill(name="Microgateway")
            skill9 = Skill(name="Swift Alliance Access")
            skill10 = Skill(name="Alliance Web Platform")
            skill11 = Skill(name="Integration Platform")
            skill12 = Skill(name="Swift Alliance Gateway")
            skill13 = Skill(name="SwiftNet Link")
            skill14 = Skill(name="Hardware Security Module")
            skill15 = Skill(name="Swift CSP")
            skill16 = Skill(name="Swift API")
            skill17 = Skill(name="Splunk")
            skill18 = Skill(name="Java/RHEL/ShellScript")

            db.session.add_all([skill1, skill2, skill3, skill4, skill5, skill6, skill7, skill8, skill9, skill10, skill11, skill12, skill13, skill14, skill15, skill16, skill17, skill18])

        if not Award.query.first():
            award1 = Award(
                name="Kudos Award",
                organization="SWIFT",
                year="Dec 2022",
            )

            award2 = Award(
                name="Passion For Excellence Award",
                organization="BNY Mellon",
                year="2021",
            )

            award3 = Award(
                name="Value Champion Award",
                organization="Standard Chartered",
                year="2019",
            )

            award4 = Award(
                name="Well, Done Award",
                organization="Standard Chartered",
                year="2017",
            )

            award5 = Award(
                name="SPOT Award",
                organization="Syntel Inc",
                year="2014",
            )

            award6 = Award(
                name="Winning Streak",
                organization="Syntel Inc",
                year="2014",
            )
           
            db.session.add_all([award1, award2, award3, award4, award5, award6])

        db.session.commit()
    
    app.run(debug=True)
