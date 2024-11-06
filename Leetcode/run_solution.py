# run_solution.py
import importlib
import os
import inspect
import ast

def parse_argument(arg):
    """Parses an argument to handle lists and integers correctly."""
    try:
        # Attempt to parse the argument as a Python literal (e.g., list, int)
        return ast.literal_eval(arg)
    except (ValueError, SyntaxError):
        # If it’s not a list or int, return it as a string (fallback)
        return arg

def run_solution(solution_name, method_name, *args):
    try:
        # Dynamically import the selected solution module
        module = importlib.import_module(f'solutions.{solution_name}')
        solution = module.Solution()
        
        # Check if the method exists in the Solution class
        if not hasattr(solution, method_name):
            print(f"Error: Method '{method_name}' not found in '{solution_name}.py'.")
            return
        
        # Get the method and inspect its signature
        method = getattr(solution, method_name)
        sig = inspect.signature(method)
        
        # Parse and convert arguments to match the parameter types
        typed_args = []
        for arg, param in zip(args, sig.parameters.values()):
            parsed_arg = parse_argument(arg)
            # Check if the parsed argument matches the expected type
            if param.annotation != param.empty and not isinstance(parsed_arg, param.annotation):
                print(f"Error: Argument '{parsed_arg}' does not match the expected type {param.annotation}.")
                return
            typed_args.append(parsed_arg)

        # Run the method with typed arguments
        result = method(*typed_args)
        print(f"Result: {result}")
    
    except ModuleNotFoundError:
        print(f"Error: Solution file '{solution_name}.py' does not exist in the 'solutions' folder.")
    except TypeError:
        print(f"Error: Incorrect arguments for the method '{method_name}'. Please check the input format.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Prompt for the solution file name and method name once
    solution_name = input("Enter the solution file name (without .py extension): ")
    
    # Check if the solution file exists
    if not os.path.isfile(f'solutions/{solution_name}.py'):
        print(f"Error: Solution file '{solution_name}.py' does not exist.")
        return

    # Get method name to execute
    method_name = input("Enter the method name to run (e.g., twoSum): ")

    # Loop to continuously prompt for new arguments and run the solution
    while True:
        try:
            # Prompt for arguments and parse them
            args_input = input("Enter the arguments for the method, separated by spaces (or type 'exit' to quit): ").split()
            if args_input and args_input[0].lower() == 'exit':
                print("Exiting the script.")
                break
            
            # Run the solution with the provided method and arguments
            run_solution(solution_name, method_name, *args_input)
        
        except KeyboardInterrupt:
            print("\nExiting the script.")
            break

if __name__ == "__main__":
    main()
