from mongoengine import connect, disconnect

from openapi_server.dbmodels.annotation_store import AnnotationStore
from openapi_server.dbmodels.dataset import Dataset
from openapi_server.dbmodels.fhir_store import FhirStore
from openapi_server.dbmodels.note import Note
from openapi_server.dbmodels.patient import Patient


def connect_db():
    connect('mongoenginetest', host='mongomock://localhost')


def disconnect_db():
    disconnect(alias='mongoenginetest')


def create_test_dataset(dataset_id):
    return Dataset(name='datasets/{dataset_id}'.format(
        dataset_id=dataset_id)
    ).save()


def create_test_fhir_store(dataset_id, fhir_store_id):
    return FhirStore(
        name='datasets/{dataset_id}/fhirStores/{fhir_store_id}'
        .format(dataset_id=dataset_id, fhir_store_id=fhir_store_id)
    ).save()


def create_test_patient(dataset_id, fhir_store_id):
    return Patient(
        fhirStoreName='/datasets/{dataset_id}/fhirStores/{fhir_store_id}'
        .format(
            dataset_id=dataset_id,
            fhir_store_id=fhir_store_id),
        identifier='',
        gender='unknown'
    ).save()


def create_test_note(dataset_id, fhir_store_id):
    return Note(
        fhirStoreName='/datasets/{dataset_id}/fhirStores/{fhir_store_id}'
        .format(
            dataset_id=dataset_id,
            fhir_store_id=fhir_store_id),
        text='This is the content of a clinical note.',
        noteType='loinc:LP29684-5',
        patientId='507f1f77bcf86cd799439011'
    ).save()


def create_test_annotation_store(dataset_id, annotation_store_id):
    return AnnotationStore(
        name='datasets/{dataset_id}/annotationStores/{annotation_store_id}'
        .format(dataset_id=dataset_id, annotation_store_id=annotation_store_id)
    ).save()
