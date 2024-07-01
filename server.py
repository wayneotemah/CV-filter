from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import FileResponse
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session
import pandas as pd
from database import SessionLocal, engine, ResumeResponse, Base


from typing import List, Optional
from pdf_reader import process_pdf_from_url
from prompts import get_score

Base.metadata.create_all(bind=engine)

app = FastAPI()

class ResumeItem(BaseModel):
    email: str
    first_name: str
    last_name: str
    academic_university: Optional[str] = None
    employment_company: Optional[str] = None
    course: Optional[str] = None
    goal: Optional[str] = None
    description: Optional[str] = None
    link: Optional[str] = None
    resume: Optional[str] = None
    city: Optional[str] = None
    link: Optional[str] = None
    name: Optional[str] = None
    state: Optional[str] = None
    course: Optional[str] = None
    gender: Optional[str] = None
    country: Optional[str] = None
    area_code: Optional[str] = None
    institution: Optional[str] = None
    nationality: Optional[str] = None
    phone_number: Optional[str] = None
    date_of_birth: Optional[str] = None
    mobile_number: Optional[str] = None
    graduation_year: Optional[str] = None
    mailing_address: Optional[str] = None
    spoken_language: Optional[str] = None
    personal_statement: Optional[str] = None
    academic_background: Optional[str] = None
    academic_transcripts: Optional[str] = None
    expected_achievement: Optional[str] = None
    special_requirements: Optional[str] = None
    supporting_documents: Optional[str] = None
    programming_languages: Optional[str] = None
    why_join_dlt_programme: Optional[str] = None
    can_commit_to_programme: Optional[str] = None
    identification_document: Optional[str] = None
    professional_references: Optional[str] = None
    has_special_requirements: Optional[str] = None
    reliable_internet_access: Optional[str] = None
    blockchain_experience_level: Optional[str] = None
    relevant_certification_file: Optional[str] = None
    academic_achievements_awards: Optional[str] = None
    planned_use_of_skills_earned: Optional[str] = None
    career_goals_in_blockchain_web3: Optional[str] = None
    relevant_courses_certifications: Optional[str] = None
    challenging_problem_solved_with_technology: Optional[str] = None
    integrity_declaration: Optional[str] = None
    terms: Optional[str] = None


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/process_resumes/")
async def process_resumes(resumesItem: ResumeItem,db: Session = Depends(get_db)):
    results = []
    # for resume_item in resumes:
    pdf_url = resumesItem.resume
    resume_text = process_pdf_from_url(pdf_url)
    result = get_score(resume_text)
    message = {}
    if result:
        response_data = {
        "email": resumesItem.email,
        "score": result.score,
        "summary": result.summary,
        "first_name": resumesItem.first_name,
        "last_name": resumesItem.last_name,
        "academic_university": resumesItem.academic_university,
        "employment_company": resumesItem.employment_company,
        "course": resumesItem.course,
        "goal": resumesItem.goal,
        "description": resumesItem.description,
        "link": resumesItem.link,
        "resume": resumesItem.resume,
        "city": resumesItem.city,
        "state": resumesItem.state,
        "gender": resumesItem.gender,
        "country": resumesItem.country,
        "area_code": resumesItem.area_code,
        "institution": resumesItem.institution,
        "nationality": resumesItem.nationality,
        "phone_number": resumesItem.phone_number,
        "date_of_birth": resumesItem.date_of_birth,
        "mobile_number": resumesItem.mobile_number,
        "graduation_year": resumesItem.graduation_year,
        "mailing_address": resumesItem.mailing_address,
        "spoken_language": resumesItem.spoken_language,
        "personal_statement": resumesItem.personal_statement,
        "academic_background": resumesItem.academic_background,
        "academic_transcripts": resumesItem.academic_transcripts,
        "expected_achievement": resumesItem.expected_achievement,
        "special_requirements": resumesItem.special_requirements,
        "supporting_documents": resumesItem.supporting_documents,
        "programming_languages": resumesItem.programming_languages,
        "why_join_dlt_programme": resumesItem.why_join_dlt_programme,
        "can_commit_to_programme": resumesItem.can_commit_to_programme,
        "identification_document": resumesItem.identification_document,
        "professional_references": resumesItem.professional_references,
        "has_special_requirements": resumesItem.has_special_requirements,
        "reliable_internet_access": resumesItem.reliable_internet_access,
        "blockchain_experience_level": resumesItem.blockchain_experience_level,
        "relevant_certification_file": resumesItem.relevant_certification_file,
        "academic_achievements_awards": resumesItem.academic_achievements_awards,
        "planned_use_of_skills_earned": resumesItem.planned_use_of_skills_earned,
        "career_goals_in_blockchain_web3": resumesItem.career_goals_in_blockchain_web3,
        "relevant_courses_certifications": resumesItem.relevant_courses_certifications,
        "challenging_problem_solved_with_technology": resumesItem.challenging_problem_solved_with_technology,
        "integrity_declaration": resumesItem.integrity_declaration,
        "terms": resumesItem.terms
    }

        db_response = ResumeResponse(**response_data)
        db.add(db_response)
        db.commit()
        db.refresh(db_response)
        message = {
            "success": "Resume processed successfully",
        }
        
    else:
        message = {
            "error": "Error processing resume"
        }
    
    return JSONResponse(content=message,status_code=400)


@app.get("/top_users/")
async def get_top_users(number: int, db: Session = Depends(get_db)):
    
    top_users = db.query(ResumeResponse).order_by(ResumeResponse.score.desc()).limit(number).all()
    
    if not top_users:
        raise HTTPException(status_code=404, detail="No users found")
    
    df = pd.DataFrame([user.__dict__ for user in top_users])
    
    # Remove SQLAlchemy internal attributes
    df = df.drop(columns=["_sa_instance_state"])
    
    output_file = "./media/tmp/top_users.xlsx"
    
    # Save the DataFrame to an Excel file
    df.to_excel(output_file, index=False)
    
    # Return the Excel file as a downloadable response
    return FileResponse(output_file, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", filename="top_users.xlsx")