# import connexion
# import six

# from openapi_server.models.error import Error  # noqa: E501
# from openapi_server.models.note_store import NoteStore  # noqa: E501
# from openapi_server.models.page_of_note_stores import PageOfNoteStores  # noqa: E501
# from openapi_server import util


def create_note_store(dataset_id, note_store=None):  # noqa: E501
    """Create a note store linked to a dataset ID

    Create a note store with the name specified # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param note_store:
    :type note_store: dict | bytes

    :rtype: NoteStore
    """
    # if connexion.request.is_json:
    #     note_store = NoteStore.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_note_store(dataset_id, id):  # noqa: E501
    """Delete a note store by ID

    Deletes the note store for a given ID # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param id: The ID of the note store
    :type id: str

    :rtype: NoteStore
    """
    return 'do some magic!'


def get_note_store(dataset_id, id):  # noqa: E501
    """Get a note store by ID

    Returns the note store for a given ID # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param id: The ID of the note store
    :type id: str

    :rtype: NoteStore
    """
    return 'do some magic!'


def list_note_stores(dataset_id, limit=None, offset=None):  # noqa: E501
    """Get all note stores by dataset ID

    Returns the note stores for a given dataset ID # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageOfNoteStores
    """
    return 'do some magic!'
