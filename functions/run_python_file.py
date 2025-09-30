import os
import sys
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    try:
        
        abs_working_dir = os.path.abspath(working_directory)
        abs_full_path = os.path.abspath(os.path.join(working_directory, file_path))
        
        if not abs_full_path.startswith(abs_working_dir):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(abs_full_path):
            return f'Error: File "{file_path}" not found.'
        
        if not abs_full_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'
        
        completed_process = subprocess.run([sys.executable, abs_full_path, *args], capture_output=True, text=True, cwd=abs_working_dir, timeout=30)
        
        output_parts = []
        if completed_process.stdout:
            output_parts.append(f"STDOUT:\n{completed_process.stdout}")
            
        if completed_process.stderr:
            output_parts.append(f"STDERR:\n{completed_process.stderr}")
            
        if completed_process.returncode != 0:
            output_parts.append(f"Process exited with code {completed_process.returncode}")
            
        if not output_parts:
            return "No output produced."
        
        return "\n".join(output_parts)
    
    except subprocess.TimeoutExpired:
        return f'Process timed out after 30s: "{file_path}"'
    
    except Exception as e:
        return f'Error: {str(e)}'
