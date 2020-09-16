import unittest
from luis.luis_retriever import LUISRetriever

class LUISRetrieverTest(unittest.TestCase):

	"""
	Test of the LUISRetriever class.
	"""

	def _test_pizza(self, sentence, theory):
		"""
		Used to compare the result of the API with the theory result.

		Args:
			sentence: str - the sentence we will analyze
			theory: dict - the output theory

		TODO: Maybe compare dicts without the scores (eg: 'score': 0.994500756), because if we retrain
			  our dataset, theses scores could change
		"""
		result = LUISRetriever(sentence).call()

		#Asserting there is a result
		self.assertIsNotNone(result)

		#Asserting the response is a dict
		self.assertIsInstance(result, dict)

		#Asserting the output is exact
		self.assertEqual(result, theory)

		print("'{}' --> OK".format(sentence))


	def test_good_pizzas(self):
		"""
		This function will test the LUIS response with some good pizzas.
		"""

		sentence = 'I want two large pepperoni pizzas on thin crust please'
		theory = {'query': 'I want two large pepperoni pizzas on thin crust please', 'prediction': {'topIntent': 'ModifyOrder', 'intents': {'ModifyOrder': {'score': 1.0}, 'None': {'score': 8.55e-09}, 'Greetings': {'score': 1.82222226e-09}, 'CancelOrder': {'score': 1.47272727e-09}, 'Confirmation': {'score': 9.8125e-10}}, 'entities': {'Order': [{'FullPizzaWithModifiers': [{'PizzaType': ['pepperoni pizzas'], 'Size': [['Large']], 'Quantity': [2], 'Crust': [['Thin']], '$instance': {'PizzaType': [{'type': 'PizzaType', 'text': 'pepperoni pizzas', 'startIndex': 17, 'length': 16, 'score': 0.9978157, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}], 'Size': [{'type': 'SizeList', 'text': 'large', 'startIndex': 11, 'length': 5, 'score': 0.9984481, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}], 'Quantity': [{'type': 'builtin.number', 'text': 'two', 'startIndex': 7, 'length': 3, 'score': 0.999770939, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}], 'Crust': [{'type': 'CrustList', 'text': 'thin crust', 'startIndex': 37, 'length': 10, 'score': 0.933985531, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}]}}], '$instance': {'FullPizzaWithModifiers': [{'type': 'FullPizzaWithModifiers', 'text': 'two large pepperoni pizzas on thin crust', 'startIndex': 7, 'length': 40, 'score': 0.90681237, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}]}}], 'ToppingList': [['Pepperoni']], '$instance': {'Order': [{'type': 'Order', 'text': 'two large pepperoni pizzas on thin crust', 'startIndex': 7, 'length': 40, 'score': 0.9047088, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}], 'ToppingList': [{'type': 'ToppingList', 'text': 'pepperoni', 'startIndex': 17, 'length': 9, 'modelTypeId': 5, 'modelType': 'List Entity Extractor', 'recognitionSources': ['model']}]}}}}
		self._test_pizza(sentence, theory)

		sentence = 'Can I have a parmesan pizza on pan crust?'
		theory = {'query': 'Can I have a parmesan pizza on pan crust?', 'prediction': {'topIntent': 'ModifyOrder', 'intents': {'ModifyOrder': {'score': 1.0}, 'None': {'score': 8.55e-09}, 'Greetings': {'score': 1.82222226e-09}, 'CancelOrder': {'score': 1.47272727e-09}, 'Confirmation': {'score': 9.8125e-10}}, 'entities': {'Order': [{'FullPizzaWithModifiers': [{'PizzaType': ['parmesan pizza'], 'Crust': [['Pan']], '$instance': {'PizzaType': [{'type': 'PizzaType', 'text': 'parmesan pizza', 'startIndex': 13, 'length': 14, 'score': 0.6931204, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}], 'Crust': [{'type': 'CrustList', 'text': 'pan crust', 'startIndex': 31, 'length': 9, 'score': 0.5911143, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}]}}], '$instance': {'FullPizzaWithModifiers': [{'type': 'FullPizzaWithModifiers', 'text': 'a parmesan pizza on pan crust', 'startIndex': 11, 'length': 29, 'score': 0.559578359, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}]}}], 'ToppingList': [['Parmesan Cheese']], '$instance': {'Order': [{'type': 'Order', 'text': 'a parmesan pizza on pan crust', 'startIndex': 11, 'length': 29, 'score': 0.481073946, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}], 'ToppingList': [{'type': 'ToppingList', 'text': 'parmesan', 'startIndex': 13, 'length': 8, 'modelTypeId': 5, 'modelType': 'List Entity Extractor', 'recognitionSources': ['model']}]}}}}
		self._test_pizza(sentence, theory)

		sentence = 'I want a pizza on pan crust with chicken, eggplant, cheddar and Beef'
		theory = {'query': 'I want a pizza on pan crust with chicken, eggplant, cheddar and Beef', 'prediction': {'topIntent': 'ModifyOrder', 'intents': {'ModifyOrder': {'score': 1.0}, 'None': {'score': 8.55e-09}, 'Greetings': {'score': 1.82222226e-09}, 'CancelOrder': {'score': 1.47272727e-09}, 'Confirmation': {'score': 9.8125e-10}}, 'entities': {'Order': [{'FullPizzaWithModifiers': [{'PizzaType': ['pizza'], 'Crust': [['Pan']], 'ToppingModifiers': [{'Topping': [['Chicken'], ['Eggplant'], ['Cheddar'], ['Beef']], 'Modifier': [['Add']], '$instance': {'Topping': [{'type': 'ToppingList', 'text': 'chicken', 'startIndex': 33, 'length': 7, 'score': 0.9968178, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}, {'type': 'ToppingList', 'text': 'eggplant', 'startIndex': 42, 'length': 8, 'score': 0.986775458, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}, {'type': 'ToppingList', 'text': 'cheddar', 'startIndex': 52, 'length': 7, 'score': 0.995619, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}, {'type': 'ToppingList', 'text': 'Beef', 'startIndex': 64, 'length': 4, 'score': 0.9698927, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}], 'Modifier': [{'type': 'ModifierList', 'text': 'with', 'startIndex': 28, 'length': 4, 'score': 0.9916684, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}]}}], '$instance': {'PizzaType': [{'type': 'PizzaType', 'text': 'pizza', 'startIndex': 9, 'length': 5, 'score': 0.986509562, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}], 'Crust': [{'type': 'CrustList', 'text': 'pan crust', 'startIndex': 18, 'length': 9, 'score': 0.6447228, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}], 'ToppingModifiers': [{'type': 'ToppingModifiers', 'text': 'with chicken, eggplant, cheddar and Beef', 'startIndex': 28, 'length': 40, 'score': 0.390196383, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}]}}], '$instance': {'FullPizzaWithModifiers': [{'type': 'FullPizzaWithModifiers', 'text': 'a pizza on pan crust with chicken, eggplant, cheddar and Beef', 'startIndex': 7, 'length': 61, 'score': 0.960103154, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}]}}], '$instance': {'Order': [{'type': 'Order', 'text': 'a pizza on pan crust with chicken, eggplant, cheddar and Beef', 'startIndex': 7, 'length': 61, 'score': 0.994500756, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}]}}}}
		self._test_pizza(sentence, theory)

	
	def test_bad_pizzas(self):
		"""
		This function will test the LUIS response with some bad pizzas.
		"""

		sentence = 'I want a computer'
		theory = {'query': 'I want a computer', 'prediction': {'topIntent': 'ModifyOrder', 'intents': {'ModifyOrder': {'score': 0.06401406}, 'Confirmation': {'score': 0.03185104}, 'Greetings': {'score': 0.008373831}, 'CancelOrder': {'score': 0.00583848543}, 'None': {'score': 0.00109198678}}, 'entities': {}}}
		self._test_pizza(sentence, theory)

		sentence = 'Can I have a zebra?'
		theory = {'query': 'Can I have a zebra?', 'prediction': {'topIntent': 'ModifyOrder', 'intents': {'ModifyOrder': {'score': 0.04325798}, 'Confirmation': {'score': 0.0226381365}, 'Greetings': {'score': 0.0037291937}, 'CancelOrder': {'score': 0.003312903}, 'None': {'score': 0.00230691512}}, 'entities': {}}}
		self._test_pizza(sentence, theory)

