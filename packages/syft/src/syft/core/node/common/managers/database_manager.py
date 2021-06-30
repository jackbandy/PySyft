# stdlib
from typing import Any
from typing import List
from typing import Union

# third party
from sqlalchemy.orm import sessionmaker


class DatabaseManager:
    def register(self, **kwargs) -> Any:
        """Register e  new object into the database.

        Args:
            parameters : List of object parameters.
        Returns:
            object: Database Object
        """
        _obj = self._schema(**kwargs)
        session_local = sessionmaker(autocommit=False, autoflush=False, bind=self.db)()
        session_local.add(_obj)
        session_local.commit()
        return _obj

    def query(self, **kwargs) -> Union[None, Any]:
        """Query db objects filtering by parameters
        Args:
            parameters : List of parameters used to filter.
        """
        session_local = sessionmaker(autocommit=False, autoflush=False, bind=self.db)()
        objects = session_local.query(self._schema).filter_by(**kwargs).all()
        session_local.close()
        return objects

    def first(self, **kwargs) -> Union[None, Any]:
        """Query db objects filtering by parameters
        Args:
            parameters : List of parameters used to filter.
        """
        session_local = sessionmaker(autocommit=False, autoflush=False, bind=self.db)()
        objects = session_local.query(self._schema).filter_by(**kwargs).first()
        session_local.close()
        return objects

    def last(self, **kwargs):
        """Query and return the last occurrence.

        Args:
            parameters: List of parameters used to filter.
        Return:
            obj: Last object instance.
        """
        session_local = sessionmaker(autocommit=False, autoflush=False, bind=self.db)()
        obj = session_local.query(self._schema).filter_by(**kwargs).all()[-1]
        session_local.close()
        return obj

    def all(self) -> List[Any]:
        session_local = sessionmaker(autocommit=False, autoflush=False, bind=self.db)()
        result =  list(session_local.query(self._schema).all())
        session_local.close()
        return result

    def delete(self, **kwargs):
        """Delete an object from the database.

        Args:
            parameters: Parameters used to filter the object.
        """
        session_local = sessionmaker(autocommit=False, autoflush=False, bind=self.db)()
        object_to_delete = session_local.query(**kwargs)[0]
        session_local.delete(object_to_delete)
        session_local.commit()
        session_local.close()

    def modify(self, query, values):
        """Modifies one or many records."""
        session_local = sessionmaker(autocommit=False, autoflush=False, bind=self.db)()
        session_local.query(self._schema).filter_by(**query).update(values)
        session_local.commit()
        session_local.close()

    def contain(self, **kwargs) -> bool:
        session_local = sessionmaker(autocommit=False, autoflush=False, bind=self.db)()
        objects = session_local.query(self._schema).filter_by(**kwargs).all()
        session_local.close()
        return len(objects) != 0

    def __len__(self) -> int:
        session_local = sessionmaker(autocommit=False, autoflush=False, bind=self.db)()
        result = session_local.query(self._schema).count()
        session_local.close()
        return result