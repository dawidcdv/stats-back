import logging
from sqlalchemy import (
    Table, MetaData, Column, Integer, String, Date, JSON, ForeignKey,
)
from sqlalchemy.orm import mapper, relationship
from src.statistics.models.UploadedFile import UploadedFile
from src.statistics.models.Statistics import Statistics

logger = logging.getLogger(__name__)

metadata = MetaData()

uploaded_file = Table(
    'uploaded_file', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(50)),
    Column('checksum', String(50)),
    Column('size', Integer),
    Column('row', Integer),
    Column('column', Integer),
)
statistics = Table(
    'statistics', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('file_id', ForeignKey('uploaded_file.id')),
    Column('name', String(50)),
    Column('description', String(2048)),
    Column('data_description', JSON(2048)),

)

def start_mappers():
    logger.info("Starting mappers")
    uploaded_files = mapper(UploadedFile, uploaded_file)
    stats = mapper(Statistics, statistics, properties={
        'file': relationship(UploadedFile, lazy='subquery')
    })
