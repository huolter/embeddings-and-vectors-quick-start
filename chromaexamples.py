import chromadb

# initialize the client
chroma_client = chromadb.Client()

# create a collection
collection = chroma_client.create_collection(name="my_collection")

# mannualy add some documents
collection.add(
    documents=["What a horrible dog! I hate dogs and cats",
               "I need a new car, or maybe a motorcycle"],
    ids=["id1", "id2"]
)

results = collection.query(
    query_texts=["I saw an elephant"],
    n_results=2
)

print(results)
