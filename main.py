import urls
import inspect


def get_parameters_from_docstring(docstring):
    param_info = []

    for line in docstring.strip().split("\n"):
        line = line.strip()
        if line.startswith("Returns:"):
            break
        if ":" in line:
            parts = line.split(":", 1)
            if len(parts) == 2 and parts[0].strip() and parts[1].strip():
                param_name_and_type, param_desc = parts[0].strip(), parts[1].strip()

                if "(" in param_name_and_type and ")" in param_name_and_type:
                    param_name, type_info = param_name_and_type.split("(")
                    param_name = param_name.strip()
                    type_info = type_info.replace(")", "").strip()
                    param_info.append((param_name, param_desc, type_info))
                else:
                    param_name = param_name_and_type
                    type_info = None
                    param_info.append((param_name, param_desc, type_info))

    return param_info


def build_urls_dict(module):
    urls_dict = {}
    for name, func in module.__dict__.items():
        if callable(func) and func.__doc__:
            param_info = get_parameters_from_docstring(func.__doc__)

            sig = inspect.signature(func)
            default_values = {}
            for param in sig.parameters.values():
                if param.default is not inspect.Parameter.empty:
                    default_values[param.name] = param.default

            urls_dict[name] = (func, param_info, default_values)
    return urls_dict


def console():
    urls_dict = build_urls_dict(urls)

    while True:
        command = input("> ")
        if command in urls_dict:
            func, param_info, default_values = urls_dict[command]

            try:
                if not param_info:
                    r = func()
                else:
                    params = []

                    for param_name, param_desc, type_info in param_info:
                        if param_name in default_values:
                            default_value = default_values[param_name]
                            input_str = input(f"Enter {param_desc} ({type_info}) (default: {default_value}): ")
                            if input_str:
                                param_value = eval(type_info)(input_str)
                            else:
                                param_value = default_value
                        else:
                            while True:
                                input_str = input(f"Enter {param_desc} ({type_info}): ")
                                try:
                                    if type_info:
                                        param_value = eval(type_info)(input_str)
                                    else:
                                        param_value = input_str
                                    break
                                except ValueError:
                                    print("Invalid input")

                        params.append(param_value)

                    r = func(*params)

                if r is not None:
                    if isinstance(r, dict):
                        for key, value in r.items():
                            print(f"{key}: {value}")
                    else:
                        print(r)
            except Exception as e:
                print(f"An error occurred: {e}")

        elif command == "quit":
            quit()
        else:
            print("Unknown command")


if __name__ == "__main__":
    console()
