import re

def parse_resume(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            
            name = content.split("\n")[0].strip() if content else "Not found"
            email = re.search(r"[A-Za-z0-9._+%-]+@[A-Za-z0-9.-]+", content)
            phone = re.search(r"\b\d{10}\b", content)
            skills = re.findall(r"\b(python|java|c\+\+|sql|html|css|javascript|react)\b", content, re.IGNORECASE)
            
            return {
                "name": name,
                "email": email.group() if email else "Not found",
                "phone": phone.group() if phone else "Not found",
                "skills": skills
            }
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def match_resume(resume_data, job_description_file):
    if resume_data is None:
        return None
    
    try:
        with open(job_description_file, "r") as file:
            job_desc = file.read()
        
        required_skills = re.findall(r"\b(python|java|c\+\+|sql|javascript|react|html|css)\b", job_desc, re.IGNORECASE)
        matched_skills = [skill for skill in resume_data["skills"] if skill.lower() in map(str.lower, required_skills)]
        score = (len(matched_skills) / len(required_skills)) * 100 if required_skills else 0
        missing_skills = set(map(str.lower, required_skills)) - set(map(str.lower, matched_skills))

        # required_skills = [skill.strip().lower() for skill in required_skills]
        # matched_skills = [skill.strip().lower() for skill in matched_skills]
        

        return {
            "score": round(score, 2),
            "matched_skills": matched_skills,
            "missing_skills": list(missing_skills)
        }
    except FileNotFoundError:
        print(f"Error: File '{job_description_file}' not found.")
        return None

def main():
    print("WELCOME TO THE RESUME ANALYZER!!!")
    resume_file = input("Enter the resume file name: ")
    job_file = input("Enter the job description file: ")
    
    resume_data = parse_resume(f"resumes/{resume_file}")
    if resume_data is None:
        return
    
    print("\nRESUME DETAILS")
    for key, value in resume_data.items():
        print(f"{key.capitalize()}: {value}")

    analysis = match_resume(resume_data, f"job_descriptions/{job_file}")
    if analysis is None:
        return
    
    print("\nANALYSIS REPORT:")
    print(f"Score: {analysis['score']}%")
    print(f"Matched Skills: {', '.join(analysis['matched_skills']) if analysis['matched_skills'] else 'None'}")
    print(f"Missing Skills: {', '.join(analysis['missing_skills']) if analysis['missing_skills'] else 'None'}")

    with open("resume_analysis_report.txt", "w") as file:
        file.write("Resume Analysis Report\n")
        file.write(f"Score: {analysis['score']}%\n")
        file.write(f"Matched Skills: {', '.join(analysis['matched_skills']) if analysis['matched_skills'] else 'None'}\n")
        file.write(f"Missing Skills: {', '.join(analysis['missing_skills']) if analysis['missing_skills'] else 'None'}\n")
    
    print("THE REPORT IS SAVED")

if __name__ == "__main__":
    main()
