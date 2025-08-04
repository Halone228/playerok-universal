#!/usr/bin/env python3
"""
Скрипт для автоматического преобразования обычных классов в Pydantic модели
с использованием Annotated pattern.
"""

import re
import sys

def convert_class_to_pydantic(content):
    """Конвертирует обычные классы в Pydantic модели."""
    
    # Паттерн для поиска класса с __init__ методом
    class_pattern = r'class\s+(\w+):\s*\n((?:\s*"""[\s\S]*?"""\s*\n)?)\s*def\s+__init__\(self,([^)]*)\):\s*\n([\s\S]*?)(?=\nclass|\nif\s+TYPE_CHECKING|\Z)'
    
    def replace_class(match):
        class_name = match.group(1)
        docstring = match.group(2) if match.group(2) else ""
        init_params = match.group(3)
        init_body = match.group(4)
        
        # Извлекаем параметры из __init__
        params = []
        if init_params.strip():
            param_lines = init_params.split(',')
            for param in param_lines:
                param = param.strip()
                if param and param != 'self':
                    params.append(param)
        
        # Создаем Pydantic поля
        pydantic_fields = []
        for param in params:
            # Парсим параметр: name: type = default
            param_match = re.match(r'(\w+):\s*([^=]+)(?:\s*=\s*(.+))?', param)
            if param_match:
                param_name = param_match.group(1)
                param_type = param_match.group(2).strip()
                param_default = param_match.group(3)
                
                # Ищем описание поля в init_body
                description_match = re.search(
                    rf'self\.{param_name}:[^=]*=\s*{param_name}\s*\n\s*"""\s*([^"]+)\s*"""',
                    init_body
                )
                description = description_match.group(1).strip() if description_match else f"{param_name}"
                
                # Создаем Annotated поле
                if param_default and param_default.strip() != 'None':
                    if '|' in param_type and 'None' in param_type:
                        pydantic_fields.append(f'    {param_name}: Annotated[{param_type}, Field({param_default}, description="{description}")]')
                    else:
                        pydantic_fields.append(f'    {param_name}: Annotated[{param_type}, Field({param_default}, description="{description}")]')
                elif '|' in param_type and 'None' in param_type:
                    pydantic_fields.append(f'    {param_name}: Annotated[{param_type}, Field(None, description="{description}")]')
                else:
                    pydantic_fields.append(f'    {param_name}: Annotated[{param_type}, Field(description="{description}")]')
        
        # Собираем новый класс
        new_class = f'class {class_name}(BaseModel):\n{docstring}'
        if pydantic_fields:
            new_class += '\n'.join(pydantic_fields)
        else:
            new_class += '    pass'
        
        return new_class
    
    # Применяем замену
    new_content = re.sub(class_pattern, replace_class, content, flags=re.MULTILINE)
    
    return new_content

def main():
    input_file = '/home/halone/projects/playerok-universal/playerokapi/types.py'
    
    # Читаем файл
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Конвертируем
    new_content = convert_class_to_pydantic(content)
    
    # Записываем обратно
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("Конвертация завершена!")

if __name__ == '__main__':
    main()
