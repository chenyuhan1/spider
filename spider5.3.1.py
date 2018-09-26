import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students
student = {
    'id': '0164589',
    'name': '陈雨寒',
    'age': 20,
    'gender': 'male'
}
student1 = {
    'id': '0164590',
    'name': '陈雨寒2',
    'age': 20,
    'gender': 'male'
}
student2 = {
    'id': '0164591',
    'name': 'chenyuhan',
    'age': 20,
    'gender': 'female'
}
result = collection.insert_many([student, student1, student2])
print(result)
results = collection.find({'age': 20})
print(results)
for result1 in results:
    print(result1)
