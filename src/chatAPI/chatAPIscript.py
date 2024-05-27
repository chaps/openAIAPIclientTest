from openai import OpenAI
import json
import sys

with open('config.json', 'r') as configFile:
    config = json.load(configFile)

scriptNames = [name for name in config["chatAPI"]]

def printScriptNames():
    for name in scriptNames: print(name)

print("Available scripts:")
printScriptNames()


chatAPIscriptName = input('Enter the chatAPI script name (default will be: '+ scriptNames[0]+ '): ').strip() or scriptNames[0]

# Set up your OpenAI API key
client = OpenAI()

# Load project config:
if chatAPIscriptName not in config["chatAPI"]:
    print("No scriptName: " + chatAPIscriptName)
    print("Available options are: " )
    printScriptNames()
    sys.exit(1)
config = config["chatAPI"][chatAPIscriptName]


# Read the contents of the DOM file to be analyzed
with open(config["DOMsourcePath"], 'r') as file:
    file_content = file.read()

# Read the file that contains the prompts instructions:
with open(config["promptPath"], 'r') as file:
    prompt_text = file.read()

# Combine file content with prompt text
combined_text = prompt_text + file_content

print("--------")
print("Running chatGPT with Prompt:")
print(prompt_text)
print("--------")

# Send combined text to the OpenAI API for processing
response = client.chat.completions.create(
    messages= [
        {"role": "system", "content": config["systemContent"]},
        {"role": "user", "content": combined_text}
    ],
    model=config["model"]
)
answer = response.choices[0].message.content

print(prompt_text)
print("--------")
print("OpenAI answer:")
print("--------")
print(answer)

# Write the anwser to a file
with open(config["outputPath"], 'w+') as file:
    file.write(answer)



