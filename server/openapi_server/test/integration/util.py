from mongoengine import connect, disconnect

from openapi_server.dbmodels.annotation import Annotation
from openapi_server.dbmodels.annotation_source import AnnotationSource
from openapi_server.dbmodels.annotation_store import AnnotationStore
from openapi_server.dbmodels.dataset import Dataset
from openapi_server.dbmodels.fhir_store import FhirStore
from openapi_server.dbmodels.note import Note
from openapi_server.dbmodels.patient import Patient
from openapi_server.dbmodels.resource_source import ResourceSource


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


def create_test_patient(dataset_id, fhir_store_id, patient_id):
    store_name = 'datasets/%s/fhirStores/%s' % (dataset_id, fhir_store_id)
    resource_name = '%s/fhir/Patient/%s' % (store_name, patient_id)
    return Patient(
        resourceName=resource_name,
        fhirStoreName=store_name,
        identifier=patient_id,
        gender='unknown'
    ).save()


def create_test_note(dataset_id, fhir_store_id, note_id):
    store_name = 'datasets/%s/fhirStores/%s' % (dataset_id, fhir_store_id)
    resource_name = '%s/fhir/Note/%s' % (store_name, note_id)
    return Note(
        resourceName=resource_name,
        fhirStoreName=store_name,
        identifier=note_id,
        text='This is the content of a clinical note.',
        noteType='loinc:LP29684-5',
        patientId='awesome-patient'
    ).save()


def create_test_annotation_store(dataset_id, annotation_store_id):
    return AnnotationStore(
        name='datasets/{dataset_id}/annotationStores/{annotation_store_id}'
        .format(dataset_id=dataset_id, annotation_store_id=annotation_store_id)
    ).save()


def create_test_annotation(dataset_id, annotation_store_id, annotation_id):
    store_name = 'datasets/%s/annotationStores/%s' % \
        (dataset_id, annotation_store_id)
    resource_name = '%s/annotations/%s' % (store_name, annotation_id)
    return Annotation(
        name=resource_name,
        annotationSource=AnnotationSource(
            resourceSource=ResourceSource(name='full/path/to/resource')
        ),
        annotationStoreName=store_name,
        textDateAnnotations=[],
        textPersonNameAnnotations=[],
        textPhysicalAddressAnnotations=[]
    ).save()
