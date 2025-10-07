from rdflib import Graph, URIRef, BNode, OWL, RDF, Literal, Namespace
import json

# NAMESPACES for graph
FHIR = Namespace("http://hl7.org/fhir/")
EX = Namespace("http://example.org/")

# limit depth on these keys
DEPTH_LIMIT_ON = ['identifier', 'individual', 'code',
                  'coding', 'valueCoding', 'type', 'text', 'verificationStatus',
                  'clinicalStatus', 'period', 'class', 'name']
SKIP_KEYS = ['resourceType', 'id',  # because these two should already have been parsed
             'extension', 'telecom', 'address', 'maritalStatus', 'language', 'display']

# map json key value to resource type
MAP_KEY_TO_RESOURCE_TYPE = { # assumes that these keys are a reference to only one resource type (not necessarily true)
    'subject': 'Patient',
    'serviceProvider': 'Organization',
    'encounter': 'Encounter'
}

class FhirGraph():
    '''A FHIR RDF representation of a FHIR JSON resource'''

    def __init__(self, data, target_graph: Graph=None) -> Graph:
        '''Construct an RDF representaiton of FHIR Resource(s)
        :param data: source JSON representation of FHIR Resource(s)
        '''
        self._graph = target_graph if target_graph is not None else Graph()
        self._graph.bind("fhir", FHIR)
        self._graph.bind("ex", EX)
        self._source = data
        if 'entry' in self._source:
            # Bundle
            self._root_resource_type = 'Bundle'
        elif 'resourceType' in self._source:
            self._root_resource_type = self._source['resourceType']

    def add_reference_to_resource(self, root_uri: URIRef, data_key: str, data_val: dict, referenced_resource_type: str):
        '''
        :param root_uri: root level of resource in RDF
        :param data_key: key for JSON object reference, should be 'subject'
        :param data_val: value for JSON object reference as dictionary
        :param referenced_resource_type: must be from the FHIR Resource types
        '''
        # OPTION 1: establish direct link
        if 'reference' in data_val:
            reference_id = str.split(data_val['reference'], ':')[-1] # assuming reference is of the form "urn:uuid:#######"
            reference_uri = URIRef(EX[referenced_resource_type + '/' + reference_id])
            self._graph.add((root_uri, FHIR[data_key], reference_uri))
        # OPTION 2: establish link via blank node
        # resource_reference = BNode()
        # self._graph.add((root_uri, FHIR[data_key], resource_reference))
        # self._graph.add((resource_reference, RDF.type, FHIR[referenced_resource_type]))
        # self._graph.add((resource_reference, FHIR.type, FHIR[referenced_resource_type]))
        # if 'reference' in data_val:
        #     # establish blank node reference
        #     reference_node = BNode()
        #     self._graph.add((resource_reference, FHIR.reference, reference_node))
        #     self._graph.add((reference_node, FHIR.value, Literal(data_val['reference'])))
        #     # establish fhir:link
        #     # TODO: handle other reference schema formats (e.g., "Resource/identifier")
        #     reference_id = str.split(data_val['reference'], ':')[-1] # assuming reference is of the form "urn:uuid:#######"
        #     reference_uri = URIRef(EX[referenced_resource_type + '/' + reference_id])
        #     self._graph.add((resource_reference, FHIR.link, reference_uri))
        # if 'display' in data_val:
        #     self._graph.add((resource_reference, FHIR.display, Literal(data_val['display'])))
        # print([x for x in data_val.items()]) # TEMP DEBUG LINE

    def add_data_to_graph(self, data, root_uri=None):
        '''Add data from FHIR resource to graph
        :param data: data from a FHIR resource to be added to the graph
        :param root_uri: root level of resource in RDF, for recursive calls
        '''
        # print(data)   # TEMP DEBUG LINE
        if root_uri is None:
            resource_type = data['resourceType']
            root_uri = URIRef(EX[resource_type + '/' + data['id']])
            
            # Add basic properties for each resource
            self._graph.add((root_uri, RDF.type, FHIR[resource_type]))
            self._graph.add((root_uri, FHIR.nodeRole, FHIR.treeRoot))
            self._graph.add((root_uri, FHIR.resourceType, Literal(resource_type)))
        
        # Iterate over the attributes of the resource
        for key, value in data.items():
            if key in SKIP_KEYS:  # Skip resourceType, id, etc
                continue

            if isinstance(value, dict):  # Handle nested objects
                if key in MAP_KEY_TO_RESOURCE_TYPE.keys():
                    self.add_reference_to_resource(root_uri, key, value, MAP_KEY_TO_RESOURCE_TYPE[key])
                else:
                    if key not in DEPTH_LIMIT_ON:
                        self.add_data_to_graph(value, root_uri)  # Recursive call for nested objects
                    self._graph.add((root_uri, FHIR[key], Literal(value)))  # Link to the nested resource
            elif isinstance(value, list):  # Handle lists
                for item in value:
                    if isinstance(item, dict):  # If the item is a resource
                        if key not in DEPTH_LIMIT_ON:
                            self.add_data_to_graph(item, root_uri)  # Recursive call for nested resources
                        self._graph.add((root_uri, FHIR[key], Literal(item)))
                    else:
                        self._graph.add((root_uri, FHIR[key], Literal(item)))
            else:
                self._graph.add((root_uri, FHIR[key], Literal(value)))

    def generate(self, limit=5) -> Graph:
        '''generator method for FhirGraph'''
        i = 0
        for entry in self._source['entry']:
            resource = entry['resource']
            self.add_data_to_graph(resource, None)
            i += 1
            if i > limit:
                break
        return self._graph
        # self.add_data_to_graph(data=self._source)