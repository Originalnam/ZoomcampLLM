from elasticsearch import Elasticsearch

es = Elasticsearch(["http://localhost:9200"])

if es.ping():
    print("Connected to Elasticsearch")
    print(es.info())
else:
    print("Could not connect to Elasticsearch")