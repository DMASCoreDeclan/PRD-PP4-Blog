# Rename this to env.py and place in the root directory.
# Ensure you add it to .gitignore

import os
if os.path.exists("env.py"):
  import env 

os.environ.setdefault(
	"SECRET_KEY",'Your_Secret_Key'
	)

os.environ.setdefault(
	"DATABASE_URL", 'Your_postgres://ugefica_URL'
	)
os.environ.setdefault(
    "CLOUDINARY_URL", 'Your_cloudinary://87634_URL'
    )
