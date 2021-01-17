# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json

from openapi_server.dbmodels.annotation import Annotation as DbAnnotation
from openapi_server.dbmodels.annotation_store import AnnotationStore as DbAnnotationStore  # noqa: E501
from openapi_server.dbmodels.dataset import Dataset as DbDataset
from openapi_server.test.integration import BaseTestCase
from openapi_server.test.integration import util


class TestAnnotationController(BaseTestCase):
    """AnnotationController integration test stubs"""

    def setUp(self):
        util.connect_db()
        DbDataset.objects().delete()
        DbAnnotationStore.objects().delete()
        DbAnnotation.objects().delete()
        util.create_test_dataset('awesome-dataset')
        util.create_test_annotation_store(
            'awesome-dataset', 'awesome-annotation-store')

    def tearDown(self):
        util.disconnect_db()

    def test_create_annotation(self):
        """Test case for create_annotation

        Create an annotation
        """
        annotation = {
            "textDateAnnotations": [{
                "start": 42,
                "length": 10,
                "text": "10/26/2020",
                "dateFormat": "MM/DD/YYYY"
            }, {
                "start": 42,
                "length": 10,
                "text": "10/26/2020",
                "dateFormat": "MM/DD/YYYY"
            }],
            "textPersonNameAnnotations": [{
                "start": 42,
                "length": 11,
                "text": "Chloe Price"
            }, {
                "start": 42,
                "length": 11,
                "text": "Chloe Price"
            }],
            "textPhysicalAddressAnnotations": [{
                "start": 42,
                "length": 11,
                "text": "Seattle",
                "addressType": "city"
            }, {
                "start": 42,
                "length": 11,
                "text": "Seattle",
                "addressType": "city"
            }],
            "annotationSource": {
                "resourceSource": {
                    "name": "name"
                }
            }
        }
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/annotationStores'
            '/{annotation_store_id}/annotations'.format(
                dataset_id='awesome-dataset',
                annotation_store_id='awesome-annotation-store'),
            method='POST',
            headers=headers,
            data=json.dumps(annotation),
            content_type='application/json')
        self.assert201(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_annotation(self):
        """Test case for delete_annotation

        Delete an annotation
        """
        annotation = util.create_test_annotation(
            'awesome-dataset', 'awesome-annotation-store')
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/annotationStores'
            '/{annotation_store_id}/annotations/{annotation_id}'.format(
                dataset_id='awesome-dataset',
                annotation_store_id='awesome-annotation-store',
                annotation_id=annotation.id),
            method='DELETE',
            headers=headers)
        self.assert_status(
            response, 201,
            'Response body is : ' + response.data.decode('utf-8'))

    def test_get_annotation(self):
        """Test case for get_annotation

        Get an annotation
        """
        annotation = util.create_test_annotation(
            'awesome-dataset', 'awesome-annotation-store')
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/annotationStores'
            '/{annotation_store_id}/annotations/{annotation_id}'.format(
                dataset_id='awesome-dataset',
                annotation_store_id='awesome-annotation-store',
                annotation_id=annotation.id),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_annotations(self):
        """Test case for list_annotations

        List the annotations in an annotation store
        """
        util.create_test_annotation(
            'awesome-dataset', 'awesome-annotation-store')
        query_string = [('limit', 10),
                        ('offset', 0)]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/annotationStores'
            '/{annotation_store_id}/annotations'.format(
                dataset_id='awesome-dataset',
                annotation_store_id='awesome-annotation-store'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
