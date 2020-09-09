import connexion
import six

from openapi_server.models.note import Note  # noqa: E501
from openapi_server import util


def notes_read(id):  # noqa: E501
    """Get a clinical note by ID

    Returns the clinical note for a given ID # noqa: E501

    :param id: The ID of the clinical note to fetch
    :type id: str

    :rtype: Note
    """
    return 'do some magic!'


def notes_read_all():  # noqa: E501
    """Get all clinical notes

    Returns the clinical notes # noqa: E501


    :rtype: List[Note]
    """
    return 'do some magic!'


def notes_update(id, note):  # noqa: E501
    """Update a clinical note by ID

    This can only be done by the logged in user. # noqa: E501

    :param id: Updates the clinical note for a given ID
    :type id: str
    :param note: Updated clinical note
    :type note: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        note = Note.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
