import os

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