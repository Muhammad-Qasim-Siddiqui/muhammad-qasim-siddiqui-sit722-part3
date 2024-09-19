from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Updated to include sslmode=require for secure SSL connection
SQLALCHEMY_DATABASE_URL = "postgresql://sit722_part3_db_user:gS4ZrYN42FYsXTyfTnaHpELURuhXNcDb@dpg-crm4hgij1k6c73fjgb1g-a.oregon-postgres.render.com/sit722_part3_db?sslmode=require"

# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Set up the session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base model to inherit from
Base = declarative_base()
