from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./store.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class ResumeResponse(Base):
    __tablename__ = "resume_responses"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    score = Column(Integer)
    summary = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    academic_university = Column(String, nullable=True)
    employment_company = Column(String, nullable=True)
    course = Column(String, nullable=True)
    goal = Column(String, nullable=True)
    description = Column(String, nullable=True)
    link = Column(String, nullable=True)
    resume = Column(String, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)
    gender = Column(String, nullable=True)
    country = Column(String, nullable=True)
    area_code = Column(String, nullable=True)
    institution = Column(String, nullable=True)
    nationality = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    date_of_birth = Column(String, nullable=True)
    mobile_number = Column(String, nullable=True)
    graduation_year = Column(String, nullable=True)
    mailing_address = Column(String, nullable=True)
    spoken_language = Column(String, nullable=True)
    personal_statement = Column(String, nullable=True)
    academic_background = Column(String, nullable=True)
    academic_transcripts = Column(String, nullable=True)
    expected_achievement = Column(String, nullable=True)
    special_requirements = Column(String, nullable=True)
    supporting_documents = Column(String, nullable=True)
    programming_languages = Column(String, nullable=True)
    why_join_dlt_programme = Column(String, nullable=True)
    can_commit_to_programme = Column(String, nullable=True)
    identification_document = Column(String, nullable=True)
    professional_references = Column(String, nullable=True)
    has_special_requirements = Column(String, nullable=True)
    reliable_internet_access = Column(String, nullable=True)
    blockchain_experience_level = Column(String, nullable=True)
    relevant_certification_file = Column(String, nullable=True)
    academic_achievements_awards = Column(String, nullable=True)
    planned_use_of_skills_earned = Column(String, nullable=True)
    career_goals_in_blockchain_web3 = Column(String, nullable=True)
    relevant_courses_certifications = Column(String, nullable=True)
    challenging_problem_solved_with_technology = Column(String, nullable=True)
    integrity_declaration = Column(String, nullable=True)
    terms = Column(String, nullable=True)

Base.metadata.create_all(bind=engine)
