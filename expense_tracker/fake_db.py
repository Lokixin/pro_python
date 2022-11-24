import logging
import uuid

from pydantic.error_wrappers import ValidationError

from expense_tracker.models import UserIn


logger = logging.getLogger(__name__)

user_list = {
    0: {
        "name": "John",
        "surname": "Doe",
        "email": "johndoe@gmail.com",
        "age": 30,
    },
    1: {
        "name": "George",
        "surname": "Pierre",
        "email": "george@pierre.com",
        "age": 27,
    },
}


class InvalidUserFormat(Exception):
    pass


class FakeCollection:
    def __init__(self, name: str, schema) -> None:
        self.name = name
        self.Schema = schema
        self.documents = {}

    def _generate_uuid(self) -> str:
        return uuid.uuid4().hex

    def insert(self, data: dict | list[dict]) -> None:
        try:
            if isinstance(data, dict):
                self.Schema(**data)
                document_uuid = self._generate_uuid()
                self.documents[document_uuid] = data
            if isinstance(data, list):
                documents_uuids = [
                    self._generate_uuid()
                    for document in data
                    if self.Schema(**document) is not None
                ]
                self.documents = {**self.documents, **dict(zip(documents_uuids, data))}
        except ValidationError:
            logger.exception("Invalid User Input data")
            raise InvalidUserFormat("Data could not be inserted because format is not adequate")

    def update(self, document_uuid: str, props: dict) -> dict:
        try:
            doc = self.documents[document_uuid]
            for key, val in props.items():
                if not(key in doc):
                    raise InvalidUserFormat
                doc[key] = val
            return doc
        except KeyError:
            logger.info("Invalid user uuid")

    def delete(self, document_uuid: str | list[str]):
        if isinstance(document_uuid, list):
            deleted = [
                self.documents.pop(doc_uuid, None)
                for doc_uuid in document_uuid
            ]
            return deleted
        return [self.documents.pop(document_uuid, None)]

    def find(self, **kwargs):
        if "uuid" in kwargs:
            return self.documents[kwargs.get("uuid", None)]
        if not kwargs:
            return self.documents

        results = []

        for doc_key, doc in self.documents.items():
            for key, val in kwargs.items():
                if not(doc[key] == val):
                    break
            else:
                doc["uuid"] = doc_key
                results.append(doc)
        return results


if __name__ == "__main__":
    coll = FakeCollection(name="users", schema=UserIn)
    coll.insert(list(user_list.values()))
    print(coll.documents)
    results = coll.find(name="George", surname="Pierre")
    print(results)
    first_uuid = results[0]["uuid"]
    coll.find(uuid=first_uuid)
    updated_user = coll.update(
        document_uuid=first_uuid,
        props={"name": "Dimas", "age": 25}
    )
    print(updated_user)
    print(coll.find())
    print(coll.delete(document_uuid=first_uuid))
