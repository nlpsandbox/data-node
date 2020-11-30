from mongoengine import connect, disconnect

from openapi_server.dbmodels.dataset import Dataset
from openapi_server.dbmodels.fhir_store import FhirStore
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