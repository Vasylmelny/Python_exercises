# Print the value of key ‘history’ from nested dict

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print("Key by history is:", sampleDict['class']['student']['marks']['history'])