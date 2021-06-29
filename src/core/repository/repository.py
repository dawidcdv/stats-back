import abc
from src.statistics.models.Statistics import Statistics


class AbstractRepository(abc.ABC):

    def add(self, stats):
        self._add(stats)

    def get(self, id):
         return  self._get(id)

    def getAll(self):
        return self._getAll()

    def delete(self,id):
        return self._delete(id)

    @abc.abstractmethod
    def _add(self, stats):
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self, id):
        raise NotImplementedError

    @abc.abstractmethod
    def _getAll(self, id):
        raise NotImplementedError

    @abc.abstractmethod
    def _delete(self, id):
        raise NotImplementedError



class SqlAlchemyRepository(AbstractRepository):

    def __init__(self, session):
        super().__init__()
        self.session = session

