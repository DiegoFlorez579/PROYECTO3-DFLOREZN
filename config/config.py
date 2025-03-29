import os

DATABASE_URL = os.getenv("DATABASE_URL", "")
if DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")
else:
    print("❌ ERROR: No se encontró DATABASE_URL")
