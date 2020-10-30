# Industry Strings#
INDUSTRY_VERBOSE_NAME = 'Industry'
INDUSTRY_VERBOSE_NAME_PLURAL = 'Industries'
# Industry Strings#

# JobType Strings#
JOB_TYPE_VERBOSE_NAME = 'Job Type'
JOB_TYPE_VERBOSE_NAME_PLURAL = 'Job Types'
# JobType Strings#

# Qualification Strings#
QUALIFICATION_VERBOSE_NAME = 'Qualification'
QUALIFICATION_VERBOSE_NAME_PLURAL = 'Qualifications'
# Qualification Strings#

# EXPERIENCE Strings#
EXPERIENCE_VERBOSE_NAME = 'Experience'
EXPERIENCE_VERBOSE_NAME_PLURAL = 'Experiences'
# EXPERIENCE Strings#

# GENDER Strings#
GENDER_VERBOSE_NAME = 'Gender (Pro)'
GENDER_VERBOSE_NAME_PLURAL = 'Genders (Pro)'
# EXPERIENCE Strings#

# Job Strings#
JOB_VERBOSE_NAME = 'Job'
JOB_VERBOSE_NAME_PLURAL = 'Jobs'
ON_TXT = 'on'
OFF_TXT = 'off'
YES_TXT = 'Yes'
NO_TXT = 'No'
NO_LOCATION = 'Unknown'
NO_NAME = 'None'
# Job Strings#

# COMPANY Strings#
COMPANY_VERBOSE_NAME = 'Company'
COMPANY_VERBOSE_NAME_PLURAL = 'Companies'
# COMPANY Strings#

# Currency Strings#
CURRENCY_VERBOSE_NAME = 'Currency'
CURRENCY_VERBOSE_NAME_PLURAL = 'Currencies'
# Currency Strings#

# Trending_keywords Strings#
TRENDING_KEYWORDS_VERBOSE_NAME = 'Trending Keyword'
TRENDING_KEYWORDS_VERBOSE_NAME_PLURAL = 'Trending Keywords'
# Trending_keywords Strings#

# Career Strings#
CAREER_VERBOSE_NAME = 'Career Advice'
CAREER_VERBOSE_NAME_PLURAL = 'Career Advices'
# Career Strings#

# City Strings#
CITY_VERBOSE_NAME = 'City'
CITY_VERBOSE_NAME_PLURAL = 'Cities'
# City Strings#

# Skills Strings #
SKILLS_VERBOSE_NAME = 'Skill'
SKILLS_VERBOSE_NAME_PLURAL = 'Skills'
# Skills Strings #

# Job Skill Detail Strings #
JOB_SKILL_DETAIL_VERBOSE_NAME = 'Job Skill'
JOB_SKILL_DETAIL_VERBOSE_NAME_PLURAL = 'Job Skills'
# Job Skill Detail Strings #

# Bookmark Job Strings #
BOOKMARK_JOB_VERBOSE_NAME = 'Favorite Job'
BOOKMARK_JOB_VERBOSE_NAME_PLURAL = 'Favorite Jobs'
# Bookmark Job Strings #

# Apply Online Strings #
JOB_APPLICATION_VERBOSE_NAME = 'Job Application'
JOB_APPLICATION_VERBOSE_NAME_PLURAL = 'Job Applications'
# Apply Online Strings #

# Added by Munir (02-03).05.2020 >>>
JOB_SITES = (
    ('ONSITE', 'On-site'),
    ('REMOTE', 'Remote'),
)
DEFAULT_JOB_SITE = 'ONSITE'

JOB_NATURES = (
    ('FULLTIME', 'Full-time'),
    ('PARTTIME', 'Part-time'),
)
DEFAULT_JOB_NATURE = 'FULLTIME'

JOB_TYPES = (
    ('PERMANENT', 'Permanent'),
    ('CONTRACTUAL', 'Contractual'),

)
DEFAULT_JOB_TYPE = 'PERMANENT'

JOB_CREATOR_TYPES = (
    ('OPERATOR', 'Operator'),
    ('SYSTEM', 'System'),
    ('COMPANY', 'Company'),
)
DEFAULT_JOB_CREATOR_TYPE = 'OPERATOR'

JOB_STATUSES = (
    ('NOT_READY', 'Not Ready'),
    ('RAW', 'Raw'),
    ('DRAFT', 'Draft'),
    ('REVIEWED', 'Reviewed'),
    ('APPROVED', 'Approved'),
    ('PUBLISHED', 'Published'),
    ('UNPUBLISHED', 'Unpublished'),
)
DEFAULT_JOB_STATUS = 'DRAFT'

JOBSOURCE_VERBOSE_NAME = 'Job Source'
JOBSOURCE_VERBOSE_NAME_PLURAL = 'Job Sources'

JOBCATEGORY_VERBOSE_NAME = 'Job Category'
JOBCATEGORY_VERBOSE_NAME_PLURAL = 'Job Categories'

JOBGENDER_VERBOSE_NAME = 'Gender Preference(Job)'
JOBGENDER_VERBOSE_NAME_PLURAL = 'Gender Preferences(Job)'

DEFAULT_JOB_COUNTRY = 'BD'

APPLICATION_STATUS_VERBOSE_NAME = 'Application Status'
APPLICATION_STATUS_VERBOSE_NAME_PLURAL = 'Application Statuses'

CITY_VERBOSE_NAME = "City"
CITY_VERBOSE_NAME_PLURAL = "Cities"
# <<<
SALARY_OPTION = (
    ('AMOUNT', 'Amount'),
    ('RANGE', 'Range'),
    ('NEGOTIABLE', 'Negotiable'),

)
DEFAULT_SALARY_OPTION = "AMOUNT"
