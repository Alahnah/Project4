JobPosting
--
job_id int PK
title varchar(255)
department varchar(255)
salary_range varchar(25)
telecommuting bool
has_company_logo bool
has_questions bool
fraudulent bool
country_id FK >- Country.country_id int
emp_type_id FK >- EmploymentType.emp_type_id int
req_exp_id FK >- RequiredExperience.req_exp_id int
req_edu_id FK >- RequiredEducation.req_edu_id int
industry_id FK >- Industry.industry_id int
function_id FK >- Function.function_id int

Country
--
country_id int PK
country varchar(2)

Function
--
function_id int PK
function varchar(25)

EmploymentType
--
emp_type_id int PK
employment_type varchar(10)

Industry
--
industry_id int PK
industry varchar(50)

RequiredEducation
--
req_edu_id int PK
required_education varchar(50)

RequiredExperience
--
req_exp_id int PK
required_experience varchar(50)