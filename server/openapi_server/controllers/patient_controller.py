import connexion
from mongoengine.errors import DoesNotExist

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.page_of_patients import PageOfPatients  # noqa: E501
from openapi_server.models.patient import Patient  # noqa: E501
from openapi_server.dbmodels.fhir_store import FhirStore as DbFhirStore
from openapi_server.dbmodels.patient import Patient as DbPatient
from openapi_server.config import Config


def create_patient(dataset_id, fhir_store_id, patient=None):  # noqa: E501
    """Create a FHIR Patient

    Create a FHIR Patient # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param fhir_store_id: The ID of the FHIR store
    :type fhir_store_id: str
    :param patient:
    :type patient: dict | bytes

    :rtype: Patient
    """
    res = None
    status = None

    # check if the FHIR store exists
    store_name = None
    try:
        store_name = "datasets/%s/fhirStores/%s" % (dataset_id, fhir_store_id)
        DbFhirStore.objects.get(name=store_name)
    except DoesNotExist:
        status = 404
        res = Error("The specified FHIR store was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    # create the patient
    if status is None and connexion.request.is_json:
        try:
            patient = Patient.from_dict(connexion.request.get_json())
            db_patient = DbPatient(
                fhirStoreName=store_name,
                identifier=patient.identifier,
                gender=patient.gender
            ).save()
            res = Patient.from_dict(db_patient.to_dict())
            status = 201
        except Exception as error:
            status = 500
            res = Error("Internal error", status, str(error))

    return res, status


def delete_patient(dataset_id, fhir_store_id, patient_id):  # noqa: E501
    """Delete a FHIR Patient

    Deletes the FHIR Patient specified # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param fhir_store_id: The ID of the FHIR store
    :type fhir_store_id: str
    :param patient_id: The ID of the FHIR Patient
    :type patient_id: str

    :rtype: Patient
    """
    res = None
    status = None
    try:
        db_patient = DbPatient.objects.get(id=patient_id)
        res = Patient.from_dict(db_patient.to_dict())
        db_patient.delete()
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status


def get_patient(dataset_id, fhir_store_id, patient_id):  # noqa: E501
    """Get a FHIR Patient

    Returns the FHIR Patient specified # noqa: E501

    :param dataset_id: The ID of the dataset
    :type dataset_id: str
    :param fhir_store_id: The ID of the FHIR store
    :type fhir_store_id: str
    :param patient_id: The ID of the FHIR Patient
    :type patient_id: str

    :rtype: Patient
    """
    res = None
    status = None
    try:
        db_patient = DbPatient.objects.get(id=patient_id)
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
        db_patients = DbPatient.objects(
            fhirStoreName__startswith=store_name).skip(offset).limit(limit)
        patients = [Patient.from_dict(p.to_dict()) for p in db_patients]
        next_ = ""
        if len(patients) == limit:
            next_ = (
                "%s/datasets/%s/fhirStores/%s/fhir/Patient"
                "?limit=%s&offset=%s") % \
                (Config().server_api_url, dataset_id, fhir_store_id, limit,
                    offset + limit)
        res = PageOfPatients(
            offset=offset,
            limit=limit,
            links={
                "next": next_
            },
            patients=patients)
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status
