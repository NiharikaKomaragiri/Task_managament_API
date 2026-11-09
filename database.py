from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# sessionmaker: Creates database sessions.
# declarative_base: Provides the base class for defining database tables using Python classes.

# Database URL
DATABASE_URL = "sqlite:///./tasks.db"

# Create database engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Create database session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for database models
Base = declarative_base()