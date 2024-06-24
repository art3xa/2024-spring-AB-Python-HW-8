from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

pg_string = "postgresql+psycopg2://postgres:postgres@localhost:5433/postgres"
ENGINE = create_engine(pg_string)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)


def get_db():
    """Create and get database session.

    :yield: database session.
    """
    with SessionLocal() as session:
        try:
            return session
        except HTTPException:
            session.rollback()
            raise
        finally:
            session.close()
