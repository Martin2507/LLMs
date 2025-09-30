import os

from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_full_path = os.path.abspath(os.path.join(working_directory, file_path))
        
        if(not abs_full_path.startswith(abs_working_dir)):
            return(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        
        with open(abs_full_path, 'w') as f:
            f.write(content)
            
        with open(abs_full_path, 'r') as f:
            new_content = f.read()
            
            if(content in new_content):
                return(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
            
                
        
    except Exception as e:
        return(f'Error: {str(e)}')
    
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write a provided content to the file based on the provided path to that file, if the file does not exist create a new one",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to write content to, relative to the working directory.",
            ),
            "content": types.Schema(  # <-- fixed here
                type=types.Type.STRING,
                description="The content to write to the file"
            )
        },
    ),
)
