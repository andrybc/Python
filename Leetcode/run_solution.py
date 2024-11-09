import importlib
import os
import inspect
import ast
from list_node import ListNode, create_linked_list
import re

def create_linked_list_of_strings(values):
    """Helper function to create a linked list from a list of string values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def parse_argument(arg, expected_type, array_element_type=None):
    """Parses an argument based on its expected type and nested types."""
    try:
        if expected_type == "int":
            return int(arg)
        elif expected_type == "float":
            return float(arg)
        elif expected_type == "bool":
            return arg.lower() == "true"
        elif expected_type == "str":
            return arg

        elif expected_type == "array":
            values = ast.literal_eval(arg)
            if isinstance(values, list):
                return [parse_argument(str(val), array_element_type) for val in values]

        elif expected_type == "linked_list":
            values = ast.literal_eval(arg)
            if isinstance(values, list):
                if array_element_type == "int":
                    return create_linked_list(values)
                elif array_element_type == "str":
                    return create_linked_list_of_strings(values)

        elif expected_type == "tuple":
            values = ast.literal_eval(arg)
            if isinstance(values, tuple):
                return tuple(parse_argument(str(val), array_element_type) for val in values)

        elif expected_type == "dict":
            values = ast.literal_eval(arg)
            if isinstance(values, dict):
                return {key: parse_argument(str(value), detect_type(value)) for key, value in values.items()}

    except (ValueError, SyntaxError):
        return arg

def detect_type(value):
    """Dynamically detect the type of a dictionary value for parsing purposes."""
    if isinstance(value, int):
        return "int"
    elif isinstance(value, float):
        return "float"
    elif isinstance(value, bool):
        return "bool"
    elif isinstance(value, str):
        return "str"
    elif isinstance(value, list):
        return "array"
    elif isinstance(value, tuple):
        return "tuple"
    elif isinstance(value, dict):
        return "dict"
    else:
        return "str"
    
def format_output(output):
    """Format the output based on its data structure for clean printing."""
    # Detect if output is a linked list (based on attributes rather than class)
    if hasattr(output, "val") and hasattr(output, "next"):
        # Convert linked list to a Python list for display
        result = []
        current = output
        while current:
            result.append(current.val)
            current = current.next
        return result

    elif isinstance(output, list):
        # Format each element in the list recursively
        return [format_output(elem) for elem in output]

    elif isinstance(output, tuple):
        # Format each element in the tuple recursively
        return tuple(format_output(elem) for elem in output)

    elif isinstance(output, dict):
        # Format each value in the dictionary recursively
        return {key: format_output(value) for key, value in output.items()}

    else:
        # Return basic data types directly
        return output
    
    
def get_parameters():
    """Prompt the user to define the parameters once at the beginning."""
    param_types = input("Enter the parameter types (e.g., 'int array dict'): ").split()
    element_types = []

    for param_type in param_types:
        if param_type in ("array", "linked_list", "tuple"):
            element_type = input(f"Specify the data type for elements in the {param_type} (int, str, bool, dict, tuple): ")
            element_types.append(element_type)
        else:
            element_types.append(None)

    return param_types, element_types

def run_solution(solution_name, method_name, *args):
    """Run the solution's method with the provided arguments."""
    try:
        module = importlib.import_module(f'solutions.{solution_name}')
        solution = module.Solution()
        
        if not hasattr(solution, method_name):
            print(f"Error: Method '{method_name}' not found in '{solution_name}.py'.")
            return
        
        method = getattr(solution, method_name)
        result = method(*args)
        
        # Format and print the result based on its data structure
        formatted_result = format_output(result)
        print(f"Result: {formatted_result}")

    except ModuleNotFoundError:
        print(f"Error: Solution file '{solution_name}.py' does not exist in the 'solutions' folder.")
    except TypeError as e:
        print(f"Error: Incorrect arguments for the method '{method_name}'.")
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    solution_name = input("Enter the solution file name (without .py extension): ")
    if not os.path.isfile(f'solutions/{solution_name}.py'):
        print(f"Error: Solution file '{solution_name}.py' does not exist.")
        return

    method_name = input("Enter the method name to run (e.g., addTwoNumbers): ")

    param_types, element_types = get_parameters()

    while True:
        try:
            args = []
            for i, param_type in enumerate(param_types):
                if param_type in ("array", "linked_list", "tuple", "dict"):
                    element_type = element_types[i]
                    arg = input(f"Enter the {param_type} of {element_type}s: ")
                    parsed_arg = parse_argument(arg, param_type, element_type)
                else:
                    arg = input(f"Enter the {param_type} argument: ")
                    parsed_arg = parse_argument(arg, param_type)
                args.append(parsed_arg)
            
            run_solution(solution_name, method_name, *args)

            continue_choice = input("Enter 'exit' to quit or press Enter to try new arguments: ").strip().lower()
            if continue_choice == "exit":
                print("Exiting the script.")
                break

        except KeyboardInterrupt:
            print("\nExiting the script.")
            break

if __name__ == "__main__":
    main()
