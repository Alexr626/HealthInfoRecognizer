import openai
import os 

import pandas as pd

column_names = ["Abbreviation", "Full_Form", "Abbreviation_In_Context", "Start_Index", "End_Index", "Category", "Context"]

# Trying to load the data with 'ISO-8859-1' encoding
data = pd.read_csv("data.txt", delimiter="|", names=column_names, header=None, encoding='ISO-8859-1')

# Displaying the first few rows of the DataFrame
data.head()

# print data to see if it is loaded correctly
# medication name
# status
# active/discontinued
#  
# print(data)

import random

from sklearn.model_selection import train_test_split

# Split the 'Context' column into training and testing data
train_data, test_data = train_test_split(data['Context'], test_size=0.2, random_state=42)

# Iterate over the random subset and run the code
for context in test_data:
    system_message = """
        You are a world class state of the art agent. Your purpose is to correctly complete this task :
    `Return the list of  medicines that the user is taking and the discription  to complete the task ` These are the guidelines you consider when completing
    your task: Give the correct medicing. If you are unsure of the answer, try to think about the task as a whole. """

    assistant_message = """Let's think step by step to get the correct answer"""

    user_message = f"""Give me the medicine for the following doctors note : {context}"""

    functions = [{
        "name": "get_medicines",
        "description": "Get the steps to complete the high level task",
        "parameters": {
            "type": "object",
            "properties": {
                "medicines": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "medication": {
                                "type": "string",
                                "description": "Name of the medication"
                            },
                            "status": {
                                "type": "string",
                                "description": "Status of the medication",
                                "enum": ["active", "discontinued"]
                            }
                        },
                        "required": ["medication", "status"]
                    }
                }
            },
            "required": ["medicines"]
        }
    }]

    response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0613", messages=[
                    {
                        "role": "system", "content": system_message}, {
                        "role": "assistant", "content": assistant_message},
                        {"role": "user", "content": user_message}
                          ], functions=functions, function_call={
                                "name": "get_medicines"})
    
    # Get the response
    response_json = response.to_dict()
    function_call_arguments = response_json['choices'][0]['message']['function_call']['arguments']
    print(function_call_arguments)
    # Load function_call_arguments as a json rather than a string
    import json
    function_call_arguments = json.loads(function_call_arguments)
    print(function_call_arguments)
    print(context)
    for medicine in function_call_arguments['medicines']:
        
        print(f"Medication: {medicine['medication']}, Status: {medicine['status']}")
    # Print the response in a pretty json format
    #
    # Save the output with "context, and then medicines" to a json file
    output = {"context": context, "medicines": function_call_arguments['medicines']}
    try:
        with open('output.json', 'r') as json_file:
            data = json.load(json_file)
            data.append(output)
    except (FileNotFoundError, json.JSONDecodeError):
        data = [output]

    with open('output.json', 'w') as json_file:
        json.dump(data, json_file)

