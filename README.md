Hiring test for YoungApp.co

Instruction: https://github.com/youngapp/hiring-candidate/blob/master/BACKEND.md

Simple Python program which will give you the JSON intents of a sentence using LUIS Machine Learning engine.
This works only with Pizzas. Example :
>'I want two large pepperoni pizzas on thin crust please'
will give you :
>{'query': 'I want two large pepperoni pizzas on thin crust please', 'prediction': {'topIntent': 'ModifyOrder', 'intents': {'ModifyOrder': {'score': 1.0}, 'None': {'score': 8.55e-09}, 'Greetings': {'score': 1.82222226e-09}, 'CancelOrder': {'score': 1.47272727e-09}, 'Confirmation': {'score': 9.8125e-10}}, 'entities': {'Order': [{'FullPizzaWithModifiers': [{'PizzaType': ['pepperoni pizzas'], 'Size': [['Large']], 'Quantity': [2], 'Crust': [['Thin']], '$instance': {'PizzaType': [{'type': 'PizzaType', 'text': 'pepperoni pizzas', 'startIndex': 17, 'length': 16, 'score': 0.9978157, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}], (...)


Install:
1. You need to install theses Python modules: requests, unittest, python-dotenv
2. You need to create an account on Microsoft Azure and LUIS
3. Follow theses instruction: https://docs.microsoft.com/bs-cyrl-ba/azure/cognitive-services/LUIS/luis-get-started-get-intent-from-rest?pivots=programming-language-python
4. Create a .env file in the root of the project, copy the content of template.env, and replace the default values with your constants


Usage:
There is no usage, I just had to code an OOP class with an unit test. If you want to run the tests:
cd srcs && python -m unittest test/luis_retriever_test.py