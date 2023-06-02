
from sqlalchemy import  Column, Float, TIMESTAMP, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class Sample(Base):
    __tablename__ = 'samples'
    
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False,
                default=uuid.uuid4)
    real_part = Column(Float)
    imag_part = Column(Float)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
