import connexion
import six

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.note import Note  # noqa: E501
from openapi_server.models.page_of_notes import PageOfNotes  # noqa: E501
from openapi_server import util


def create_note(dataset_id, store_id, note=None):  # noqa: E501
    """Create a note linked to a dataset ID and store ID

    Create a note # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param store_id: The ID of the store
    :type store_id: str
    :param note: 
    :type note: dict | bytes

    :rtype: Note
    """
    if connexion.request.is_json:
        note = Note.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_note(dataset_id, store_id, id):  # noqa: E501
    """Delete an note by ID

    Deletes the note for a given ID # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param store_id: The ID of the store
    :type store_id: str
    :param id: The ID of the note
    :type id: str

    :rtype: Note
    """
    return 'do some magic!'


def get_note(dataset_id, store_id, id):  # noqa: E501
    """Get a note by ID

    Returns the note for a given ID # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param store_id: The ID of the store
    :type store_id: str
    :param id: The ID of the note
    :type id: str

    :rtype: Note
    """
    return 'do some magic!'


def list_notes(dataset_id, store_id, limit=None, offset=None):  # noqa: E501
    """Get all notes linked to a dataset ID and store ID

    Returns the notes for a given dataset ID and store ID # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param store_id: The ID of the store
    :type store_id: str
    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageOfNotes
    """
    return 'do some magic!'
