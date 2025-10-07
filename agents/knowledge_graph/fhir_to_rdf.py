from rdflib import Graph, URIRef, BNode, OWL, RDF, Literal, Namespace
import json

# NAMESPACES for graph
FHIR = Namespace("http://hl7.org/fhir/")
EX = Namespace("http://example.org/")

# limit depth on these keys
DEPTH_LIMIT_ON = ['identifier', # 'subject', 
                  'encounter', 'serviceProvider', 'individual', 'code',
                  'coding', 'valueCoding', 'type', 'text', 'verificationStatus',
                  'clinicalStatus', 'reference', 'period', 'class', 'name']
SKIP_KEYS = ['resourceType', 'id',  # because these two should already have been parsed
             'extension', 'telecom', 'address', 'maritalStatus', 'language', 'display']

class FhirGraph():
    '''A FHIR RDF representation of a FHIR JSON resource'''

    def __init__(self, data) -> Graph:
        '''Construct an RDF representaiton of FHIR Resource(s)
        :param data: source JSON representation of FHIR Resource(s)
        '''
        self._graph = Graph()
        self._graph.bind("fhir", FHIR)
        self._graph.bind("ex", EX)
        self._source = data
        if 'entry' in self._source:
            # Bundle
            self._root_resource_type = 'Bundle'
        elif 'resourceType' in self._source:
            self._root_resource_type = self._source['resourceType']
        self.generate()
        return self._graph
    
    def add_reference_to_graph(self, reference_root, data_val: dict):
        '''
        :param reference_root:
        :param data_val: passed along from 
        '''
        reference_node = BNode()
        self._graph.add((reference_root, FHIR.reference, reference_node))
        self._graph.add((reference_node, FHIR.value, Literal(data_val['reference'])))

    def add_subject_reference_to_graph(self, root, data_key: str, data_val: dict):
        '''assuming that subject is a reference to a Patient (not necessarily true)
        :param root: root level of resource in RDF
        :param data_key: key for JSON object reference, should be 'subject'
        :param data_val: value for JSON object reference as dictionary
        '''
        if data_key != 'subject':
            return
        entry = BNode()
        self._graph.add((root, FHIR[data_key], entry))
        self._graph.add((entry, RDF.type, FHIR.Patient))
        self._graph.add((entry, FHIR.type, FHIR.Patient))
        if 'reference' in data_val:
            # reference_bundle_entry = self._source['entry'][['fullUrl'] == value['reference']]
            # print(reference_bundle_entry)
            # establish blank node reference
            self.add_reference_to_graph(entry, data_val)
            # establish fhir:link
            reference_id = str.split(data_val['reference'], ':')[-1] # assuming reference is of the form "urn:uuid:#######"
            self._graph.add((entry, FHIR.link, URIRef(EX['Patient' + '/' + reference_id])))
        if 'display' in data_val:
            display_value = data_val['display']
            self._graph.add((entry, FHIR.display, Literal(display_value)))
        # print([x for x in value.items()]) # TEMP DEBUG LINE

    def add_data_to_graph(self, data, root=None):
        '''Add data from FHIR resource to graph
        :param data: data from a FHIR resource to be added to the graph
        :param root: root level of resource in RDF, for recursive calls
        '''
        if root is None:
            resource_type = data['resourceType']
            root = URIRef(EX[resource_type + '/' + data['id']])
            
            # Add basic properties for each resource
            self._graph.add((root, RDF.type, FHIR[resource_type]))
            self._graph.add((root, FHIR.nodeRole, FHIR.treeRoot))
            self._graph.add((root, FHIR.resourceType, Literal(resource_type)))
        
        # Iterate over the attributes of the resource
        for key, value in data.items():
            if key in SKIP_KEYS:  # Skip resourceType, id, etc
                continue

            if isinstance(value, dict):  # Handle nested objects
                if key in ['subject']:
                    # assuming that subject is a reference to a Patient (not necessarily true)
                    self.add_subject_reference_to_graph(root, key, value)
                if key not in DEPTH_LIMIT_ON:
                    self.add_data_to_graph(value, root)  # Recursive call for nested objects
                self._graph.add((root, FHIR[key], Literal(value)))  # Link to the nested resource
            elif isinstance(value, list):  # Handle lists
                for item in value:
                    if isinstance(item, dict):  # If the item is a resource
                        if key not in DEPTH_LIMIT_ON:
                            self.add_data_to_graph(item, root)  # Recursive call for nested resources
                        self._graph.add((root, FHIR[key], Literal(item)))
                    else:
                        self._graph.add((root, FHIR[key], Literal(item)))
            else:
                self._graph.add((root, FHIR[key], Literal(value)))

    def generate(self) -> Graph:
        '''generator method for FhirGraph'''
        self.add_data_to_graph(data=self._source)