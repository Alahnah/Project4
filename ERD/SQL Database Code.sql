-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/eT1bA0
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "JobPosting" (
    "job_id" int   NOT NULL,
    "title" varchar(255)   NOT NULL,
    "department" varchar(255)   NULL,
    "salary_range" varchar(25)   NULL,
    "telecommuting" bool   NOT NULL,
    "has_company_logo" bool   NOT NULL,
    "has_questions" bool   NOT NULL,
    "fraudulent" bool   NOT NULL,
    "country_id" int   NOT NULL,
    "emp_type_id" int   NOT NULL,
    "req_exp_id" int   NOT NULL,
    "req_edu_id" int   NOT NULL,
    "industry_id" int   NOT NULL,
    "function_id" int   NOT NULL,
    CONSTRAINT "pk_JobPosting" PRIMARY KEY (
        "job_id"
     )
);

CREATE TABLE "Country" (
    "country_id" int   NOT NULL,
    "country" varchar(2)   NULL,
    CONSTRAINT "pk_Country" PRIMARY KEY (
        "country_id"
     )
);

CREATE TABLE "Function" (
    "function_id" int   NOT NULL,
    "function" varchar(25)   NULL,
    CONSTRAINT "pk_Function" PRIMARY KEY (
        "function_id"
     )
);

CREATE TABLE "EmploymentType" (
    "emp_type_id" int   NOT NULL,
    "employment_type" varchar(10)   NULL,
    CONSTRAINT "pk_EmploymentType" PRIMARY KEY (
        "emp_type_id"
     )
);

CREATE TABLE "Industry" (
    "industry_id" int   NOT NULL,
    "industry" varchar(50)   NULL,
    CONSTRAINT "pk_Industry" PRIMARY KEY (
        "industry_id"
     )
);

CREATE TABLE "RequiredEducation" (
    "req_edu_id" int   NOT NULL,
    "required_education" varchar(50)   NULL,
    CONSTRAINT "pk_RequiredEducation" PRIMARY KEY (
        "req_edu_id"
     )
);

CREATE TABLE "RequiredExperience" (
    "req_exp_id" int   NOT NULL,
    "required_experience" varchar(50)   NULL,
    CONSTRAINT "pk_RequiredExperience" PRIMARY KEY (
        "req_exp_id"
     )
);

ALTER TABLE "JobPosting" ADD CONSTRAINT "fk_JobPosting_country_id" FOREIGN KEY("country_id")
REFERENCES "Country" ("country_id");

ALTER TABLE "JobPosting" ADD CONSTRAINT "fk_JobPosting_emp_type_id" FOREIGN KEY("emp_type_id")
REFERENCES "EmploymentType" ("emp_type_id");

ALTER TABLE "JobPosting" ADD CONSTRAINT "fk_JobPosting_req_exp_id" FOREIGN KEY("req_exp_id")
REFERENCES "RequiredExperience" ("req_exp_id");

ALTER TABLE "JobPosting" ADD CONSTRAINT "fk_JobPosting_req_edu_id" FOREIGN KEY("req_edu_id")
REFERENCES "RequiredEducation" ("req_edu_id");

ALTER TABLE "JobPosting" ADD CONSTRAINT "fk_JobPosting_industry_id" FOREIGN KEY("industry_id")
REFERENCES "Industry" ("industry_id");

ALTER TABLE "JobPosting" ADD CONSTRAINT "fk_JobPosting_function_id" FOREIGN KEY("function_id")
REFERENCES "Function" ("function_id");

