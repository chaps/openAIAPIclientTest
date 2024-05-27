
## Requirements:
- Install python
- For running UI based scripts please install the following for UI:
  - `brew install python-tk`

## 1: Setup OpenAI API Key

you can copy the `.env.template` to generate a new .env file with the following command 
`cp .env.template .env`
OR create a file named `.env`
in the created `.env` file define the OPENAI API KEY variable with the following code and 
add the API key value to the new `.env` file:
```
OPENAI_API_KEY=""
```

## 2: Create a virtual environment:

or run the following commands:
```
python3 -m venv openai-env
source openai-env/bin/activate
```

## 3: Install the project dependencies:
```
pip3 install -r requirements.txt
```

## 4: source the defined api key to the loaded env vars: 
```
source .env
```






