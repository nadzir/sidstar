from .listuitl import *

class TestList:

   def test_get_top_occurences_from_list_should_return_result_when_valid_list(self):
       items = [1, 1, 2, 3]
       expected_result = [(1, 2)]
       actual_result =get_top_occurences_from_list(items, 1)
       assert expected_result == actual_result
   
       items = ["a", "a", "b", "c"]
       expected_result = [("a", 2)]
       actual_result = get_top_occurences_from_list(items, 1)
       assert expected_result == actual_result
   
   
   def test_get_top_occurences_from_list_should_return_empty_array_when_null(self):
       items = None
       expected_result = []
       actual_result = get_top_occurences_from_list(items)
       assert expected_result == actual_result
   
       items = []
       num_of_elements = None
       expected_result = []
       actual_result = get_top_occurences_from_list(
           items, num_of_elements=num_of_elements
       )
       assert expected_result == actual_result
   
       items = None
       num_of_elements = None
       expected_result = []
       actual_result = get_top_occurences_from_list(
           items, num_of_elements=num_of_elements
       )
       assert expected_result == actual_result
   
   
   def test_get_top_occurences_from_list_should_return_empty_array_when_invalid_type(self):
       items = "string"
       expected_result = []
       actual_result = get_top_occurences_from_list(items)
       assert expected_result == actual_result
   
       items = 1
       expected_result = []
       actual_result = get_top_occurences_from_list(items)
       assert expected_result == actual_result
