import connexion
import six

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.note import Note  # noqa: E501
from openapi_server.models.page_of_notes import PageOfNotes  # noqa: E501
from openapi_server import util


def create_note(dataset_id, fhir_store_id, note=None):  # noqa: E501
    """Create a note

    Create a note # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param fhir_store_id: The ID of the FHIR store
    :type fhir_store_id: str
    :param note: 
    :type note: dict | bytes

    :rtype: Note
    """
    if connexion.request.is_json:
        note = Note.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_note(dataset_id, fhir_store_id, note_id):  # noqa: E501
    """Delete a note

    Deletes the note specified # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param fhir_store_id: The ID of the FHIR store
    :type fhir_store_id: str
    :param note_id: The ID of the note
    :type note_id: str

    :rtype: Note
    """
    return 'do some magic!'


def get_note(dataset_id, fhir_store_id, note_id):  # noqa: E501
    """Get a note

    Returns the note specified # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param fhir_store_id: The ID of the FHIR store
    :type fhir_store_id: str
    :param note_id: The ID of the note
    :type note_id: str

    :rtype: Note
    """
    return 'do some magic!'


def list_notes(dataset_id, fhir_store_id, limit=None, offset=None):  # noqa: E501
    """List notes

    Returns the notes in a FHIR store # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param fhir_store_id: The ID of the FHIR store
    :type fhir_store_id: str
    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageOfNotes
    """
    return 'do some magic!'
