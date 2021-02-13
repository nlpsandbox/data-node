import connexion
from mongoengine.errors import DoesNotExist, NotUniqueError

from openapi_server.dbmodels.fhir_store import FhirStore as DbFhirStore  # noqa: E501
from openapi_server.dbmodels.patient import Patient as DbPatient  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.page_of_patients import PageOfPatients  # noqa: E501
from openapi_server.models.patient import Patient  # noqa: E501
from openapi_server.models.patient_create_request import PatientCreateRequest  # noqa: E501
from openapi_server.models.patient_create_response import PatientCreateResponse  # noqa: E501
from openapi_server.config import Config
from openapi_server.controllers.note_controller import delete_notes_by_patient  # noqa: E501


def create_patient(dataset_id, fhir_store_id, patient_id):  # noqa: E501
    """Create a FHIR patient

    Create a FHIR patient # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param fhir_store_id: The ID of the FHIR store
    :type fhir_store_id: str
    :param patient_id: The ID of the patient that is being created
    :type patient_id: str

    :rtype: PatientCreateResponse
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
            patient_create_request = PatientCreateRequest.from_dict(
                connexion.request.get_json())
            resource_name = "%s/fhir/Patient/%s" % (store_name, patient_id)
            DbPatient(
                resourceName=resource_name,
                fhirStoreName=store_name,
                identifier=patient_id,
                gender=patient_create_request.gender
            ).save()
            patient_resource_name = "%s/fhir/Patient/%s" % \
                (store_name, patient_id)
            res = PatientCreateResponse(name=patient_resource_name)
            status = 201
        except NotUniqueError as error:
            status = 409
            res = Error("Conflict", status, str(error))
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def delete_patient(dataset_id, fhir_store_id, patient_id):  # noqa: E501
    """Delete a FHIR patient

    Deletes the FHIR patient specified # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param fhir_store_id: The ID of the FHIR store
    :type fhir_store_id: str
    :param patient_id: The ID of the FHIR patient
    :type patient_id: str

    :rtype: object
    """
    res = None
    status = None
    try:
        store_name = "datasets/%s/fhirStores/%s" % \
            (dataset_id, fhir_store_id)
        resource_name = "%s/fhir/Patient/%s" % \
            (store_name, patient_id)
        delete_notes_by_patient(store_name, patient_id)
        DbPatient.objects.get(resourceName=resource_name).delete()
        res = {}
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def get_patient(dataset_id, fhir_store_id, patient_id):  # noqa: E501
    """Get a FHIR patient

    Returns the FHIR patient specified # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param fhir_store_id: The ID of the FHIR store
    :type fhir_store_id: str
    :param patient_id: The ID of the FHIR patient
    :type patient_id: str

    :rtype: Patient
    """
    res = None
    status = None
    try:
        resource_name = "datasets/%s/fhirStores/%s/fhir/Patient/%s" % \
            (dataset_id, fhir_store_id, patient_id)
        db_patient = DbPatient.objects.get(resourceName=resource_name)
        res = Patient.from_dict(db_patient.to_dict())
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def list_patients(dataset_id, fhir_store_id, limit=None, offset=None):  # noqa: E501
    """List the Patients in a FHIR store

    Returns the Patients in a FHIR store # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param fhir_store_id: The ID of the FHIR store
    :type fhir_store_id: str
    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageOfPatients
    """
    res = None
    status = None
    try:
        store_name = "datasets/%s/fhirStores/%s" % (dataset_id, fhir_store_id)
        db_objects = DbPatient.objects(fhirStoreName=store_name)
        db_patients = db_objects.skip(offset).limit(limit)
        total_results = db_objects.count()
        patients = [Patient.from_dict(p.to_dict()) for p in db_patients]
        next_ = ""
        if len(patients) == limit:
            next_ = '{api_url}/{fhir_store_name}/fhir/Patient?limit={limit}' \
                '&offset={offset}'.format(
                    api_url=Config().server_api_url,
                    fhir_store_name=store_name,
                    limit=limit,
                    offset=offset + limit
                )
        res = PageOfPatients(
            offset=offset,
            limit=limit,
            links={
                "next": next_
            },
            total_results=total_results,
            patients=patients
        )
        status = 200
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status
