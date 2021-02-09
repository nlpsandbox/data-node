import connexion
from mongoengine.errors import DoesNotExist, NotUniqueError

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.note import Note  # noqa: E501
from openapi_server.models.note_create_request import NoteCreateRequest  # noqa: E501
from openapi_server.models.note_create_response import NoteCreateResponse  # noqa: E501
from openapi_server.models.page_of_notes import PageOfNotes  # noqa: E501
from openapi_server.dbmodels.fhir_store import FhirStore as DbFhirStore
from openapi_server.dbmodels.note import Note as DbNote
from openapi_server.dbmodels.patient import Patient as DbPatient
from openapi_server.config import Config


def create_note(dataset_id, fhir_store_id, note_id):  # noqa: E501
    """Create a note

    Create a note # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param fhir_store_id: The ID of the FHIR store
    :type fhir_store_id: str
    :param note_id: The ID of the note that is being created
    :type note_id: str

    :rtype: NoteCreateResponse
    """
    res = None
    status = None
    try:
        store_name = None
        try:
            store_name = "datasets/%s/fhirStores/%s" % (dataset_id, fhir_store_id)  # noqa: E501
            DbFhirStore.objects.get(name=store_name)
        except DoesNotExist:
            status = 400
            res = Error("The specified FHIR store was not found", status)
            return res, status

        try:
            note_create_request = NoteCreateRequest.from_dict(connexion.request.get_json())  # noqa: E501
            try:
                DbPatient.objects.get(id=note_create_request.patient_id)
            except DoesNotExist:
                status = 400
                res = Error("The specified patientId was not found", status)
                return res, status

            resource_name = "%s/Note/%s" % (store_name, note_id)

            db_note = DbNote(
                identifier=note_id,
                resourceName=resource_name,
                fhirStoreName=store_name,
                text=note_create_request.text,
                noteType=note_create_request.note_type,
                patientId=note_create_request.patient_id
            ).save()
            note = Note.from_dict(db_note.to_dict())
            note_resource_name = "%s/Note/%s" % (store_name, note.id)
            res = NoteCreateResponse(name=note_resource_name)
            status = 201
        except NotUniqueError as error:
            status = 409
            res = Error("Conflict", status, str(error))
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def delete_note(dataset_id, fhir_store_id, note_id):  # noqa: E501
    """Delete a note

    Deletes the note specified # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param fhir_store_id: The ID of the FHIR store
    :type fhir_store_id: str
    :param note_id: The ID of the note
    :type note_id: str

    :rtype: object
    """
    res = None
    status = None
    try:
        resource_name = "datasets/%s/fhirStores/%s/Note/%s" % \
            (dataset_id, fhir_store_id, note_id)
        DbNote.objects.get(resourceName=resource_name).delete()
        res = {}
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def delete_notes_by_patient(fhir_store_name, patientId):
    res = None
    status = None
    try:
        DbNote.objects(
            fhirStoreName=fhir_store_name & patientId=patientId).delete()
        res = {}
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


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
    res = None
    status = None
    try:
        resource_name = "datasets/%s/fhirStores/%s/Note/%s" % \
            (dataset_id, fhir_store_id, note_id)
        db_note = DbNote.objects.get(resourceName=resource_name)
        res = Note.from_dict(db_note.to_dict())
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


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
    res = None
    status = None
    try:
        store_name = "datasets/%s/fhirStores/%s" % (dataset_id, fhir_store_id)
        db_notes = DbNote.objects(fhirStoreName=store_name) \
            .skip(offset).limit(limit)
        notes = [Note.from_dict(n.to_dict()) for n in db_notes]
        next_ = ""
        if len(notes) == limit:
            next_ = '{api_url}/{fhir_store_name}/fhir/Note?limit={limit}' \
                '&offset={offset}'.format(
                    api_url=Config().server_api_url,
                    fhir_store_name=store_name,
                    limit=limit,
                    offset=offset + limit
                )
        res = PageOfNotes(
            offset=offset,
            limit=limit,
            links={
                "next": next_
            },
            notes=notes)
        status = 200
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status
