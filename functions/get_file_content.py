import os

from google.genai import types

from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_full_path = os.path.abspath(os.path.join(working_directory, file_path))
        
        if(not abs_full_path.startswith(abs_working_dir)):
            return(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')

        if(not os.path.isfile(abs_full_path)):
            return(f'Error: File not found or is not a regular file: "{file_path}"')
        
        with open(abs_full_path, 'r') as file:
            file_content = file.read()
            
        if(len(file_content) >= MAX_CHARS):
            formated_content = f"{file_content[:MAX_CHARS]}" + ' [...File "{file_path}" truncated at 10000 characters]'
            
            return(formated_content)
        
        else:
            return(file_content)
    
    except Exception as e:
        return(f'Error: {str(e)}')
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read the content of a file and limits its output to 10000 characters",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to read content from, relative to the working directory.",
            ),
        },
    ),
)

